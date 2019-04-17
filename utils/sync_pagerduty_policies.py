#!/usr/bin/env python
#
# Synchronize list of escalation policies with notification channels in Sysdig
#
import argparse
import json
import os
import sys

import requests

sys.path.insert(
    0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))

from sdcclient import SdMonitorClient


#
# Parse arguments
#
parser = argparse.ArgumentParser(
    description='Synchronize PagerDuty escalation policies with Sysdig, to make sure each escalation policy has a notification channel enabled in Sysdig')
parser.add_argument('sysdig-token', nargs=1, help='Sysdig API token')
parser.add_argument(
    'pagerduty-account-id', nargs=1, help='PagerDuty account ID')
parser.add_argument(
    'pagerduty-access-key', nargs=1, help='PagerDuty API access key')
parser.add_argument(
    '--link',
    action='store_true',
    help='Set to creat notification channels in Sysdig and services in PagerDuty for all escalation policies'
)
parser.add_argument(
    '--unlink',
    action='store_true',
    help='Set to remove notification channels connected to PagerDuty escalation policies'
)
parser.add_argument(
    '--dry-run',
    action='store_true',
    help='Set to get a report of changes, without actually apply them')

args = vars(parser.parse_args())


def run(sysdig_token, pager_duty_id, pager_duty_token, link, unlink, dry_run):
    sysdig = SdMonitorClient(sysdig_token)
    pager_duty = PagerDutyAPI(pager_duty_token)
    actions_factory = ActionFactory(sysdig, pager_duty, pager_duty_id)

    #
    # Get list of Sysdig notification channels
    #
    ok, res = sysdig.list_notification_channels()
    if not ok:
        print('\nUnable to fetch Sysdig notification channels')
        print(res)
        sys.exit(1)

    #
    # Find PagerDuty notification channels
    #
    pagerduty_channels = filter(lambda channel: channel['type'] == 'PAGER_DUTY',
                                res['notificationChannels'])
    print('Found {} PagerDuty notification {} configured in Sysdig'.format(
        len(pagerduty_channels), pluralize('channel', len(pagerduty_channels))))
    # print(json.dumps(pagerduty_channels, sort_keys=True, indent=4))

    #
    # Get list of PagerDuty escalation policies
    #
    escalation_policies = pager_duty.get(
        '/escalation_policies')['escalation_policies']
    print('Found {} PagerDuty escalation {}'.format(
        len(escalation_policies),
        pluralize('policy', len(escalation_policies), 'policies')))
    escalation_policies_map = {}
    for escalation_policy in escalation_policies:
        escalation_policies_map[escalation_policy['id']] = escalation_policy
    # print(json.dumps(escalation_policies, sort_keys=True, indent=4))

    #
    # Get list of PagerDuty services
    #
    services = pager_duty.get('/services', {'include[]': ['integrations']})['services']
    print('Found {} PagerDuty {}'.format(
        len(services), pluralize('service', len(services))))
    # print(json.dumps(services, sort_keys=True, indent=4))

    #
    # Get integration details
    #
    for service in services:
        for integration in service['integrations']:
            integration['details'] = pager_duty.get(
                '/services/{}/integrations/{}'.format(service['id'], integration['id']))['integration']

    #
    # Find integrations with Sysdig
    #

    # Build map of notification channel -> integration key

    def get_integration_map(acc, channel):
        acc[channel['options']['serviceKey']] = channel
        return acc

    integration_keys = reduce(get_integration_map, pagerduty_channels, {})

    for service in services:
        service['sysdig_integrations'] = filter(
            lambda integration: integration['integration_key'] in integration_keys, service['integrations'])

    #
    # Get actions
    #
    actions = []
    if unlink:
        # delete all notification channels
        for channel in pagerduty_channels:
            actions.append({
                'info': 'Sysdig: Delete channel "{}" ({})'.format(channel['name'], channel['id']),
                'fn': actions_factory.delete_notification_channel(channel)
            })

        # delete integration with Sysdig, and services left with no integrations
        for service in services:
            if service['sysdig_integrations']:
                if len(service['sysdig_integrations']) == len(service['integrations']):
                    actions.append({
                        'info': 'PagerDuty: Delete service "{}" ({})'.format(service['name'], service['id']),
                        'fn': actions_factory.delete_service(service['id'])
                    })
                else:
                    for integration in service['sysdig_integrations']:
                        actions.append({
                            'info': 'PagerDuty: Delete integration "{}" ({}) in service "{}" ({})'.format(integration['name'], integration['id'], service['name'], service['id']),
                            'fn': actions_factory.delete_integration(service['id'], integration['id'])
                        })
            elif service['name'] == '{} (Sysdig)'.format(escalation_policies_map[service['escalation_policy']['id']]['name']):
                # delete service that this script (very likely) created in the past (based on the name)
                actions.append({
                    'info': 'PagerDuty: Delete service "{}" ({})'.format(service['name'], service['id']),
                    'fn': actions_factory.delete_service(service['id'])
                })

    if link:
        # create services
        for policy in escalation_policies:
            service_name = '{} (Sysdig)'.format(policy['name'])

            policy_services = filter(lambda service: service['escalation_policy']['id'] == policy['id'], services)
            valid_services = filter(lambda service: service['name'] ==
                                    service_name and service['sysdig_integrations'], policy_services)

            if not valid_services:
                # create service, integration, notification channel
                actions.append({
                    'info': 'Create service, integration, and notification channel for policy "{}"'.format(policy['name']),
                    'fn': actions_factory.create_all(policy)
                })

    if actions:
        #
        # Run action, or just print the task in dry mode
        #
        print('')
        print('Performing the following actions:')
        for action in actions:
            if dry_run:
                print('\t* {}'.format(action['info']))
            else:
                print('\t* {}...'.format(action['info']))
                action['fn']()
                print('\t  Done!')

    else:
        if unlink:
            print('All escalation policies have been disconnected from Sysdig!')
        if link:
            print('All escalation policies are already connected to Sysdig!')


class PagerDutyAPI():
    def __init__(self, token):
        self._base_url = 'https://api.pagerduty.com'
        self._token = token

    def get(self, endpoint, params=None):
        return self._base_request('get', endpoint, params=params)

    def post(self, endpoint, data=None):
        return self._base_request('post', endpoint, data=data)

    def delete(self, endpoint, params=None):
        return self._base_request('delete', endpoint, params=params)

    def _base_request(self, method, endpoint, params=None, data=None):
        url = self._get_url(endpoint)
        request_data = json.dumps(data) if data else None
        response = getattr(requests, method)(url, params=params, data=request_data, headers=self._get_headers())

        return self._handle_response(response, url)

    def _handle_response(self, response, url):
        if response.status_code >= 300:
            error = 'PagerDuty API request {} {} failed: {}, {}'.format(
                response.request.method, url, response.status_code, response.content)

            print(error)
            raise Exception(error)
        elif response.status_code == 204:
            return None
        else:
            return self._parse_response(response)

    def _parse_response(self, response):
        return response.json()

    def _get_url(self, endpoint):
        return '{}{}'.format(self._base_url, endpoint)

    def _get_headers(self):
        return {
            'Accept': 'application/vnd.pagerduty+json;version=2',
            'Content-Type': 'application/json',
            'Authorization': 'Token token={}'.format(self._token)
        }


class ActionFactory():
    def __init__(self, sysdig, pager_duty, pager_duty_id):
        self._sysdig = sysdig
        self._pager_duty = pager_duty
        self._pager_duty_id = pager_duty_id

    def delete_service(self, service_id):
        def fn():
            self._pager_duty.delete('/services/{}'.format(service_id))

        return fn

    def delete_integration(self, service_id, integration_id):
        def fn():
            self._pager_duty.delete('/services/{}/integrations/{}'.format(service_id, integration_id))

        return fn

    def delete_notification_channel(self, channel):
        def fn():
            self._sysdig.delete_notification_channel(channel)

        return fn

    def create_all(self, policy):
        def fn():
            new_service = self._pager_duty.post('/services', {
                'service': {
                    'type': 'service',
                    'name': '{} (Sysdig)'.format(policy['name']),
                    'auto_resolve_timeout': None,
                    'acknowledgement_timeout': None,
                    'status': 'active',
                    'escalation_policy': {
                        'id': policy['id'],
                        'type': 'escalation_policy_reference'
                    },
                    'incident_urgency_rule': {
                        'type': 'use_support_hours',
                        'during_support_hours': {
                            'type': 'constant',
                            'urgency': 'high'
                        },
                        'outside_support_hours': {
                            'type': 'constant',
                            'urgency': 'low'
                        }
                    },
                    'support_hours': {
                        'type': 'fixed_time_per_day',
                        'time_zone': 'America/Lima',
                        'start_time': '09:00:00',
                        'end_time': '17:00:00',
                        'days_of_week': [
                            1,
                            2,
                            3,
                            4,
                            5
                        ]
                    },
                    'scheduled_actions': [
                        {
                            'type': 'urgency_change',
                            'at': {
                                'type': 'named_time',
                                'name': 'support_hours_start'
                            },
                            'to_urgency': 'high'
                        }
                    ],
                    'alert_creation': 'create_alerts_and_incidents',
                    'alert_grouping': 'time',
                    'alert_grouping_timeout': 2
                }
            })['service']

            sysdig_vendor = self._pager_duty.get('/vendors?query=sysdig&limit=100&offset=0&total=false')['vendors'][0]

            new_integration = self._pager_duty.post('/services/{}/integrations'.format(new_service['id']), {
                'integration': {
                    'type': 'integration_inbound_integration',
                    'name': 'Sysdig',
                    'vendor': {
                        'id': sysdig_vendor['id'],
                        'type': 'vendor'
                    },
                    'service': {
                        'id': new_service['id'],
                        'summary': new_service['summary'],
                        'type': new_service['type'],
                        'self': new_service['self'],
                        'html_url': new_service['html_url'],
                    }
                }
            })['integration']

            self._sysdig.create_notification_channel({
                'type': 'PAGER_DUTY',
                'enabled': True,
                'sendTestNotification': False,
                'name': policy['name'],
                'options': {
                    'account': self._pager_duty_id,
                    'serviceKey': new_integration['integration_key'],
                    'serviceName': new_service['name'],
                    'notifyOnOk': True,
                    'notifyOnResolve': True
                }
            })

        return fn

    def create_notification_channel(self, policy, name, integration):
        def fn():
            self._sysdig.create_notification_channel({
                "type": "PAGER_DUTY",
                "enabled": True,
                "sendTestNotification": False,
                "name": name,
                "options": {
                    "account": self._pager_duty_id,
                    "serviceKey": integration['intergration_key'],
                    "serviceName": policy['name'],
                    "notifyOnOk": True,
                    "notifyOnResolve": True
                }
            })

        return fn


def pluralize(term, count, plural=None):
    if count == 1:
        return term
    else:
        if plural is None:
            return '{}s'.format(term)
        else:
            return plural


# let's get started!
print('')


run(args['sysdig-token'][0], args['pagerduty-account-id'][0],
    args['pagerduty-access-key'][0], args['link'], args['unlink'], args['dry_run'])
