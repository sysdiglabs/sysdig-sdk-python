import os
import json
import requests
import copy
import datetime

class _SdcCommon(object):
    '''Interact with the Sysdig Monitor/Secure API.

    **Arguments**
        - **token**: A Sysdig Monitor/Secure API token from the *Sysdig Cloud API* section of the Settings page for `monitor <https://app.sysdigcloud.com/#/settings/user>`_ or .`secure <https://secure.sysdig.com/#/settings/user>`_.
        - **sdc_url**: URL for contacting the Sysdig API server. Set this in `On-Premises installs <https://support.sysdigcloud.com/hc/en-us/articles/206519903-On-Premises-Installation-Guide>`__.
        - **ssl_verify**: Whether to verify certificate. Set to False if using a self-signed certificate in an `On-Premises install <https://support.sysdigcloud.com/hc/en-us/articles/206519903-On-Premises-Installation-Guide>`__.

    **Returns**
        An object for further interactions with the Sysdig Monitor/Secure API. See methods below.
    '''
    lasterr = None

    def __init__(self, token="", sdc_url='https://app.sysdigcloud.com', ssl_verify=True):
        self.token = os.environ.get("SDC_TOKEN", token)
        self.hdrs = {'Authorization': 'Bearer ' + self.token, 'Content-Type': 'application/json'}
        self.url = os.environ.get("SDC_URL", sdc_url)
        self.ssl_verify = os.environ.get("SDC_SSL_VERIFY", None)
        if self.ssl_verify == None:
            self.ssl_verify = ssl_verify
        else:
            self.ssl_verify = self.ssl_verify.lower() == 'true'

    def _checkResponse(self, res):
        if res.status_code >= 300:
            errorcode = res.status_code
            self.lasterr = None

            try:
                j = res.json()
            except:
                self.lasterr = 'status code ' + str(errorcode)
                return False

            if 'errors' in j:
                if 'message' in j['errors'][0]:
                    self.lasterr = j['errors'][0]['message']

                if 'reason' in j['errors'][0]:
                    if self.lasterr is not None:
                        self.lasterr += ' '
                    else:
                        self.lasrerr = ''

                    self.lasterr += j['errors'][0]['reason']
            elif 'message' in j:
                self.lasterr = j['message']
            else:
                self.lasterr = 'status code ' + str(errorcode)
            return False
        return True

    def get_user_info(self):
        '''**Description**
            Get details about the current user.

        **Success Return Value**
            A dictionary containing information about the user, for example its email and the maximum number of agents it can install.

        **Example**
            `examples/print_user_info.py <https://github.com/draios/python-sdc-client/blob/master/examples/print_user_info.py>`_
        '''
        res = requests.get(self.url + '/api/user/me', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def get_user_token(self):
        '''**Description**
            Return the API token of the current user.

        **Success Return Value**
            A string containing the user token.
        '''
        res = requests.get(self.url + '/api/token', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        tkinfo = res.json()

        return [True, tkinfo['token']['key']]

    def get_connected_agents(self):
        '''**Description**
            Return the agents currently connected to Sysdig Monitor for the current user.

        **Success Return Value**
            A list of the agents with all their attributes.
        '''
        res = requests.get(self.url + '/api/agents/connected', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        data = res.json()
        return [True, data['agents']]

    def get_n_connected_agents(self):
        '''**Description**
            Return the number of agents currently connected to Sysdig Monitor for the current user.

        **Success Return Value**
            An integer number.
        '''
        res = requests.get(self.url + '/api/agents/connected', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        data = res.json()
        return [True, data['total']]

    def get_notification_ids(self, channels):
            res = requests.get(self.url + '/api/notificationChannels', headers=self.hdrs, verify=self.ssl_verify)

            if not self._checkResponse(res):
                return [False, self.lasterr]

            # Should try and improve this M * N lookup
            ids = []
            for c in channels:
                found = False
                for ch in res.json()["notificationChannels"]:
                    if c['type'] == ch['type']:
                        if c['type'] == 'SNS':
                            opt = ch['options']
                            if set(opt['snsTopicARNs']) == set(c['snsTopicARNs']):
                                found = True
                                ids.append(ch['id'])
                        elif c['type'] == 'EMAIL':
                            opt = ch['options']
                            if 'emailRecipients' in c:
                                if set(c['emailRecipients']) == set(opt['emailRecipients']):
                                    found = True
                                    ids.append(ch['id'])
                            elif 'name' in c:
                                if c['name'] == ch['name']:
                                    found = True
                                    ids.append(ch['id'])
                        elif c['type'] == 'PAGER_DUTY':
                            opt = ch['options']
                            if opt['account'] == c['account'] and opt['serviceName'] == c['serviceName']:
                                found = True
                                ids.append(ch['id'])
                        elif c['type'] == 'SLACK':
                            opt = ch['options']
                            if 'channel' in opt and opt['channel'] == c['channel']:
                                found = True
                                ids.append(ch['id'])
                        elif c['type'] == 'OPSGENIE':
                            if 'name' in c:
                                if c['name'] == ch['name']:
                                    found = True
                                    ids.append(ch['id'])
                        elif c['type'] == 'WEBHOOK':
                            if 'name' in c:
                                if c['name'] == ch['name']:
                                    found = True
                                    ids.append(ch['id'])
                if not found:
                    return [False, "Channel not found: " + str(c)]

            return [True, ids]

    def create_email_notification_channel(self, channel_name, email_recipients):
        channel_json = {
            'notificationChannel' : {
                'type' : 'EMAIL',
                'name' : channel_name,
                'enabled' : True,
                'options' : {
                    'emailRecipients' : email_recipients
                }
            }
        }

        res = requests.post(self.url + '/api/notificationChannels', headers=self.hdrs, data=json.dumps(channel_json), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def get_notification_channel(self, id):

        res = requests.get(self.url + '/api/notificationChannels/' + str(id), headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()['notificationChannel']]

    def update_notification_channel(self, channel):
        if 'id' not in channel:
            return [False, "Invalid channel format"]

        res = requests.put(self.url + '/api/notificationChannels/' + str(channel['id']), headers=self.hdrs, data=json.dumps({ "notificationChannel": channel }), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def delete_notification_channel(self, channel):
        if 'id' not in channel:
            return [False, "Invalid channel format"]

        res = requests.delete(self.url + '/api/notificationChannels/' + str(channel['id']), headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, None]

    def get_data_retention_info(self):
        '''**Description**
            Return the list of data retention intervals, with beginning and end UTC time for each of them. Sysdig Monitor performs rollups of the data it stores. This means that data is stored at different time granularities depending on how far back in time it is. This call can be used to know what precision you can expect before you make a call to :func:`~SdcClient.get_data`.

        **Success Return Value**
            A dictionary containing the list of available sampling intervals.

        **Example**
            `examples/print_data_retention_info.py <https://github.com/draios/python-sdc-client/blob/master/examples/print_data_retention_info.py>`_
        '''
        res = requests.get(self.url + '/api/history/timelines/', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def get_topology_map(self, grouping_hierarchy, time_window_s, sampling_time_s):
        #
        # Craft the time interval section
        #
        tlines = self.get_data_retention_info()

        for tline in tlines[1]['agents']:
            if tline['sampling'] == sampling_time_s * 1000000:
                timeinfo = tline

        if timeinfo is None:
            return [False, "sampling time " + str(sampling_time_s) + " not supported"]

        timeinfo['from'] = timeinfo['to'] - timeinfo['sampling']

        #
        # Create the grouping hierarchy
        #
        gby = [{'metric': g} for g in grouping_hierarchy]

        #
        # Prepare the json
        #
        req_json = {
            'format': {
                'type': 'map',
                'exportProcess': True
            },
            'time': timeinfo,
            #'filter': {
            #    'filters': [
            #        {
            #            'metric': 'agent.tag.Tag',
            #            'op': '=',
            #            'value': 'production-maintenance',
            #            'filters': None
            #        }
            #    ],
            #    'logic': 'and'
            #},
            'limit': {
                'hostGroups': 20,
                'hosts': 20,
                'containers': 20,
                'processes': 10
            },
            'group': {
                'configuration': {
                    'groups': [
                        {
                            'filters': [],
                            'groupBy': gby
                        }
                    ]
                }
            },
            'nodeMetrics': [
                {
                    'id': 'cpu.used.percent',
                    'aggregation': 'timeAvg',
                    'groupAggregation': 'avg'
                }
            ],
            'linkMetrics': [
                {
                    'id': 'net.bytes.total',
                    'aggregation': 'timeAvg',
                    'groupAggregation': 'sum'
                }
            ]
        }

        #
        # Fire the request
        #
        res = requests.post(self.url + '/api/data?format=map', headers=self.hdrs,
                            data=json.dumps(req_json), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def post_event(self, name, description=None, severity=None, event_filter=None, tags=None):
        '''**Description**
            Send an event to Sysdig Monitor. The events you post are available in the Events tab in the Sysdig Monitor UI and can be overlied to charts.

        **Arguments**
            - **name**: the name of the new event.
            - **description**: a longer description offering detailed information about the event.
            - **severity**: syslog style from 0 (high) to 7 (low).
            - **event_filter**: metadata, in Sysdig Monitor format, of nodes to associate with the event, e.g. ``host.hostName = 'ip-10-1-1-1' and container.name = 'foo'``.
            - **tags**: a list of key-value dictionaries that can be used to tag the event. Can be used for filtering/segmenting purposes in Sysdig Monitor.

        **Success Return Value**
            A dictionary describing the new event.

        **Examples**
            - `examples/post_event_simple.py <https://github.com/draios/python-sdc-client/blob/master/examples/post_event_simple.py>`_
            - `examples/post_event.py <https://github.com/draios/python-sdc-client/blob/master/examples/post_event.py>`_
        '''
        edata = {
            'event': {
                'name': name
                }
            }

        if description is not None:
            edata['event']['description'] = description

        if severity is not None:
            edata['event']['severity'] = severity

        if event_filter is not None:
            edata['event']['filter'] = event_filter

        if tags is not None:
            edata['event']['tags'] = tags

        res = requests.post(self.url + '/api/events/', headers=self.hdrs, data=json.dumps(edata), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def get_events(self, name=None, from_ts=None, to_ts=None, tags=None):
        '''**Description**
            Returns the list of Sysdig Monitor events.

        **Arguments**
            - **name**: filter events by name.
            - **from_ts**: filter events by start time. Timestamp format is in UTC (seconds).
            - **to_ts**: filter events by end time. Timestamp format is in UTC (seconds).
            - **tags**: filter events by tags. Can be, for example ``tag1 = 'value1'``.

        **Success Return Value**
            A dictionary containing the list of events.

        **Example**
            `examples/list_events.py <https://github.com/draios/python-sdc-client/blob/master/examples/list_events.py>`_
        '''
        params = {}

        if name is not None:
            params['name'] = name

        if from_ts is not None:
            params['from'] = from_ts

        if to_ts is not None:
            params['to'] = to_ts

        if tags is not None:
            params['tags'] = tags

        res = requests.get(self.url + '/api/events/', headers=self.hdrs, params=params, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def delete_event(self, event):
        '''**Description**
            Deletes an event.

        **Arguments**
            - **event**: the event object as returned by :func:`~SdcClient.get_events`.

        **Success Return Value**
            `None`.

        **Example**
            `examples/delete_event.py <https://github.com/draios/python-sdc-client/blob/master/examples/delete_event.py>`_
        '''
        if 'id' not in event:
            return [False, "Invalid event format"]

        res = requests.delete(self.url + '/api/events/' + str(event['id']), headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, None]

    def get_data(self, metrics, start_ts, end_ts=0, sampling_s=0,
                 filter='', datasource_type='host', paging=None):
        '''**Description**
            Export metric data (both time-series and table-based).

        **Arguments**
            - **metrics**: a list of dictionaries, specifying the metrics and grouping keys that the query will return. A metric is any of the entries that can be found in the *Metrics* section of the Explore page in Sysdig Monitor. Metric entries require an *aggregations* section specifying how to aggregate the metric across time and containers/hosts. A grouping key is any of the entries that can be found in the *Show* or *Segment By* sections of the Explore page in Sysdig Monitor. These entries are used to apply single or hierarchical segmentation to the returned data and don't require the aggregations section. Refer to the Example link below for ready-to-use code snippets.
            - **start_ts**: the UTC time (in seconds) of the beginning of the data window. A negative value can be optionally used to indicate a relative time in the past from now. For example, -3600 means "one hour ago".
            - **end_ts**: the UTC time (in seconds) of the end of the data window, or 0 to indicate "now". A negative value can also be optionally used to indicate a relative time in the past from now. For example, -3600 means "one hour ago".
            - **sampling_s**: the duration of the samples that will be returned. 0 means that the whole data will be returned as a single sample.
            - **filter**: a boolean expression combining Sysdig Monitor segmentation criteria that defines what the query will be applied to. For example: *kubernetes.namespace.name='production' and container.image='nginx'*.
            - **datasource_type**: specify the metric source for the request, can be ``container`` or ``host``. Most metrics, for example ``cpu.used.percent`` or ``memory.bytes.used``, are reported by both hosts and containers. By default, host metrics are used, but if the request contains a container-specific grouping key in the metric list/filter (e.g. ``container.name``), then the container source is used. In cases where grouping keys are missing or apply to both hosts and containers (e.g. ``tag.Name``), *datasource_type* can be explicitly set to avoid any ambiguity and allow the user to select precisely what kind of data should be used for the request. `examples/get_data_datasource.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_data_datasource.py>`_ contains a few examples that should clarify the use of this argument.
            - **paging**:

        **Success Return Value**
            A dictionary with the requested data. Data is organized in a list of time samples, each of which includes a UTC timestamp and a list of values, whose content and order reflect what was specified in the *metrics* argument.

        **Examples**
            - `examples/get_data_simple.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_data_simple.py>`_
            - `examples/get_data_advanced.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_data_advanced.py>`_
            - `examples/list_hosts.py <https://github.com/draios/python-sdc-client/blob/master/examples/list_hosts.py>`_
            - `examples/get_data_datasource.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_data_datasource.py>`_
        '''
        reqbody = {
            'metrics': metrics,
            'dataSourceType': datasource_type,
        }

        if start_ts < 0:
            reqbody['last'] = -start_ts
        elif start_ts == 0:
            return [False, "start_ts cannot be 0"]
        else:
            reqbody['start'] = start_ts
            reqbody['end'] = end_ts

        if filter != '':
            reqbody['filter'] = filter

        if paging is not None:
            reqbody['paging'] = paging

        if sampling_s != 0:
            reqbody['sampling'] = sampling_s

        res = requests.post(self.url + '/api/data/', headers=self.hdrs, data=json.dumps(reqbody), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def get_sysdig_captures(self):
        '''**Description**
            Returns the list of sysdig captures for the user.

        **Success Return Value**
            A dictionary containing the list of captures.

        **Example**
            `examples/list_sysdig_captures.py <https://github.com/draios/python-sdc-client/blob/master/examples/list_sysdig_captures.py>`_
        '''
        res = requests.get(self.url + '/api/sysdig', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def poll_sysdig_capture(self, capture):
        '''**Description**
            Fetch the updated state of a sysdig capture. Can be used to poll the status of a capture that has been previously created and started with :func:`~SdcClient.create_sysdig_capture`.

        **Arguments**
            - **capture**: the capture object as returned by :func:`~SdcClient.get_sysdig_captures` or :func:`~SdcClient.create_sysdig_capture`.

        **Success Return Value**
            A dictionary showing the updated details of the capture. Use the ``status`` field to check the progress of a capture.

        **Example**
            `examples/create_sysdig_capture.py <https://github.com/draios/python-sdc-client/blob/master/examples/create_sysdig_capture.py>`_
        '''
        if 'id' not in capture:
            return [False, 'Invalid capture format']

        res = requests.get(self.url + '/api/sysdig/' + str(capture['id']), headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def create_sysdig_capture(self, hostname, capture_name, duration, capture_filter='', folder='/'):
        '''**Description**
            Create a new sysdig capture. The capture will be immediately started.

        **Arguments**
            - **hostname**: the hostname of the instrumented host where the capture will be taken.
            - **capture_name**: the name of the capture.
            - **duration**: the duration of the capture, in seconds.
            - **capture_filter**: a sysdig filter expression.
            - **folder**: directory in the S3 bucket where the capture will be saved.

        **Success Return Value**
            A dictionary showing the details of the new capture.

        **Example**
            `examples/create_sysdig_capture.py <https://github.com/draios/python-sdc-client/blob/master/examples/create_sysdig_capture.py>`_
        '''
        res = self.get_connected_agents()
        if not res[0]:
            return res

        capture_agent = None

        for agent in res[1]:
            if hostname == agent['hostName']:
                capture_agent = agent
                break

        if capture_agent is None:
            return [False, hostname + ' not found']

        data = {
            'agent': capture_agent,
            'name' : capture_name,
            'duration': duration,
            'folder': folder,
            'filters': capture_filter,
            'bucketName': ''
        }

        res = requests.post(self.url + '/api/sysdig', headers=self.hdrs, data=json.dumps(data), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def create_user_invite(self, user_email):
        '''**Description**
            Invites a new user to use Sysdig Monitor. This should result in an email notification to the specified address.

        **Arguments**
            - **user_email**: the email address of the user that will be invited to use Sysdig Monitor

        **Success Return Value**
            The newly created user.

        **Example**
            `examples/user_team_mgmt.py <https://github.com/draios/python-sdc-client/blob/master/examples/user_team_mgmt.py>`_
        '''
        # Look up the list of users to see if this exists, do not create if one exists
        res = requests.get(self.url + '/api/users', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        data = res.json()
        for user in data['users']:
            if user['username'] == user_email:
                return [False, 'user ' + user_email + ' already exists']

        # Create the user
        user_json = {'username' : user_email}
        res = requests.post(self.url + '/api/users', headers=self.hdrs, data=json.dumps(user_json), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def delete_user(self, user_email):
        '''**Description**
            Deletes a user from Sysdig Monitor.

        **Arguments**
            - **user_email**: the email address of the user that will be deleted from Sysdig Monitor

        **Example**
            `examples/user_team_mgmt.py <https://github.com/draios/python-sdc-client/blob/master/examples/user_team_mgmt.py>`_
        '''
        res = self.get_user_ids([user_email])
        if res[0] == False:
            return res
        userid = res[1][0]
        res = requests.delete(self.url + '/api/users' + str(userid), headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, None]

    def get_user(self, user_email):
        res = requests.get(self.url + '/api/users', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        for u in res.json()['users']:
            if u['username'] == user_email:
                return [True, u]
        return [False, 'User not found']

    def get_users(self):
        '''**Description**
            Return a list containing details about all users in the Sysdig Monitor environment. The API token must have Admin rights for this to succeed.

        **Success Return Value**
            A list user objects
        '''
        res = requests.get(self.url + '/api/users', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()['users']]

    def edit_user(self, user_email, firstName=None, lastName=None, roles=None, teams=None):
        res = self.get_user(user_email)
        if res[0] == False:
            return res
        user = res[1]
        reqbody = {
            'agentInstallParams': user['agentInstallParams'],
            'roles': roles if roles else user['roles'],
            'username': user_email,
            'version': user['version']
            }

        if teams == None:
            reqbody['teams'] = user['teams']
        else:
            t = self.get_team_ids(teams)
            if t[0] == False:
                return [False, 'Could not get team IDs']
            reqbody['teams'] = t[1]

        if firstName == None:
            reqbody['firstName'] = user['firstName'] if 'firstName' in user.keys() else ''
        else:
            reqbody['firstName'] = firstName

        if lastName == None:
            reqbody['lastName'] = user['lastName'] if 'lastName' in user.keys() else ''
        else:
            reqbody['lastName'] = lastName

        res = requests.put(self.url + '/api/users/' + str(user['id']), headers=self.hdrs, data=json.dumps(reqbody), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, 'Successfully edited user']

    def get_teams(self, team_filter=''):
        '''**Description**
            Return the set of teams that match the filter specified. The *team_filter* should be a substring of the names of the teams to be returned.

        **Arguments**
            - **team_filter**: the team filter to match when returning the list of teams

        **Success Return Value**
            The teams that match the filter.
        '''
        res = requests.get(self.url + '/api/teams', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        ret = filter(lambda t: team_filter in t['name'],res.json()['teams'])
        return [True, ret]

    def get_team(self, name):
        '''**Description**
            Return the team with the specified team name, if it is present.

        **Arguments**
            - **name**: the name of the team to return

        **Success Return Value**
            The requested team.

        **Example**
            `examples/user_team_mgmt.py <https://github.com/draios/python-sdc-client/blob/master/examples/user_team_mgmt.py>`_
        '''
        res = self.get_teams(name)
        if res[0] == False:
            return res
        for t in res[1]:
            if t['name'] == name:
                return [True, t]
        return [False, 'Could not find team']

    def get_team_ids(self, teams):
        res = requests.get(self.url + '/api/teams', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        u = filter(lambda x: x['name'] in teams, res.json()['teams'])
        return [True, map(lambda x: x['id'], u)]

    def get_user_ids(self, users):
        res = requests.get(self.url + '/api/users', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        u = filter(lambda x: x['username'] in users, res.json()['users'])
        return [True, map(lambda x: x['id'], u)]

    def create_team(self, name, users=[], filter='', description='', show='host', theme='#7BB0B2',
                    perm_capture=False, perm_custom_events=False, perm_aws_data=False):
        '''**Description**
            Creates a new team

        **Arguments**
            - **name**: the name of the team to create.
            - **users**: list of user names to add to the team.
            - **filter**: the scope that this team is able to access within Sysdig Monitor.
            - **description**: describes the team that will be created.
            - **show**: possible values are *host*, *container*.
            - **theme**: the color theme that Sysdig Monitor will use when displaying the team.
            - **perm_capture**: if True, this team will be allowed to take sysdig captures.
            - **perm_custom_events**: if True, this team will be allowed to view all custom events from every user and agent.
            - **perm_aws_data**: if True, this team will have access to all AWS metrics and tags, regardless of the team's scope.

        **Success Return Value**
            The newly created team.

        **Example**
            `examples/user_team_mgmt.py <https://github.com/draios/python-sdc-client/blob/master/examples/user_team_mgmt.py>`_
        '''
        reqbody = {
            'name': name,
            'description': description,
            'theme': theme,
            'show': show,
            'canUseSysdigCapture': perm_capture,
            'canUseCustomEvents': perm_custom_events,
            'canUseAwsMetrics': perm_aws_data,
        }

        # Map user-names to IDs
        if users != None and len(users) != 0:
            res = self.get_user_ids(users)
            if res[0] == False:
                return [False, 'Could not convert user names to IDs']
            reqbody['users'] = res[1]
        else:
            reqbody['users'] = []

        if filter != '':
            reqbody['filter'] = filter

        res = requests.post(self.url + '/api/teams', headers=self.hdrs, data=json.dumps(reqbody), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def edit_team(self, name, users=None, filter=None, description=None, show=None, theme=None,
                  perm_capture=None, perm_custom_events=None, perm_aws_data=None):
        '''**Description**
           Edits an existing team. All arguments are optional. Team settings for any arguments unspecified will remain at their current settings.

        **Arguments**
            - **name**: the name of the team to edit.
            - **users**: list of user names that should now be members of the team.
            - **filter**: the scope that this team is able to access within Sysdig Monitor.
            - **description**: describes the team that will be created.
            - **show**: possible values are *host*, *container*.
            - **theme**: the color theme that Sysdig Monitor will use when displaying the team.
            - **perm_capture**: if True, this team will be allowed to take sysdig captures.
            - **perm_custom_events**: if True, this team will be allowed to view all custom events from every user and agent.
            - **perm_aws_data**: if True, this team will have access to all AWS metrics and tags, regardless of the team's scope.

        **Success Return Value**
            The edited team.

        **Example**
            `examples/user_team_mgmt.py <https://github.com/draios/python-sdc-client/blob/master/examples/user_team_mgmt.py>`_
        '''
        res = self.get_team(name)
        if res[0] == False:
            return res

        t = res[1]
        reqbody = {
            'name': name,
            'description': description if description else t['description'],
            'theme': theme if theme else t['theme'],
            'show': show if show else t['show'],
            'canUseSysdigCapture': perm_capture if perm_capture else t['canUseSysdigCapture'],
            'canUseCustomEvents': perm_custom_events if perm_custom_events else t['canUseCustomEvents'],
            'canUseAwsMetrics': perm_aws_data if perm_aws_data else t['canUseAwsMetrics'],
            'id': t['id'],
            'version': t['version']
            }

        # Handling for users to map user-names to IDs
        if users != None:
            res = self.get_user_ids(users)
            if res[0] == False:
                return [False, 'Could not convert user names to IDs']
            reqbody['users'] = res[1]
        elif 'users' in t.keys():
            reqbody['users'] = t['users']
        else:
            reqbody['users'] = []

        # Special handling for filters since we don't support blank filters
        if filter != None:
            reqbody['filter'] = filter
        elif 'filter' in t.keys():
            reqbody['filter'] = t['filter']

        res = requests.put(self.url + '/api/teams/' + str(t['id']), headers=self.hdrs, data=json.dumps(reqbody), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def delete_team(self, name):
        '''**Description**
            Deletes a team from Sysdig Monitor.

        **Arguments**
            - **name**: the name of the team that will be deleted from Sysdig Monitor

        **Example**
            `examples/user_team_mgmt.py <https://github.com/draios/python-sdc-client/blob/master/examples/user_team_mgmt.py>`_
        '''
        res = self.get_team(name)
        if res[0] == False:
            return res

        t = res[1]
        res = requests.delete(self.url + '/api/teams/' + str(t['id']), headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, None]

    def switch_user_team(self, new_team_id):
        '''**Description**
            Switches the current user context to the specified team. In other words, this function makes it possible to start operating in the context of a different team without having to use the token of that team.

        **Arguments**
            - **new_team_id**: the numeric ID of the team (such as returned by :func:`~SdcClient.get_team_ids`) to switch to.
        '''
        res = self.get_user_info()
        if not res[0]:
            return res

        myuinfo = res[1]['user']
        myuinfo['currentTeam'] = new_team_id
        uid = myuinfo['id']

        res = requests.put(self.url + '/api/user/' + str(uid), headers=self.hdrs, data=json.dumps(myuinfo), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        else:
            return [True, None]

    def get_agents_config(self):
        res = requests.get(self.url + '/api/agents/config', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        data = res.json()
        return [True, data]

    def set_agents_config(self, config):
        res = requests.put(self.url + '/api/agents/config', headers=self.hdrs, data=json.dumps(config), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def clear_agents_config(self):
        data = {'files' : []}
        self.set_agents_config(data)

    def get_user_api_token(self, username, teamname):
        res = self.get_team(teamname)
        if res[0] == False:
            return res

        t = res[1]

        res = requests.get(self.url + '/api/token/%s/%d' % (username, t['id']), headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        data = res.json()
        return [True, data['token']['key']]

class SdMonitorClient(_SdcCommon):

    def __init__(self, token="", sdc_url='https://app.sysdigcloud.com', ssl_verify=True):
        super(SdMonitorClient, self).__init__(token, sdc_url, ssl_verify)

    def get_alerts(self):
        '''**Description**
            Retrieve the list of alerts configured by the user.

        **Success Return Value**
            An array of alert dictionaries, with the format described at `this link <https://app.sysdigcloud.com/apidocs/#!/Alerts/get_api_alerts>`__

        **Example**
            `examples/list_alerts.py <https://github.com/draios/python-sdc-client/blob/master/examples/list_alerts.py>`_
        '''
        res = requests.get(self.url + '/api/alerts', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def get_notifications(self, from_ts, to_ts, state=None, resolved=None):
        '''**Description**
            Returns the list of Sysdig Monitor alert notifications.

        **Arguments**
            - **from_ts**: filter events by start time. Timestamp format is in UTC (seconds).
            - **to_ts**: filter events by start time. Timestamp format is in UTC (seconds).
            - **state**: filter events by alert state. Supported values are ``OK`` and ``ACTIVE``.
            - **resolved**: filter events by resolution status. Supported values are ``True`` and ``False``.

        **Success Return Value**
            A dictionary containing the list of notifications.

        **Example**
            `examples/list_alert_notifications.py <https://github.com/draios/python-sdc-client/blob/master/examples/list_alert_notifications.py>`_
        '''
        params = {}

        if from_ts is not None:
            params['from'] = from_ts * 1000000

        if to_ts is not None:
            params['to'] = to_ts * 1000000

        if state is not None:
            params['state'] = state

        if resolved is not None:
            params['resolved'] = resolved

        res = requests.get(self.url + '/api/notifications', headers=self.hdrs, params=params, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def update_notification_resolution(self, notification, resolved):
        '''**Description**
            Updates the resolution status of an alert notification.

        **Arguments**
            - **notification**: notification object as returned by :func:`~SdcClient.get_notifications`.
            - **resolved**: new resolution status. Supported values are ``True`` and ``False``.

        **Success Return Value**
            The updated notification.

        **Example**
            `examples/resolve_alert_notifications.py <https://github.com/draios/python-sdc-client/blob/master/examples/resolve_alert_notifications.py>`_
        '''
        if 'id' not in notification:
            return [False, 'Invalid notification format']

        notification['resolved'] = resolved
        data = {'notification': notification}

        res = requests.put(self.url + '/api/notifications/' + str(notification['id']), headers=self.hdrs, data=json.dumps(data), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def create_alert(self, name=None, description=None, severity=None, for_atleast_s=None, condition=None,
                     segmentby=[], segment_condition='ANY', user_filter='', notify=None, enabled=True,
                     annotations={}, alert_obj=None):
        '''**Description**
            Create a threshold-based alert.

        **Arguments**
            - **name**: the alert name. This will appear in the Sysdig Monitor UI and in notification emails.
            - **description**: the alert description. This will appear in the Sysdig Monitor UI and in notification emails.
            - **severity**: syslog-encoded alert severity. This is a number from 0 to 7 where 0 means 'emergency' and 7 is 'debug'.
            - **for_atleast_s**: the number of consecutive seconds the condition must be satisfied for the alert to fire.
            - **condition**: the alert condition, as described here https://app.sysdigcloud.com/apidocs/#!/Alerts/post_api_alerts
            - **segmentby**: a list of Sysdig Monitor segmentation criteria that can be used to apply the alert to multiple entities. For example, segmenting a CPU alert by ['host.mac', 'proc.name'] allows to apply it to any process in any machine.
            - **segment_condition**: When *segmentby* is specified (and therefore the alert will cover multiple entities) this field is used to determine when it will fire. In particular, you have two options for *segment_condition*: **ANY** (the alert will fire when at least one of the monitored entities satisfies the condition) and **ALL** (the alert will fire when all of the monitored entities satisfy the condition).
            - **user_filter**: a boolean expression combining Sysdig Monitor segmentation criteria that makes it possible to reduce the scope of the alert. For example: *kubernetes.namespace.name='production' and container.image='nginx'*.
            - **notify**: the type of notification you want this alert to generate. Options are *EMAIL*, *SNS*, *PAGER_DUTY*, *SYSDIG_DUMP*.
            - **enabled**: if True, the alert will be enabled when created.
            - **annotations**: an optional dictionary of custom properties that you can associate to this alert for automation or management reasons
            - **alert_obj**: an optional fully-formed Alert object of the format returned in an "alerts" list by :func:`~SdcClient.get_alerts` This is an alternative to creating the Alert using the individual parameters listed above.

        **Success Return Value**
            A dictionary describing the just created alert, with the format described at `this link <https://app.sysdigcloud.com/apidocs/#!/Alerts/post_api_alerts>`__

        **Example**
            `examples/create_alert.py <https://github.com/draios/python-sdc-client/blob/master/examples/create_alert.py>`_
        '''
        #
        # Get the list of alerts from the server
        #
        res = requests.get(self.url + '/api/alerts', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        j = res.json()

        if alert_obj is None:
            if None in (name, description, severity, for_atleast_s, condition):
                return [False, 'Must specify a full Alert object or all parameters: name, description, severity, for_atleast_s, condition']
            else:
                #
                # Populate the alert information
                #
                alert_json = {
                    'alert' : {
                        'type' : 'MANUAL',
                        'name' : name,
                        'description' : description,
                        'enabled' : enabled,
                        'severity' : severity,
                        'timespan' : for_atleast_s * 1000000,
                        'condition' : condition,
                        'filter': user_filter
                    }
                }

                if segmentby != None and segmentby != []:
                    alert_json['alert']['segmentBy'] = segmentby
                    alert_json['alert']['segmentCondition'] = {'type' : segment_condition}

                if annotations != None and annotations != {}:
                    alert_json['alert']['annotations'] = annotations

                if notify != None:
                    alert_json['alert']['notificationChannelIds'] = notify
        else:
            # The REST API enforces "Alert ID and version must be null", so remove them if present,
            # since these would have been there in a dump from the list_alerts.py example.
            alert_obj.pop('id', None)
            alert_obj.pop('version', None)
            alert_json = {
                'alert' : alert_obj
            }

        #
        # Create the new alert
        #
        res = requests.post(self.url + '/api/alerts', headers=self.hdrs, data=json.dumps(alert_json), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def update_alert(self, alert):
        '''**Description**
            Update a modified threshold-based alert.

        **Arguments**
            - **alert**: one modified alert object of the same format as those in the list returned by :func:`~SdcClient.get_alerts`.

        **Success Return Value**
            The updated alert.

        **Example**
            `examples/update_alert.py <https://github.com/draios/python-sdc-client/blob/master/examples/update_alert.py>`_
        '''
        if 'id' not in alert:
            return [False, "Invalid alert format"]

        res = requests.put(self.url + '/api/alerts/' + str(alert['id']), headers=self.hdrs, data=json.dumps({ "alert": alert}), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def delete_alert(self, alert):
        '''**Description**
            Deletes an alert.

        **Arguments**
            - **alert**: the alert dictionary as returned by :func:`~SdcClient.get_alerts`.

        **Success Return Value**
            ``None``.

        **Example**
            `examples/delete_alert.py <https://github.com/draios/python-sdc-client/blob/master/examples/delete_alert.py>`_
        '''
        if 'id' not in alert:
            return [False, 'Invalid alert format']

        res = requests.delete(self.url + '/api/alerts/' + str(alert['id']), headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, None]

    def get_explore_grouping_hierarchy(self):
        '''**Description**
            Return the user's current grouping hierarchy as visible in the Explore tab of Sysdig Monitor.

        **Success Return Value**
            A list containing the list of the user's Explore grouping criteria.

        **Example**
            `examples/print_explore_grouping.py <https://github.com/draios/python-sdc-client/blob/master/examples/print_explore_grouping.py>`_
        '''
        res = requests.get(self.url + '/api/groupConfigurations', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        data = res.json()

        if 'groupConfigurations' not in data:
            return [False, 'corrupted groupConfigurations API response']

        gconfs = data['groupConfigurations']

        for gconf in gconfs:
            if gconf['id'] == 'explore':
                res = []
                items = gconf['groups'][0]['groupBy']

                for item in items:
                    res.append(item['metric'])

                return [True, res]

        return [False, 'corrupted groupConfigurations API response, missing "explore" entry']

    def set_explore_grouping_hierarchy(self, new_hierarchy):
        '''**Description**
            Changes the grouping hierarchy in the Explore panel of the current user.

        **Arguments**
            - **new_hierarchy**: a list of sysdig segmentation metrics indicating the new grouping hierarchy.
        '''
        body = {
            'id': 'explore',
            'groups': [{'groupBy':[]}]
        }

        for item in new_hierarchy:
            body['groups'][0]['groupBy'].append({'metric': item})

        res = requests.put(self.url + '/api/groupConfigurations/explore', headers=self.hdrs,
                            data=json.dumps(body), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        else:
            return [True, None]

    def get_views_list(self):
        res = requests.get(self.url + '/data/drilldownDashboardDescriptors.json', headers=self.hdrs,
                           verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def get_view(self, name):
        gvres = self.get_views_list()
        if gvres[0] is False:
            return gvres

        vlist = gvres[1]['drilldownDashboardDescriptors']

        id = None

        for v in vlist:
            if v['name'] == name:
                id = v['id']
                break

        if not id:
            return [False, 'view ' + name + ' not found']

        res = requests.get(self.url + '/data/drilldownDashboards/' + id + '.json', headers=self.hdrs,
                           verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def get_dashboards(self):
        '''**Description**
            Return the list of dashboards available under the given user account. This includes the dashboards created by the user and the ones shared with her by other users.

        **Success Return Value**
            A dictionary containing the list of available sampling intervals.

        **Example**
            `examples/list_dashboards.py <https://github.com/draios/python-sdc-client/blob/master/examples/list_dashboards.py>`_
        '''
        res = requests.get(self.url + '/ui/dashboards', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def find_dashboard_by(self, name=None):
        '''**Description**
            Finds dashboards with the specified name. You can then delete the dashboard (with :func:`~SdcClient.delete_dashboard`) or edit panels (with :func:`~SdcClient.add_dashboard_panel` and :func:`~SdcClient.remove_dashboard_panel`)

        **Arguments**
            - **name**: the name of the dashboards to find.

        **Success Return Value**
            A list of dictionaries of dashboards matching the specified name.

        **Example**
            `examples/dashboard.py <https://github.com/draios/python-sdc-client/blob/master/examples/dashboard.py>`_
        '''
        res = self.get_dashboards()
        if res[0] is False:
            return res
        else:
            def filter_fn(configuration):
                return configuration['name'] == name
            def create_item(configuration):
                return {'dashboard': configuration}

            dashboards = map(create_item, filter(filter_fn, res[1]['dashboards']))
            return [True, dashboards]

    def create_dashboard_with_configuration(self, configuration):
        res = requests.post(self.url + '/ui/dashboards', headers=self.hdrs, data=json.dumps({'dashboard': configuration}),
                            verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        else:
            return [True, res.json()]

    def create_dashboard(self, name):
        '''
        **Description**
            Creates an empty dashboard. You can then add panels by using ``add_dashboard_panel``.

        **Arguments**
            - **name**: the name of the dashboard that will be created.

        **Success Return Value**
            A dictionary showing the details of the new dashboard.

        **Example**
            `examples/dashboard.py <https://github.com/draios/python-sdc-client/blob/master/examples/dashboard.py>`_
        '''
        dashboard_configuration = {
            'name':   name,
            'schema': 1,
            'items':  []
        }

        #
        # Create the new dashboard
        #
        res = requests.post(self.url + '/ui/dashboards', headers=self.hdrs, data=json.dumps({'dashboard': dashboard_configuration}),
                            verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        else:
            return [True, res.json()]

    def add_dashboard_panel(self, dashboard, name, panel_type, metrics, scope=None, sort_by=None, limit=None, layout=None):
        """**Description**
            Adds a panel to the dashboard. A panel can be a time series, or a top chart (i.e. bar chart), or a number panel.

        **Arguments**
            - **dashboard**: dashboard to edit
            - **name**: name of the new panel
            - **panel_type**: type of the new panel. Valid values are: ``timeSeries``, ``top``, ``number``
            - **metrics**:  a list of dictionaries, specifying the metrics to show in the panel, and optionally, if there is only one metric, a grouping key to segment that metric by. A metric is any of the entries that can be found in the *Metrics* section of the Explore page in Sysdig Monitor. Metric entries require an *aggregations* section specifying how to aggregate the metric across time and groups of containers/hosts. A grouping key is any of the entries that can be found in the *Show* or *Segment By* sections of the Explore page in Sysdig Monitor. Refer to the examples section below for ready to use code snippets. Note, certain panels allow certain combinations of metrics and grouping keys:
                - ``timeSeries``: 1 or more metrics OR 1 metric + 1 grouping key
                - ``top``: 1 or more metrics OR 1 metric + 1 grouping key
                - ``number``: 1 metric only
            - **scope**: filter to apply to the panel; must be based on metadata available in Sysdig Monitor; Example: *kubernetes.namespace.name='production' and container.image='nginx'*.
            - **sort_by**: Data sorting; The parameter is optional and it's a dictionary of ``metric`` and ``mode`` (it can be ``desc`` or ``asc``)
            - **limit**: This parameter sets the limit on the number of lines/bars shown in a ``timeSeries`` or ``top`` panel. In the case of more entities being available than the limit, the top entities according to the sort will be shown. The default value is 10 for ``top`` panels (for ``timeSeries`` the default is defined by Sysdig Monitor itself). Note that increasing the limit above 10 is not officially supported and may cause performance and rendering issues
            - **layout**: Size and position of the panel. The dashboard layout is defined by a grid of 12 columns, each row height is equal to the column height. For example, say you want to show 2 panels at the top: one panel might be 6 x 3 (half the width, 3 rows height) located in row 1 and column 1 (top-left corner of the viewport), the second panel might be 6 x 3 located in row 1 and position 7. The location is specified by a dictionary of ``row`` (row position), ``col`` (column position), ``size_x`` (width), ``size_y`` (height).

        **Success Return Value**
            A dictionary showing the details of the edited dashboard.

        **Example**
            `examples/dashboard.py <https://github.com/draios/python-sdc-client/blob/master/examples/dashboard.py>`_
        """
        panel_configuration = {
            'name':                 name,
            'showAs':               None,
            'showAsType':           None,
            'metrics':              [],
            'gridConfiguration':    {
                'col':      1,
                'row':      1,
                'size_x':   12,
                'size_y':   6
            }
        }

        if panel_type == 'timeSeries':
            #
            # In case of a time series, the current dashboard implementation
            # requires the timestamp to be explicitly specified as "key".
            # However, this function uses the same abstraction of the data API
            # that doesn't require to specify a timestamp key (you only need to
            # specify time window and sampling)
            #
            metrics = copy.copy(metrics)
            metrics.insert(0, {'id': 'timestamp'})

        #
        # Convert list of metrics to format used by Sysdig Monitor
        #
        property_names = {}
        k_count = 0
        v_count = 0
        for i, metric in enumerate(metrics):
            property_name = 'v' if 'aggregations' in metric else 'k'

            if property_name == 'k':
                i = k_count
                k_count += 1
            else:
                i = v_count
                v_count += 1
            property_names[metric['id']] = property_name + str(i)

            panel_configuration['metrics'].append({
                'metricId':         metric['id'],
                'aggregation':      metric['aggregations']['time'] if 'aggregations' in metric else None,
                'groupAggregation': metric['aggregations']['group'] if 'aggregations' in metric else None,
                'propertyName':     property_name + str(i)
            })
        #
        # Convert scope to format used by Sysdig Monitor
        #
        if scope != None:
            filter_expressions = scope.strip(' \t\n\r?!.').split(" and ")
            filters = []

            for filter_expression in filter_expressions:
                values = filter_expression.strip(' \t\n\r?!.').split("=")
                if len(values) != 2:
                    return [False, "invalid scope format"]
                filters.append({
                    'metric':   values[0].strip(' \t\n\r?!.'),
                    'op':       '=',
                    'value':    values[1].strip(' \t\n\r"?!.'),
                    'filters':  None
                })

            if len(filters) > 0:
                panel_configuration['filter'] = {
                    'filters': {
                        'logic':    'and',
                        'filters':  filters
                    }
                }

        #
        # Configure panel type
        #
        if panel_type == 'timeSeries':
            panel_configuration['showAs'] = 'timeSeries'
            panel_configuration['showAsType'] = 'line'

            if limit != None:
                panel_configuration['paging'] = {
                    'from': 0,
                    'to':   limit - 1
                }

        elif panel_type == 'number':
            panel_configuration['showAs'] = 'summary'
            panel_configuration['showAsType'] = 'summary'
        elif panel_type == 'top':
            panel_configuration['showAs'] = 'top'
            panel_configuration['showAsType'] = 'bars'

            if sort_by is None:
                panel_configuration['sorting'] = [{
                    'id':   'v0',
                    'mode': 'desc'
                }]
            else:
                panel_configuration['sorting'] = [{
                    'id':   property_names[sort_by['metric']],
                    'mode': sort_by['mode']
                }]

            if limit is None:
                panel_configuration['paging'] = {
                    'from': 0,
                    'to':   10
                }
            else:
                panel_configuration['paging'] = {
                    'from': 0,
                    'to':   limit - 1
                }


        #
        # Configure layout
        #
        if layout != None:
            panel_configuration['gridConfiguration'] = layout

        #
        # Clone existing dashboard...
        #
        dashboard_configuration = copy.deepcopy(dashboard)
        dashboard_configuration['id'] = None

        #
        # ... and add the new panel
        #
        dashboard_configuration['items'].append(panel_configuration)

        #
        # Update dashboard
        #
        res = requests.put(self.url + '/ui/dashboards/' + str(dashboard['id']), headers=self.hdrs, data=json.dumps({'dashboard': dashboard_configuration}),
                           verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        else:
            return [True, res.json()]

    def remove_dashboard_panel(self, dashboard, panel_name):
        '''**Description**
            Removes a panel from the dashboard. The panel to remove is identified by the specified ``name``.

        **Arguments**
            - **name**: name of the panel to find and remove

        **Success Return Value**
            A dictionary showing the details of the edited dashboard.

        **Example**
            `examples/dashboard.py <https://github.com/draios/python-sdc-client/blob/master/examples/dashboard.py>`_
        '''
        #
        # Clone existing dashboard...
        #
        dashboard_configuration = copy.deepcopy(dashboard)
        dashboard_configuration['id'] = None

        #
        # ... find the panel
        #
        def filter_fn(panel):
            return panel['name'] == panel_name
        panels = filter(filter_fn, dashboard_configuration['items'])

        if len(panels) > 0:
            #
            # ... and remove it
            #
            for panel in panels:
                dashboard_configuration['items'].remove(panel)

            #
            # Update dashboard
            #
            res = requests.put(self.url + '/ui/dashboards/' + str(dashboard['id']), headers=self.hdrs, data=json.dumps({'dashboard': dashboard_configuration}),
                               verify=self.ssl_verify)
            if not self._checkResponse(res):
                return [False, self.lasterr]
            else:
                return [True, res.json()]
        else:
            return [False, 'Not found']

    def create_dashboard_from_template(self, newdashname, template, scope=[], shared=False, annotations={}):
        if scope is None:
            scope = []

        if type(scope) is str:
            checks = scope.strip(' \t\n\r?!.').split(" and ")
            scope = []

            for c in checks:
                elements = c.strip(' \t\n\r?!.').split("=")
                if len(elements) != 2:
                    return [False, "invalid scope format"]
                scope.append({elements[0].strip(' \t\n\r?!.'): elements[1].strip(' \t\n\r?!.')})
        else:
            if not(type(scope) is list):
                return [False, "invalid scope format"]

        #
        # Create the unique ID for this dashboard
        #
        baseconfid = newdashname
        for sentry in scope:
            baseconfid = baseconfid + str(sentry.keys()[0])
            baseconfid = baseconfid + str(sentry.values()[0])

        #
        # Clean up the dashboard we retireved so it's ready to be pushed
        #
        template['id'] = None
        template['version'] = None
        template['schema'] = 1
        template['name'] = newdashname
        template['isShared'] = shared # make sure the dashboard is not shared

        #
        # Assign the filter and the group ID to each view to point to this service
        #
        filters = []
        gby = []
        for sentry in scope:
            filters.append({'metric' : sentry.keys()[0], 'op' : '=', 'value' : sentry.values()[0],
                            'filters' : None})
            gby.append({'metric': sentry.keys()[0]})

        filter = {
            'filters' :
            {
                'logic' : 'and',
                'filters' : filters
            }
        }

        #
        # create the grouping configurations for each chart
        #
        j = 0
        if 'items' in template:
            for chart in template['items']:
                if len(scope) != 0:
                    j = j + 1

                    confid = baseconfid + str(j)

                    gconf = {'id': confid,
                             'groups': [
                                 {
                                     'groupBy': gby
                                 }
                             ]
                            }

                    res = requests.post(self.url + '/api/groupConfigurations', headers=self.hdrs,
                                        data=json.dumps(gconf), verify=self.ssl_verify)
                    if not self._checkResponse(res):
                        return [False, self.lasterr]

                    chart['filter'] = filter
                    chart['groupId'] = confid
                else:
                    chart['filter'] = None
                    chart['groupId'] = None

        if 'annotations' in template:
            template['annotations'].update(annotations)
        else:
            template['annotations'] = annotations

        template['annotations']['createdByEngine'] = True

        ddboard = {'dashboard': template}

        #
        # Create the new dashboard
        #
        res = requests.post(self.url + '/ui/dashboards', headers=self.hdrs, data=json.dumps(ddboard), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        else:
            return [True, res.json()]

    def create_dashboard_from_view(self, newdashname, viewname, filter, shared=False, annotations={}):
        '''**Description**
            Create a new dasboard using one of the Sysdig Monitor views as a template. You will be able to define the scope of the new dashboard.

        **Arguments**
            - **newdashname**: the name of the dashboard that will be created.
            - **viewname**: the name of the view to use as the template for the new dashboard. This corresponds to the name that the view has in the Explore page.
            - **filter**: a boolean expression combining Sysdig Monitor segmentation criteria that defines what the new dasboard will be applied to. For example: *kubernetes.namespace.name='production' and container.image='nginx'*.
            - **shared**: if set to True, the new dashboard will be a shared one.
            - **annotations**: an optional dictionary of custom properties that you can associate to this dashboard for automation or management reasons

        **Success Return Value**
            A dictionary showing the details of the new dashboard.

        **Example**
            `examples/create_dashboard.py <https://github.com/draios/python-sdc-client/blob/master/examples/create_dashboard.py>`_
        '''
        #
        # Find our template view
        #
        gvres = self.get_view(viewname)
        if gvres[0] is False:
            return gvres

        view = gvres[1]['drilldownDashboard']

        view['timeMode'] = {'mode' : 1}
        view['time'] = {'last' : 2 * 60 * 60 * 1000000, 'sampling' : 2 * 60 * 60 * 1000000}

        #
        # Create the new dashboard
        #
        return self.create_dashboard_from_template(newdashname, view, filter, shared, annotations)

    def create_dashboard_from_dashboard(self, newdashname, templatename, filter, shared=False, annotations={}):
        '''**Description**
            Create a new dasboard using one of the existing dashboards as a template. You will be able to define the scope of the new dasboard.

        **Arguments**
            - **newdashname**: the name of the dashboard that will be created.
            - **viewname**: the name of the dasboard to use as the template, as it appears in the Sysdig Monitor dashboard page.
            - **filter**: a boolean expression combining Sysdig Monitor segmentation criteria defines what the new dasboard will be applied to. For example: *kubernetes.namespace.name='production' and container.image='nginx'*.
            - **shared**: if set to True, the new dashboard will be a shared one.
            - **annotations**: an optional dictionary of custom properties that you can associate to this dashboard for automation or management reasons

        **Success Return Value**
            A dictionary showing the details of the new dashboard.

        **Example**
            `examples/create_dashboard.py <https://github.com/draios/python-sdc-client/blob/master/examples/create_dashboard.py>`_
        '''
        #
        # Get the list of dashboards from the server
        #
        res = requests.get(self.url + '/ui/dashboards', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        j = res.json()

        #
        # Find our template dashboard
        #
        dboard = None

        for db in j['dashboards']:
            if db['name'] == templatename:
                dboard = db
                break

        if dboard is None:
            self.lasterr = 'can\'t find dashboard ' + templatename + ' to use as a template'
            return [False, self.lasterr]

        #
        # Create the dashboard
        #
        return self.create_dashboard_from_template(newdashname, dboard, filter, shared, annotations)

    def create_dashboard_from_file(self, newdashname, filename, filter, shared=False, annotations={}):
        '''
        **Description**
            Create a new dasboard using a dashboard template saved to disk.

        **Arguments**
            - **newdashname**: the name of the dashboard that will be created.
            - **filename**: name of a file containing a JSON object for a dashboard in the format of an array element returned by :func:`~SdcClient.get_dashboards`
            - **filter**: a boolean expression combining Sysdig Monitor segmentation criteria defines what the new dasboard will be applied to. For example: *kubernetes.namespace.name='production' and container.image='nginx'*.
            - **shared**: if set to True, the new dashboard will be a shared one.
            - **annotations**: an optional dictionary of custom properties that you can associate to this dashboard for automation or management reasons

        **Success Return Value**
            A dictionary showing the details of the new dashboard.

        **Example**
            `examples/dashboard_save_load.py <https://github.com/draios/python-sdc-client/blob/master/examples/dashboard_save_load.py>`_
        '''
        #
        # Load the Dashboard
        #
        with open(filename) as data_file:
            dboard = json.load(data_file)

        dboard['timeMode'] = {'mode' : 1}
        dboard['time'] = {'last' : 2 * 60 * 60 * 1000000, 'sampling' : 2 * 60 * 60 * 1000000}

        #
        # Create the new dashboard
        #
        return self.create_dashboard_from_template(newdashname, dboard, filter, shared, annotations)

    def delete_dashboard(self, dashboard):
        '''**Description**
            Deletes a dashboard.

        **Arguments**
            - **dashboard**: the dashboard object as returned by :func:`~SdcClient.get_dashboards`.

        **Success Return Value**
            `None`.

        **Example**
            `examples/delete_dashboard.py <https://github.com/draios/python-sdc-client/blob/master/examples/delete_dashboard.py>`_
        '''
        if 'id' not in dashboard:
            return [False, "Invalid dashboard format"]

        res = requests.delete(self.url + '/ui/dashboards/' + str(dashboard['id']), headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, None]

    def get_metrics(self):
        '''**Description**
            Return the metric list that can be used for data requests/alerts/dashboards.

        **Success Return Value**
            A dictionary containing the list of available metrics.

        **Example**
            `examples/list_metrics.py <https://github.com/draios/python-sdc-client/blob/master/examples/list_metrics.py>`_
        '''
        res = requests.get(self.url + '/api/data/metrics', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def get_falco_rules(self):
        res = requests.get(self.url + '/api/agents/falco_rules', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        data = res.json()
        return [True, data]

    def set_falco_rules_content_raw(self, raw_payload):
        res = requests.put(self.url + '/api/agents/falco_rules', headers=self.hdrs, data=json.dumps(raw_payload), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def set_falco_rules_content(self, filter, rules_content):
        payload = { "files" : [ { "filter": filter, "content": rules_content} ] }
        return self.set_falco_rules_content_raw(payload)

    def set_falco_rules_filename(self, filter, rules_filename):
        with open(rules_filename, 'r') as f:
            rules_content = f.read()
            return self.set_falco_rules_content(filter, rules_content)

    def clear_falco_rules(self):
        data = {'files' : []}
        return self.set_falco_rules_content_raw(data)


# For backwards compatibility
SdcClient = SdMonitorClient

class SdSecureClient(_SdcCommon):

    def __init__(self, token="", sdc_url='https://app.sysdigcloud.com', ssl_verify=True):
        super(SdSecureClient, self).__init__(token, sdc_url, ssl_verify)

        self.customer_id = None

    def _get_falco_rules(self, kind):
        res = requests.get(self.url + '/api/settings/falco/{}RulesFile'.format(kind), headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        data = res.json()
        return [True, data]

    def get_system_falco_rules(self):
        '''**Description**
            Get the system falco rules file in use for this customer. See the `Falco wiki <https://github.com/draios/falco/wiki/Falco-Rules>`_ for documentation on the falco rules format.

        **Arguments**
            - None

        **Success Return Value**
            The contents of the system falco rules file.

        **Example**
            `examples/get_secure_system_falco_rules.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_secure_system_falco_rules.py>`_
        '''

        return self._get_falco_rules("system")

    def get_user_falco_rules(self):
        '''**Description**
            Get the user falco rules file in use for this customer. See the `Falco wiki <https://github.com/draios/falco/wiki/Falco-Rules>`_ for documentation on the falco rules format.

        **Arguments**
            - None

        **Success Return Value**
            The contents of the user falco rules file.

        **Example**
            `examples/get_secure_user_falco_rules.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_secure_user_falco_rules.py>`_
        '''
        return self._get_falco_rules("user")

    def _set_falco_rules(self, kind, rules_content):
        payload = self._get_falco_rules(kind)

        if not payload[0]:
            return payload

        payload[1]["{}RulesFile".format(kind)]["content"] = rules_content # pylint: disable=unsubscriptable-object

        res = requests.put(self.url + '/api/settings/falco/{}RulesFile'.format(kind), headers=self.hdrs, data=json.dumps(payload[1]), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def set_system_falco_rules(self, rules_content):
        '''**Description**
            Set the system falco rules file in use for this customer. NOTE: This API endpoint can *only* be used in on-premise deployments. Generally the system falco rules file is only modified in conjunction with Sysdig support. See the `Falco wiki <https://github.com/draios/falco/wiki/Falco-Rules>`_ for documentation on the falco rules format.

        **Arguments**
            - A string containing the system falco rules.

        **Success Return Value**
            The contents of the system falco rules file that were just updated.

        **Example**
            `examples/set_secure_system_falco_rules.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_secure_system_falco_rules.py>`_

        '''
        return self._set_falco_rules("system", rules_content)

    def set_user_falco_rules(self, rules_content):
        '''**Description**
            Set the user falco rules file in use for this customer. See the `Falco wiki <https://github.com/draios/falco/wiki/Falco-Rules>`_ for documentation on the falco rules format.

        **Arguments**
            - A string containing the user falco rules.

        **Success Return Value**
            The contents of the user falco rules file that were just updated.

        **Example**
            `examples/set_secure_user_falco_rules.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_secure_user_falco_rules.py>`_

        '''
        return self._set_falco_rules("user", rules_content)

    def _get_policy_events_int(self, ctx):
        res = requests.get(self.url + '/api/policyEvents?from={:d}&to={:d}&offset={}&limit={}'.format(int(ctx['from']), int(ctx['to']), ctx['offset'], ctx['limit']), headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        # Increment the offset by limit
        ctx['offset'] += ctx['limit']

        return [True, {"ctx": ctx, "data": res.json()}]

    def get_policy_events_range(self, from_sec, to_sec):
        '''**Description**
            Fetch all policy events that occurred in the time range [from_sec:to_sec]. This method is used in conjunction
            with :func:`~sdcclient.SdSecureClient.get_more_policy_events` to provide paginated access to policy events.

        **Arguments**
            - from_sec: the start of the timerange for which to get events
            - end_sec: the end of the timerange for which to get events

        **Success Return Value**
            An array containing:
              - A context object that should be passed to later calls to get_more_policy_events.
              - An array of policy events, in JSON format. See :func:`~sdcclient.SdSecureClient.get_more_policy_events`
                for details on the contents of policy events.

        **Example**
            `examples/get_secure_policy_events.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_secure_policy_events.py>`_

        '''
        ctx = {"from": int(from_sec) * 1000000,
               "to": int(to_sec) * 1000000,
               "offset": 0,
               "limit": 1000}

        return self._get_policy_events_int(ctx)

    def get_policy_events_duration(self, duration_sec):
        '''**Description**
            Fetch all policy events that occurred in the last duration_sec seconds. This method is used in conjunction with
            :func:`~sdcclient.SdSecureClient.get_more_policy_events` to provide paginated access to policy events.

        **Arguments**
            - duration_sec: Fetch all policy events that have occurred in the last *duration_sec* seconds.

        **Success Return Value**
            An array containing:
              - A context object that should be passed to later calls to get_more_policy_events.
              - An array of policy events, in JSON format. See :func:`~sdcclient.SdSecureClient.get_more_policy_events`
                for details on the contents of policy events.

        **Example**
            `examples/get_secure_policy_events.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_secure_policy_events.py>`_

        '''
        epoch = datetime.datetime.utcfromtimestamp(0)

        to_ts = (datetime.datetime.utcnow()-epoch).total_seconds() * 1000 * 1000
        from_ts = to_ts - (int(duration_sec) * 1000 * 1000)
        ctx = {"to": to_ts,
               "from": from_ts,
               "offset": 0,
               "limit": 1000}

        return self._get_policy_events_int(ctx)

    def get_more_policy_events(self, ctx):
        '''**Description**
            Fetch additional policy events after an initial call to :func:`~sdcclient.SdSecureClient.get_policy_events_range` /
            :func:`~sdcclient.SdSecureClient.get_policy_events_duration` or a prior call to get_more_policy_events.

        **Arguments**
            - ctx: a context object returned from an initial call to :func:`~sdcclient.SdSecureClient.get_policy_events_range` /
              :func:`~sdcclient.SdSecureClient.get_policy_events_duration` or a prior call to get_more_policy_events.

        **Success Return Value**
            An array containing:
              - A context object that should be passed to later calls to get_more_policy_events()
              - An array of policy events, in JSON format. Each policy event contains the following:
                 - hostMac: the mac address of the machine where the event occurred
                 - severity: a severity level from 1-7
                 - timestamp: when the event occurred (ns since the epoch)
                 - version: a version number for this message (currently 1)
                 - policyId: a reference to the policy that generated this policy event
                 - output: A string describing the event that occurred
                 - id: a unique identifier for this policy event
                 - isAggregated: if true, this is a combination of multiple policy events
                 - containerId: the container in which the policy event occurred

            When the number of policy events returned is 0, there are no remaining events and you can stop calling get_more_policy_events().

        **Example**
            `examples/get_secure_policy_events.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_secure_policy_events.py>`_
        '''
        return self._get_policy_events_int(ctx)

    def create_default_policies(self):
        '''**Description**
            Create a set of default policies using the current system falco rules file as a reference. For every falco rule in the system
            falco rules file, one policy will be created. The policy will take the name and description from the name and description of
            the corresponding falco rule. If a policy already exists with the same name, no policy is added or modified. Existing
            policies will be unchanged.

        **Arguments**
            - None

        **Success Return Value**
            JSON containing details on any new policies that were added.

        **Example**
            `examples/create_default_policies.py <https://github.com/draios/python-sdc-client/blob/master/examples/create_default_policies.py>`_

        '''
        res = requests.post(self.url + '/api/policies/createDefault', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def delete_all_policies(self):
        '''**Description**
            Delete all existing policies. The falco rules file is unchanged.

        **Arguments**
            - None

        **Success Return Value**
            The string "Policies Deleted"

        **Example**
            `examples/delete_all_policies.py <https://github.com/draios/python-sdc-client/blob/master/examples/delete_all_policies.py>`_

        '''
        res = requests.post(self.url + '/api/policies/deleteAll', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, "Policies Deleted"]

    def list_policies(self):
        '''**Description**
            List the current set of policies.

        **Arguments**
            - None

        **Success Return Value**
            A JSON object containing the number and details of each policy.

        **Example**
            `examples/list_policies.py <https://github.com/draios/python-sdc-client/blob/master/examples/list_policies.py>`_

        '''
        res = requests.get(self.url + '/api/policies', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def get_policy(self, name):
        '''**Description**
            Find the policy with name <name> and return its json description.

        **Arguments**
            - name: the name of the policy to fetch

        **Success Return Value**
            A JSON object containing the description of the policy. If there is no policy with
            the given name, returns False.

        **Example**
            `examples/get_policy.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_policy.py>`_

        '''
        res = requests.get(self.url + '/api/policies', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        policies = res.json()["policies"]

        # Find the policy with the given name and return it.
        for policy in policies:
            if policy["name"] == name:
                return [True, policy]

        return [False, "No policy with name {}".format(name)]

    def add_policy(self, policy_json):
        '''**Description**
            Add a new policy using the provided json.

        **Arguments**
            - policy_json: a description of the new policy

        **Success Return Value**
            The string "OK"

        **Example**
            `examples/add_policy.py <https://github.com/draios/python-sdc-client/blob/master/examples/add_policy.py>`_

        '''

        try:
            policy_obj = json.loads(policy_json)
        except Exception as e:
            return [False, "policy json is not valid json: {}".format(str(e))]

        body = {"policy": policy_obj}
        res = requests.post(self.url + '/api/policies', headers=self.hdrs, data=json.dumps(body), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def update_policy(self, policy_json):
        '''**Description**
            Update an existing policy using the provided json. The 'id' field from the policy is
            used to determine which policy to update.

        **Arguments**
            - policy_json: a description of the new policy

        **Success Return Value**
            The string "OK"

        **Example**
            `examples/update_policy.py <https://github.com/draios/python-sdc-client/blob/master/examples/update_policy.py>`_

        '''

        try:
            policy_obj = json.loads(policy_json)
        except Exception as e:
            return [False, "policy json is not valid json: {}".format(str(e))]

        if not "id" in policy_obj:
            return [False, "Policy Json does not have an 'id' field"]

        body = {"policy": policy_obj}

        res = requests.put(self.url + '/api/policies/{}'.format(policy_obj["id"]), headers=self.hdrs, data=json.dumps(body), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def delete_policy_name(self, name):
        '''**Description**
            Delete the policy with the given name.

        **Arguments**
            - name: the name of the policy to delete

        **Success Return Value**
            The JSON object representing the now-deleted policy.

        **Example**
            `examples/delete_policy.py <https://github.com/draios/python-sdc-client/blob/master/examples/delete_policy.py>`_

        '''
        res = requests.get(self.url + '/api/policies', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        # Find the policy with the given name and delete it
        for policy in res.json()["policies"]:
            if policy["name"] == name:
                return self.delete_policy_id(policy["id"])

        return [False, "No policy with name {}".format(name)]

    def delete_policy_id(self, id):
        '''**Description**
            Delete the policy with the given id

        **Arguments**
            - id: the id of the policy to delete

        **Success Return Value**
            The JSON object representing the now-deleted policy.

        **Example**
            `examples/delete_policy.py <https://github.com/draios/python-sdc-client/blob/master/examples/delete_policy.py>`_

        '''
        res = requests.delete(self.url + '/api/policies/{}'.format(id), headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]
