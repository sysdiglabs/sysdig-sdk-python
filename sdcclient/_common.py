import json
import os

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class SysdigHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        retry_strategy = Retry(
            total=3,
            status_forcelist=[500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "OPTIONS", "PUSH", "PUT"],
            backoff_factor=2,
        )
        kwargs["max_retries"] = retry_strategy

        self.ssl_verify = kwargs.get("ssl_verify", True)
        del kwargs["ssl_verify"]

        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        kwargs["verify"] = kwargs.get("verify", self.ssl_verify)

        return super().send(request, **kwargs)


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
        self.url = os.environ.get("SDC_URL", sdc_url).rstrip('/')
        self.ssl_verify = os.environ.get("SDC_SSL_VERIFY", None)
        if self.ssl_verify is None:
            self.ssl_verify = ssl_verify
        else:
            if self.ssl_verify.lower() in ['true', 'false']:
                self.ssl_verify = self.ssl_verify.lower() == 'true'

        adapter = SysdigHTTPAdapter(ssl_verify=self.ssl_verify)
        self.http = requests.Session()
        self.http.mount("https://", adapter)
        self.http.mount("http://", adapter)

    def __get_headers(self, custom_headers):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.token
        }
        if custom_headers:
            headers.update(custom_headers)
        return headers

    def _checkResponse(self, res):
        if res.status_code >= 300:  # FIXME: Should it be >=400? 301 = Moved Permanently, 302 = Found, 303 = See Other
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
            elif 'error' in j:
                self.lasterr = j['error']
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
        res = self.http.get(self.url + '/api/user/me', headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def get_user_token(self):
        '''**Description**
            Return the API token of the current user.

        **Success Return Value**
            A string containing the user token.
        '''
        res = self.http.get(self.url + '/api/token', headers=self.hdrs, verify=self.ssl_verify)
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
        res = self.http.get(self.url + '/api/agents/connected', headers=self.hdrs, verify=self.ssl_verify)
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
        res = self.http.get(self.url + '/api/agents/connected', headers=self.hdrs, verify=self.ssl_verify)
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
        res = self.http.get(self.url + '/api/notificationChannels', headers=self.hdrs, verify=self.ssl_verify)
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

        res = self.http.get(self.url + '/api/notificationChannels', headers=self.hdrs, verify=self.ssl_verify)

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
                        if 'name' in c:
                            if c['name'] == ch.get('name'):
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

        res = self.http.post(self.url + '/api/notificationChannels', headers=self.hdrs, data=json.dumps(channel_json),
                             verify=self.ssl_verify)
        return self._request_result(res)

    def create_notification_channel(self, channel):
        channel["id"] = None
        channel["version"] = None
        channel["createdOn"] = None
        channel["modifiedOn"] = None
        channel_json = {
            'notificationChannel': channel
        }

        res = self.http.post(self.url + '/api/notificationChannels', headers=self.hdrs, data=json.dumps(channel_json),
                             verify=self.ssl_verify)
        return self._request_result(res)

    def get_notification_channel(self, id):

        res = self.http.get(self.url + '/api/notificationChannels/' + str(id), headers=self.hdrs,
                            verify=self.ssl_verify)
        if not self._checkResponse(res):
            return False, self.lasterr

        return True, res.json()['notificationChannel']

    def update_notification_channel(self, channel):
        if 'id' not in channel:
            return [False, "Invalid channel format"]

        res = self.http.put(self.url + '/api/notificationChannels/' + str(channel['id']), headers=self.hdrs,
                            data=json.dumps({"notificationChannel": channel}), verify=self.ssl_verify)
        return self._request_result(res)

    def delete_notification_channel(self, channel):
        if 'id' not in channel:
            return [False, "Invalid channel format"]

        res = self.http.delete(self.url + '/api/notificationChannels/' + str(channel['id']), headers=self.hdrs,
                               verify=self.ssl_verify)
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
        res = self.http.get(self.url + '/api/history/timelines/', headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def get_data_promql(self, query, start, end, step, timeout=None, limit=None):
        '''**Description**
            Evaluate an expression query over a specified time range.

        **Arguments**
            - **query**: the PromQL query to execute.
            - **start**: the inclusive start timestamp of the query range as RFC3339 or a unix timestamp.
            - **end**: the inclusive end timestamp of the query range as RFC3339 or a unix timestamp.
            - **step**: the query resolution step width, specified as a duration or a floating-point number of seconds.
            - **timeout**: the evaluation timeout. Defaults to and is capped at 2m.
            - **limit**: the maximum number of returned series. A value of 0 disables the limit.

        **Success Return Value**
            A list of time series that matched the PromQL query, where each series is defined by a unique set of labels (metric) and a list
            of timestamped values (values). Each entry represents one time series over the queried range, with values sampled at regular intervals.

        **Examples**
            - `examples/get_data_promql_simple.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_data_promql_simple.py>`_
            - `examples/get_data_promql_advanced.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_data_promql_advanced.py>`_
        '''
        params = {
                "query": query,
                "start": start,
                "end":   end,
                "step":  step,
        }

        if timeout:
            params["timeout"] = timeout
        if limit:
            params["limit"] = limit

        url = f"{self.url}/prometheus/api/v1/query_range"
        res = self.http.get(url, headers=self.hdrs, params=params)
        return self._request_result(res)

    def get_data_promql_instant(self, query, time=None, timeout=None, limit=None):
        '''**Description**
            Evaluate an instant query at a single point in time.

        **Arguments**
            - **query**: the PromQL query to execute.
            - **time**: The evaluation timestamp as RFC3339 or a unix timestamp. If omitted, the current server time is used.
            - **timeout**: the evaluation timeout. Defaults to and is capped at 2m.
            - **limit**: the maximum number of returned series. A value of 0 disables the limit.

        **Success Return Value**
            A list of time series that matched the PromQL query, where each series is defined by a unique set of labels (metric) and a list
            of timestamped values (values). Each entry represents one time series over the queried range, with values sampled at regular intervals.

        **Examples**
            - `examples/get_data_promql_instant_simple.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_data_promql_instant_simple.py>`_
        '''
        params = {
                "query": query,
        }

        if time:
            params["time"] = time
        if timeout:
            params["timeout"] = timeout
        if limit:
            params["limit"] = limit

        url = f"{self.url}/prometheus/api/v1/query"
        res = self.http.get(url, headers=self.hdrs, params=params)
        return self._request_result(res)

    def get_series(self, match, start=None, end=None, limit=None):
        '''**Description**
            Retrieve metadata about time series that match a set of label matchers.

        **Arguments**
            - **match**: a list of PromQL matchers (e.g., `['up', 'node_cpu_seconds_total']`).
            - **start**: the inclusive start timestamp of the series query as RFC3339 or a unix timestamp.
            - **end**: the inclusive end timestamp of the series query as RFC3339 or a unix timestamp.
            - **limit**: the maximum number of returned series. The limit is capped at 10,000. To disable the limit, set the value to 0.

        **Success Return Value**
            A list of series that match the provided matchers.

        **Examples**
            - `examples/get_series.py`
        '''
        params = {
                "match[]": match,  # `match` should be a list of matchers
        }

        if start:
            params["start"] = start
        if end:
            params["end"] = end
        if limit:
            params["limit"] = limit

        url = f"{self.url}/prometheus/api/v1/series"
        res = self.http.get(url, headers=self.hdrs, params=params)
        return self._request_result(res)

    def get_labels(self, match=None, limit=None):
        '''**Description**
            Retrieve metadata about label names.

        **Arguments**
            - **match**: a list of PromQL matchers to filter the labels.
            - **limit**: the maximum number of returned labels. A value of 0 disables the limit.

        **Success Return Value**
            A list of available labels.

        **Examples**
            - `examples/get_labels.py`
        '''
        params = {}

        if match:
            params["match[]"] = match  # `match` should be a list of matchers
        if limit:
            params["limit"] = limit

        url = f"{self.url}/prometheus/api/v1/labels"
        res = self.http.get(url, headers=self.hdrs, params=params)
        return self._request_result(res)

    def get_label_values(self, label_name, match=None, limit=None):
        '''**Description**
            Retrieve the values for a specific label.

        **Arguments**
            - **label_name**: the name of the label to retrieve values for.
            - **match**: a list of PromQL matchers to filter the label values.
            - **limit**: the maximum number of returned values. A value of 0 disables the limit.

        **Success Return Value**
            A list of values for the specified label.

        **Examples**
            - `examples/get_label_values.py`
        '''
        params = {}

        if match:
            params["match[]"] = match  # `match` should be a list of matchers
        if limit:
            params["limit"] = limit

        url = f"{self.url}/prometheus/api/v1/label/{label_name}/values"
        res = self.http.get(url, headers=self.hdrs, params=params)
        return self._request_result(res)

    def get_metadata(self, metric_name=None, limit=None):
        '''**Description**
            Retrieve metadata about metrics.

        **Arguments**
            - **metric_name**: the metric name to filter metadata for. If omitted, metadata for all metrics is retrieved.
            - **limit**: the maximum number of returned metadata entries. A value of 0 disables the limit.

        **Success Return Value**
            A list of metadata entries for the specified metric(s).

        **Examples**
            - `examples/get_metadata.py`
        '''
        params = {}

        if metric_name:
            params["metric"] = metric_name
        if limit:
            params["limit"] = limit

        url = f"{self.url}/prometheus/api/v1/metadata"
        res = self.http.get(url, headers=self.hdrs, params=params)
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
            frm="&from=%d" % (from_sec * 10 ** 6) if from_sec else "",
            to="&to=%d" % (to_sec * 10 ** 6) if to_sec else "",
            scopeFilter="&scopeFilter=%s" % scope_filter if scope_filter else "")
        res = self.http.get(url, headers=self.hdrs, verify=self.ssl_verify)
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
        res = self.http.get(url, headers=self.hdrs, verify=self.ssl_verify)
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
            if hostname == agent.get('hostName'):
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

        res = self.http.post(self.url + '/api/sysdig', headers=self.hdrs, data=json.dumps(data), verify=self.ssl_verify)
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
        res = self.http.get(url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return False, self.lasterr

        return True, res.content

    def delete_sysdig_capture(self, capture_id):
        """
        Removes an existing Sysdig Capture from Monitor

        Args:
            capture_id: ID of the capture to remove

        Returns: A touple of (bool, error) where the first value is false if there's an error and the second value is the error.
        """

        res = self.http.delete(f'{self.url}/api/sysdig/{capture_id}', headers=self.hdrs, verify=self.ssl_verify)

        if not self._checkResponse(res):
            return False, self.lasterr

        return True, None

    def create_user(self, user_email, first_name=None, last_name=None, password=None):
        '''
        Provisions a new user to use Sysdig without sending an email notification.
        If password is not set through this request a random one is generated for the user
        which requires them to reset password on first login.

        Args:
            user_email (str): Email of the user to provision.
            first_name (str): First name of the user to provision. Can be null.
            last_name (str): Last name of the user to provision. Can be null.
            password (str): Default password for the user to provision. If this is not set, a random one is generated.

        Returns:
            The provisioned user information.

        '''

        user_info = {
            "username": user_email,
            "firstName": first_name,
            "lastName": last_name,
            "password": password,
        }
        user_info = {k: v for k, v in user_info.items() if v}

        res = self.http.post(self.url + '/api/user/provisioning/', headers=self.hdrs, data=json.dumps(user_info),
                             verify=self.ssl_verify)
        return self._request_result(res)

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
        res = self.http.get(self.url + '/api/users', headers=self.hdrs, verify=self.ssl_verify)
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

        res = self.http.post(self.url + '/api/users', headers=self.hdrs, data=json.dumps(user_json),
                             verify=self.ssl_verify)
        return self._request_result(res)

    def delete_user(self, user_email):
        '''**Description**
            Deletes a user from Sysdig Monitor.

        **Arguments**
            - **user_email**: the email address of the user that will be deleted from Sysdig Monitor

        **Example**
            `examples/user_team_mgmt.py <https://github.com/draios/python-sdc-client/blob/master/examples/user_team_mgmt.py>`_
        '''
        ok, res = self.get_user_ids([user_email])
        if not ok:
            return ok, res
        userid = res[0]
        res = self.http.delete(self.url + '/api/users/' + str(userid), headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, None]

    def get_user(self, user_email):
        res = self.http.get(self.url + '/api/users', headers=self.hdrs, verify=self.ssl_verify)
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
        res = self.http.get(self.url + '/api/users', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()['users']]

    def edit_user(self, user_email, firstName=None, lastName=None, systemRole=None):
        ok, user = self.get_user(user_email)
        if not ok:
            return ok, user

        reqbody = {
            'systemRole': systemRole if systemRole else user['systemRole'],
            'username': user_email,
            'enabled': user.get('enabled', False),
            'version': user['version']
        }

        if firstName is None:
            reqbody['firstName'] = user['firstName'] if 'firstName' in list(user.keys()) else ''
        else:
            reqbody['firstName'] = firstName

        if lastName is None:
            reqbody['lastName'] = user['lastName'] if 'lastName' in list(user.keys()) else ''
        else:
            reqbody['lastName'] = lastName

        res = self.http.put(self.url + '/api/users/' + str(user['id']), headers=self.hdrs, data=json.dumps(reqbody),
                            verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, 'Successfully edited user']

    def get_teams(self, team_filter='', product_filter=''):
        '''**Description**
            Return the set of teams that match the filter specified. The *team_filter* should be a substring of the names of the teams to be returned.

        **Arguments**
            - **team_filter**: the team filter to match when returning the list of teams
            - **product_filter**: the product to match when returning the list of teams (SDC-Monitor, SDS-secure)

        **Success Return Value**
            The teams that match the filter.
        '''
        url = f'{self.url}/api/teams'
        if product_filter:
            if product_filter not in ['SDC', 'SDS']:
                return [False, 'invalid product header, allowed only "SDC" or "SDS"']
            url = f'{url}?product={product_filter}'

        res = self.http.get(url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        ret = [t for t in res.json()['teams'] if team_filter in t['name']]

        return [True, ret]

    def get_team_by_id(self, id):
        '''**Description**
            Return the team with the specified team ID, if it is present.

        **Arguments**
            - **id**: the ID of the team to return

        **Success Return Value**
            The requested team.

        **Example**
            `examples/user_team_mgmt.py <https://github.com/draios/python-sdc-client/blob/master/examples/user_team_mgmt.py>`_
        '''
        res = self.http.get(self.url + '/api/teams/' + str(id), headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()['team']]

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
        res = self.http.get(self.url + '/api/v2/teams/light/name/' + str(name), headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        light_team = res.json()['team']

        ok, team_with_memberships = self.get_team_by_id(light_team['id'])

        if not ok:
            return [False, self.lasterr]

        return [True, team_with_memberships]

    def get_team_ids(self, teams):
        res = self.http.get(self.url + '/api/teams', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        u = [x for x in res.json()['teams'] if x['name'] in teams]
        return [True, [x['id'] for x in u]]

    def _get_user_id_dict(self, users):
        res = self.http.get(self.url + '/api/users', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        u = [x for x in res.json()['users'] if x['username'] in users]
        return [True, dict((user['username'], user['id']) for user in u)]

    def _get_id_user_dict(self, user_ids):
        res = self.http.get(self.url + '/api/users', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        u = [x for x in res.json()['users'] if x['id'] in user_ids]
        return [True, dict((user['id'], user['username']) for user in u)]

    def get_user_ids(self, users):
        ok, res = self._get_user_id_dict(users)
        if not ok:
            return ok, res
        else:
            return [True, list(res.values())]

    def create_team(self, name, memberships=None, filter='', description='', show='host', theme='#7BB0B2',
                    perm_capture=False, perm_custom_events=False, perm_aws_data=False, perm_rapid_response=False):
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
            - **perm_rapid_response**: if True, this team will have access rapid response feature.

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
            'canUseRapidResponse': perm_rapid_response,
        }

        # Map user-names to IDs
        if memberships:
            ok, res = self._get_user_id_dict(list(memberships.keys()))
            if not ok:
                return [False, 'Could not fetch IDs for user names']
            reqbody['userRoles'] = [
                {
                    'userId': user_id,
                    'role': memberships[user_name]
                }
                for (user_name, user_id) in res.items()
            ]
        else:
            reqbody['users'] = []

        if filter != '':
            reqbody['filter'] = filter

        res = self.http.post(self.url + '/api/teams', headers=self.hdrs, data=json.dumps(reqbody),
                             verify=self.ssl_verify)
        return self._request_result(res)

    def edit_team(self, name, memberships=None, filter=None, description=None, show=None, theme=None,
                  perm_capture=None, perm_custom_events=None, perm_aws_data=None, perm_rapid_response=False):
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
            - **perm_rapid_response**: if True, this team will have access rapid response feature.

        **Success Return Value**
            The edited team.

        **Example**
            `examples/user_team_mgmt.py <https://github.com/draios/python-sdc-client/blob/master/examples/user_team_mgmt.py>`_
        '''
        ok, team = self.get_team(name)
        if not ok:
            return ok, team

        reqbody = {
            'name': name,
            'theme': theme if theme else team['theme'],
            'show': show if show else team['show'],
            'canUseSysdigCapture': perm_capture if perm_capture else team['canUseSysdigCapture'],
            'canUseCustomEvents': perm_custom_events if perm_custom_events else team['canUseCustomEvents'],
            'canUseAwsMetrics': perm_aws_data if perm_aws_data else team['canUseAwsMetrics'],
            'canUseRapidResponse': perm_rapid_response,
            'defaultTeamRole': team['defaultTeamRole'],
            'entryPoint': team['entryPoint'],
            'id': team['id'],
            'version': team['version']
        }

        # Handling team description
        if description is not None:
            reqbody['description'] = description
        elif 'description' in list(team.keys()):
            reqbody['description'] = team['description']

        # Handling for users to map (user-name, team-role) pairs to memberships
        if memberships is not None:
            ok, res = self._get_user_id_dict(list(memberships.keys()))
            if not res:
                return [False, 'Could not convert user names to IDs']
            reqbody['userRoles'] = [
                {
                    'userId': user_id,
                    'role': memberships[user_name]
                }
                for (user_name, user_id) in res.items()
            ]
        elif 'userRoles' in list(team.keys()):
            reqbody['userRoles'] = team['userRoles']
        else:
            reqbody['userRoles'] = []

        # Special handling for filters since we don't support blank filters
        if filter is not None:
            reqbody['filter'] = filter
        elif 'filter' in list(team.keys()):
            reqbody['filter'] = team['filter']

        res = self.http.put(self.url + '/api/teams/' + str(team['id']), headers=self.hdrs, data=json.dumps(reqbody),
                            verify=self.ssl_verify)
        return self._request_result(res)

    def delete_team(self, name):
        '''**Description**
            Deletes a team from Sysdig Monitor.

        **Arguments**
            - **name**: the name of the team that will be deleted from Sysdig Monitor

        **Example**
            `examples/user_team_mgmt.py <https://github.com/draios/python-sdc-client/blob/master/examples/user_team_mgmt.py>`_
        '''
        ok, team = self.get_team(name)
        if not ok:
            return ok, team

        res = self.http.delete(self.url + '/api/teams/' + str(team['id']), headers=self.hdrs, verify=self.ssl_verify)
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
        ok, res = self.get_team(team)
        if not ok:
            return ok, res

        raw_memberships = res['userRoles']
        user_ids = [m['userId'] for m in raw_memberships]

        ok, res = self._get_id_user_dict(user_ids)
        if not ok:
            return [False, 'Could not fetch IDs for user names']
        else:
            return [True, dict([(res[m['userId']], m['role']) for m in raw_memberships])]

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

    def list_access_keys(self):
        '''
        **Description**
            List all the access keys enabled and disabled for this instance of Sysdig Monitor/Secure

        **Reslut**
            A list of access keys objects

        **Example**
            `examples/list_access_keys.py <https://github.com/draios/python-sdc-client/blob/master/examples/list_access_keys.py>`_
        '''
        res = self.http.get(self.url + '/api/customer/accessKeys', headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def create_access_key(self, agent_limit=None, agent_reserved=None, team_id=None):
        '''
        **Description**
            Create a new access key for Sysdig Monitor/Secure

        **Reslut**
            The access keys object
        '''
        access_key_payload = {
            "customerAccessKey": {
                "limit": agent_limit,
                "reservation": agent_reserved,
                "teamId": team_id
            }
        }

        res = self.http.post(self.url + '/api/customer/accessKeys', headers=self.hdrs, verify=self.ssl_verify, data=json.dumps(access_key_payload))
        return self._request_result(res)

    def update_access_key(self, access_key, agent_limit=None, agent_reserved=None, team_id=None):
        '''
        **Description**
            Create a new access key for Sysdig Monitor/Secure

        **Reslut**
            The access keys object
        '''
        access_key_payload = {
            "customerAccessKey": {
                "limit": agent_limit,
                "reservation": agent_reserved,
                "teamId": team_id
            }
        }

        res = self.http.put(self.url + '/api/customer/accessKeys/' + access_key, headers=self.hdrs, verify=self.ssl_verify, data=json.dumps(access_key_payload))
        return self._request_result(res)

    def disable_access_key(self, access_key):
        '''
        **Description**
            Disable an existing access key

        **Arguments**
            - **access_key**: the access key to be disabled

        **Reslut**
            The access keys object
        '''
        res = self.http.post(self.url + '/api/customer/accessKeys/' + access_key + "/disable/", headers=self.hdrs,
                             verify=self.ssl_verify)
        return self._request_result(res)

    def enable_access_key(self, access_key):
        '''
        **Description**
            Enable an existing access key

        **Arguments**
            - **access_key**: the access key to be enabled

        **Reslut**
            The access keys object
        '''
        res = self.http.post(self.url + '/api/customer/accessKeys/' + access_key + "/enable/", headers=self.hdrs,
                             verify=self.ssl_verify)
        return self._request_result(res)

    def get_agents_config(self):
        res = self.http.get(self.url + '/api/agents/config', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        data = res.json()
        return [True, data]

    def set_agents_config(self, config):
        res = self.http.put(self.url + '/api/agents/config', headers=self.hdrs, data=json.dumps(config),
                            verify=self.ssl_verify)
        return self._request_result(res)

    def clear_agents_config(self):
        data = {'files': []}
        return self.set_agents_config(data)

    def get_user_api_token(self, username, teamname):
        ok, team = self.get_team(teamname)
        if not ok:
            return ok, team

        res = self.http.get(self.url + '/api/token/%s/%d' % (username, team['id']), headers=self.hdrs,
                            verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        data = res.json()
        return [True, data['token']['key']]

    def _request_result(self, res):
        if not self._checkResponse(res):
            return False, self.lasterr

        return True, res.json()
