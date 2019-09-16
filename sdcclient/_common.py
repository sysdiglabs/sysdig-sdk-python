import os
import json
import requests


class _SdcCommon(object):
    '''Interact with the Sysdig Monitor/Secure API.

    **Arguments**
        - **token**: A Sysdig Monitor/Secure API token from the *Sysdig Cloud API* section of the Settings page for `monitor <https://app.sysdigcloud.com/#/settings/user>`_ or .`secure <https://secure.sysdig.com/#/settings/user>`_.
        - **sdc_url**: URL for contacting the Sysdig API server. Set this in `On-Premises installs <https://support.sysdigcloud.com/hc/en-us/articles/206519903-On-Premises-Installation-Guide>`__.
        - **ssl_verify**: Whether to verify certificate. Set to False if using a self-signed certificate in an `On-Premises install <https://support.sysdigcloud.com/hc/en-us/articles/206519903-On-Premises-Installation-Guide>`__.
        - **custom_headers**: [dict] Pass in custom headers. Useful for authentication and will override the default headers.

    **Returns**
        An object for further interactions with the Sysdig Monitor/Secure API. See methods below.
    '''
    lasterr = None

    def __init__(self, token="", sdc_url='https://app.sysdigcloud.com', ssl_verify=True, custom_headers=None):
        self.token = os.environ.get("SDC_TOKEN", token)
        self.hdrs = self.__get_headers(custom_headers)
        self.url = os.environ.get("SDC_URL", sdc_url)
        self.ssl_verify = os.environ.get("SDC_SSL_VERIFY", None)
        if self.ssl_verify == None:
            self.ssl_verify = ssl_verify
        else:
            self.ssl_verify = self.ssl_verify.lower() == 'true'

    def __get_headers(self, custom_headers):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.token
        }
        if custom_headers:
            headers.update(custom_headers)
        return headers

    def _checkResponse(self, res):
        if res.status_code >= 300:
            errorcode = res.status_code
            self.lasterr = None

            try:
                j = res.json()
            except Exception:
                self.lasterr = 'status code ' + str(errorcode)
                return False

            if 'errors' in j:
                error_msgs = []
                for error in j['errors']:
                    error_msg = []
                    if 'message' in error:
                        error_msg.append(error['message'])

                    if 'reason' in error:
                        error_msg.append(error['reason'])

                    error_msgs.append(': '.join(error_msg))

                self.lasterr = '\n'.join(error_msgs)
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
        return self._request_result(res)

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

    def list_notification_channels(self):
        '''**Description**
            List all configured Notification Channels

        **Arguments**
            none

        **Success Return Value**
            A JSON representation of all the notification channels
        '''
        res = requests.get(self.url + '/api/notificationChannels', headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def get_notification_ids(self, channels=None):
        '''**Description**
            Get an array of all configured Notification Channel IDs, or a filtered subset of them.

        **Arguments**
            - **channels**: an optional array of dictionaries to limit the set of Notification Channel IDs returned. If not specified, IDs for all configured Notification Channels are returned. Each dictionary contains a ``type`` field that can be one of the available types of Notification Channel (``EMAIL``, ``SNS``, ``PAGER_DUTY``, ``SLACK``, ``OPSGENIE``, ``VICTOROPS``, ``WEBHOOK``) as well as additional elements specific to each channel type.

        **Success Return Value**
            An array of Notification Channel IDs (integers).

        **Examples**
            - `examples/create_alert.py <https://github.com/draios/python-sdc-client/blob/master/examples/create_alert.py>`_
            - `examples/restore_alerts.py <https://github.com/draios/python-sdc-client/blob/master/examples/restore_alerts.py>`_
        '''

        res = requests.get(self.url + '/api/notificationChannels', headers=self.hdrs, verify=self.ssl_verify)

        if not self._checkResponse(res):
            return False, self.lasterr

        ids = []

        # If no array of channel types/names was provided to filter by,
        # just return them all.
        if channels is None:
            for ch in res.json()["notificationChannels"]:
                ids.append(ch['id'])
            return [True, ids]

        # Return the filtered set of channels based on the provided types/names array.
        # Should try and improve this M * N lookup
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
                            if c['name'] == ch.get('name'):
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
                            if c['name'] == ch.get('name'):
                                found = True
                                ids.append(ch['id'])
                    elif c['type'] == 'VICTOROPS':
                        if 'name' in c:
                            if c['name'] == ch.get('name'):
                                found = True
                                ids.append(ch['id'])
                    elif c['type'] == 'WEBHOOK':
                        if 'name' in c:
                            if c['name'] == ch.get('name'):
                                found = True
                                ids.append(ch['id'])
            if not found:
                return False, "Channel not found: " + str(c)

        return True, ids

    def create_email_notification_channel(self, channel_name, email_recipients):
        channel_json = {
            'notificationChannel': {
                'type': 'EMAIL',
                'name': channel_name,
                'enabled': True,
                'options': {
                    'emailRecipients': email_recipients
                }
            }
        }

        res = requests.post(self.url + '/api/notificationChannels', headers=self.hdrs, data=json.dumps(channel_json), verify=self.ssl_verify)
        return self._request_result(res)

    def create_notification_channel(self, channel):
        channel["id"] = None
        channel["version"] = None
        channel["createdOn"] = None
        channel["modifiedOn"] = None
        channel_json = {
            'notificationChannel': channel
        }

        res = requests.post(self.url + '/api/notificationChannels', headers=self.hdrs, data=json.dumps(channel_json),
                            verify=self.ssl_verify)
        return self._request_result(res)

    def get_notification_channel(self, id):

        res = requests.get(self.url + '/api/notificationChannels/' + str(id), headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return False, self.lasterr

        return True, res.json()['notificationChannel']

    def update_notification_channel(self, channel):
        if 'id' not in channel:
            return [False, "Invalid channel format"]

        res = requests.put(self.url + '/api/notificationChannels/' + str(channel['id']), headers=self.hdrs, data=json.dumps({"notificationChannel": channel}), verify=self.ssl_verify)
        return self._request_result(res)

    def delete_notification_channel(self, channel):
        if 'id' not in channel:
            return [False, "Invalid channel format"]

        res = requests.delete(self.url + '/api/notificationChannels/' + str(channel['id']), headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return False, self.lasterr
        return True, None

    def get_data_retention_info(self):
        '''**Description**
            Return the list of data retention intervals, with beginning and end UTC time for each of them. Sysdig Monitor performs rollups of the data it stores. This means that data is stored at different time granularities depending on how far back in time it is. This call can be used to know what precision you can expect before you make a call to :func:`~SdcClient.get_data`.

        **Success Return Value**
            A dictionary containing the list of available sampling intervals.

        **Example**
            `examples/print_data_retention_info.py <https://github.com/draios/python-sdc-client/blob/master/examples/print_data_retention_info.py>`_
        '''
        res = requests.get(self.url + '/api/history/timelines/', headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

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
            # 'filter': {
            #    'filters': [
            #        {
            #            'metric': 'agent.tag.Tag',
            #            'op': '=',
            #            'value': 'production-maintenance',
            #            'filters': None
            #        }
            #    ],
            #    'logic': 'and'
            # },
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
        return self._request_result(res)

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
        options = {
            'name': name,
            'description': description,
            'severity': severity,
            'filter': event_filter,
            'tags': tags
        }
        edata = {
            'event': {k: v for k, v in options.items() if v is not None}
        }
        res = requests.post(self.url + '/api/events/', headers=self.hdrs, data=json.dumps(edata), verify=self.ssl_verify)
        return self._request_result(res)

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
        options = {
            'name': name,
            'from': from_ts,
            'to': to_ts,
            'tags': tags
        }
        params = {k: v for k, v in options.items() if v is not None}
        res = requests.get(self.url + '/api/events/', headers=self.hdrs, params=params, verify=self.ssl_verify)
        return self._request_result(res)

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
            - **paging**: if segmentation of the query generates values for several different entities (e.g. containers/hosts), this parameter specifies which to include in the returned result. It's specified as a dictionary of inclusive values for ``from`` and ``to`` with the default being ``{ "from": 0, "to": 9 }``, which will return values for the "top 10" entities. The meaning of "top" is query-dependent, based on points having been sorted via the specified group aggregation, with the results sorted in ascending order if the group aggregation is ``min`` or ``none``, and descending order otherwise.

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
        return self._request_result(res)

    def get_sysdig_captures(self, from_sec=None, to_sec=None, scope_filter=None):
        '''**Description**
            Returns the list of sysdig captures for the user.

        **Arguments**
            - from_sec: the start of the timerange for which to get the captures
            - end_sec: the end of the timerange for which to get the captures
            - scope_filter: this is a SysdigMonitor-like filter (e.g 'container.image=ubuntu'). When provided, events are filtered by their scope, so only a subset will be returned (e.g. 'container.image=ubuntu' will provide only events that have happened on an ubuntu container).

        **Success Return Value**
            A dictionary containing the list of captures.

        **Example**
            `examples/list_sysdig_captures.py <https://github.com/draios/python-sdc-client/blob/master/examples/list_sysdig_captures.py>`_
        '''
        url = '{url}/api/sysdig?source={source}{frm}{to}{scopeFilter}'.format(
            url=self.url,
            source=self.product,
            frm="&from=%d" % (from_sec * 10**6) if from_sec else "",
            to="&to=%d" % (to_sec * 10**6) if to_sec else "",
            scopeFilter="&scopeFilter=%s" % scope_filter if scope_filter else "")
        res = requests.get(url, headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

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

        url = '{url}/api/sysdig/{id}?source={source}'.format(
            url=self.url, id=capture['id'], source=self.product)
        res = requests.get(url, headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

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
            'name': capture_name,
            'duration': duration,
            'folder': folder,
            'filters': capture_filter,
            'bucketName': '',
            'source': self.product
        }

        res = requests.post(self.url + '/api/sysdig', headers=self.hdrs, data=json.dumps(data), verify=self.ssl_verify)
        return self._request_result(res)

    def download_sysdig_capture(self, capture_id):
        '''**Description**
            Download a sysdig capture by id.

        **Arguments**
            - **capture_id**: the capture id to download.

        **Success Return Value**
            The bytes of the scap
        '''
        url = '{url}/api/sysdig/{id}/download?_product={product}'.format(
            url=self.url, id=capture_id, product=self.product)
        res = requests.get(url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return False, self.lasterr

        return True, res.content

    def create_user_invite(self, user_email, first_name=None, last_name=None, system_role=None):
        '''**Description**
            Invites a new user to use Sysdig Monitor. This should result in an email notification to the specified address.

        **Arguments**
            - **user_email**: the email address of the user that will be invited to use Sysdig Monitor
            - **first_name**: the first name of the user being invited
            - **last_name**: the last name of the user being invited
            - **system_role**: system-wide privilege level for this user regardless of team. specify 'ROLE_CUSTOMER' to create an Admin. if not specified, default is a non-Admin ('ROLE_USER').

        **Success Return Value**
            The newly created user.

        **Examples**
            - `examples/user_team_mgmt.py <https://github.com/draios/python-sdc-client/blob/master/examples/user_team_mgmt.py>`_
            - `examples/user_team_mgmt_extended.py <https://github.com/draios/python-sdc-client/blob/master/examples/user_team_mgmt_extended.py>`_

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
        options = {'username': user_email,
                   'firstName': first_name,
                   'lastName': last_name,
                   'systemRole': system_role}
        user_json = {k: v for k, v in options.items() if v is not None}

        res = requests.post(self.url + '/api/users', headers=self.hdrs, data=json.dumps(user_json), verify=self.ssl_verify)
        return self._request_result(res)

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
        res = requests.delete(self.url + '/api/users/' + str(userid), headers=self.hdrs, verify=self.ssl_verify)
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

    def edit_user(self, user_email, firstName=None, lastName=None, systemRole=None):
        res = self.get_user(user_email)
        if res[0] == False:
            return res
        user = res[1]
        reqbody = {
            'systemRole': systemRole if systemRole else user['systemRole'],
            'username': user_email,
            'enabled': user.get('enabled', False),
            'version': user['version']
        }

        if firstName == None:
            reqbody['firstName'] = user['firstName'] if 'firstName' in list(user.keys()) else ''
        else:
            reqbody['firstName'] = firstName

        if lastName == None:
            reqbody['lastName'] = user['lastName'] if 'lastName' in list(user.keys()) else ''
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
        ret = [t for t in res.json()['teams'] if team_filter in t['name']]
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
        u = [x for x in res.json()['teams'] if x['name'] in teams]
        return [True, [x['id'] for x in u]]

    def _get_user_id_dict(self, users):
        res = requests.get(self.url + '/api/users', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        u = [x for x in res.json()['users'] if x['username'] in users]
        return [True, dict((user['username'], user['id']) for user in u)]

    def _get_id_user_dict(self, user_ids):
        res = requests.get(self.url + '/api/users', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        u = [x for x in res.json()['users'] if x['id'] in user_ids]
        return [True, dict((user['id'], user['username']) for user in u)]

    def get_user_ids(self, users):
        res = self._get_user_id_dict(users)
        if res[0] == False:
            return res
        else:
            return [True, list(res[1].values())]

    def create_team(self, name, memberships=None, filter='', description='', show='host', theme='#7BB0B2',
                    perm_capture=False, perm_custom_events=False, perm_aws_data=False):
        '''
        **Description**
            Creates a new team

        **Arguments**
            - **name**: the name of the team to create.
            - **memberships**: dictionary of (user-name, team-role) pairs that should describe new memberships of the team.
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
        if memberships != None and len(memberships) != 0:
            res = self._get_user_id_dict(list(memberships.keys()))
            if res[0] == False:
                return [False, 'Could not fetch IDs for user names']
            reqbody['userRoles'] = [
                {
                    'userId': user_id,
                    'role': memberships[user_name]
                }
                for (user_name, user_id) in res[1].items()
            ]
        else:
            reqbody['users'] = []

        if filter != '':
            reqbody['filter'] = filter

        res = requests.post(self.url + '/api/teams', headers=self.hdrs, data=json.dumps(reqbody), verify=self.ssl_verify)
        return self._request_result(res)

    def edit_team(self, name, memberships=None, filter=None, description=None, show=None, theme=None,
                  perm_capture=None, perm_custom_events=None, perm_aws_data=None):
        '''
        **Description**
           Edits an existing team. All arguments are optional. Team settings for any arguments unspecified will remain at their current settings.

        **Arguments**
            - **name**: the name of the team to edit.
            - **memberships**: dictionary of (user-name, team-role) pairs that should describe new memberships of the team.
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
            'theme': theme if theme else t['theme'],
            'show': show if show else t['show'],
            'canUseSysdigCapture': perm_capture if perm_capture else t['canUseSysdigCapture'],
            'canUseCustomEvents': perm_custom_events if perm_custom_events else t['canUseCustomEvents'],
            'canUseAwsMetrics': perm_aws_data if perm_aws_data else t['canUseAwsMetrics'],
            'id': t['id'],
            'version': t['version']
        }

        # Handling team description
        if description is not None:
            reqbody['description'] = description
        elif 'description' in list(t.keys()):
            reqbody['description'] = t['description']

        # Handling for users to map (user-name, team-role) pairs to memberships
        if memberships != None:
            res = self._get_user_id_dict(list(memberships.keys()))
            if res[0] == False:
                return [False, 'Could not convert user names to IDs']
            reqbody['userRoles'] = [
                {
                    'userId': user_id,
                    'role': memberships[user_name]
                }
                for (user_name, user_id) in res[1].items()
            ]
        elif 'userRoles' in list(t.keys()):
            reqbody['userRoles'] = t['userRoles']
        else:
            reqbody['userRoles'] = []

        # Special handling for filters since we don't support blank filters
        if filter != None:
            reqbody['filter'] = filter
        elif 'filter' in list(t.keys()):
            reqbody['filter'] = t['filter']

        res = requests.put(self.url + '/api/teams/' + str(t['id']), headers=self.hdrs, data=json.dumps(reqbody), verify=self.ssl_verify)
        return self._request_result(res)

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

    def list_memberships(self, team):
        '''
        **Description**
            List all memberships for specified team.

        **Arguments**
            - **team**: the name of the team for which we want to see memberships

        **Result**
            Dictionary of (user-name, team-role) pairs that should describe memberships of the team.

        **Example**
            `examples/user_team_mgmt_extended.py <https://github.com/draios/python-sdc-client/blob/master/examples/user_team_mgmt_extended.py>`_
        '''
        res = self.get_team(team)
        if res[0] == False:
            return res

        raw_memberships = res[1]['userRoles']
        user_ids = [m['userId'] for m in raw_memberships]

        res = self._get_id_user_dict(user_ids)
        if res[0] == False:
            return [False, 'Could not fetch IDs for user names']
        else:
            id_user_dict = res[1]

        return [True, dict([(id_user_dict[m['userId']], m['role']) for m in raw_memberships])]

    def save_memberships(self, team, memberships):
        '''
        **Description**
            Create new user team memberships or update existing ones.

        **Arguments**
            - **team**: the name of the team for which we are creating new memberships
            - **memberships**: dictionary of (user-name, team-role) pairs that should describe new memberships

        **Example**
            `examples/user_team_mgmt_extended.py <https://github.com/draios/python-sdc-client/blob/master/examples/user_team_mgmt_extended.py>`_
        '''

        res = self.list_memberships(team)

        if res[0] is False:
            return res

        full_memberships = res[1]
        full_memberships.update(memberships)

        res = self.edit_team(team, full_memberships)

        if res[0] is False:
            return res
        else:
            return [True, None]

    def remove_memberships(self, team, users):
        '''
        **Description**
            Remove user memberships from specified team.

        **Arguments**
            - **team**: the name of the team from which user memberships are removed
            - **users**: list of usernames which should be removed from team

        **Example**
            `examples/user_team_mgmt_extended.py <https://github.com/draios/python-sdc-client/blob/master/examples/user_team_mgmt_extended.py>`_
        '''

        res = self.list_memberships(team)

        if res[0] is False:
            return res

        old_memberships = res[1]
        new_memberships = {k: v for k, v in old_memberships.items() if k not in users}

        res = self.edit_team(team, new_memberships)

        if res[0] is False:
            return res
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
        return self._request_result(res)

    def clear_agents_config(self):
        data = {'files': []}
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

    def _request_result(self, res):
        if not self._checkResponse(res):
            return False, self.lasterr

        return True, res.json()
