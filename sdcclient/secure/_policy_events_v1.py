import datetime

from sdcclient._common import _SdcCommon


class PolicyEventsClientV1(_SdcCommon):
    def __init__(self, token="", sdc_url='https://secure.sysdig.com', ssl_verify=True, custom_headers=None):
        super(PolicyEventsClientV1, self).__init__(token, sdc_url, ssl_verify, custom_headers)
        self.product = "SDS"

    def _get_policy_events_int(self, ctx):
        limit = ctx.get("limit", 50)
        policy_events_url = self.url + '/api/v1/secureEvents?limit={limit}{frm}{to}{filter}{cursor}'.format(
            limit=limit,
            frm=f"&from={int(ctx['from']):d}" if "from" in ctx else "",
            to=f"&to={int(ctx['to']):d}" if "to" in ctx else "",
            filter=f'&filter={ctx["filter"]}' if "filter" in ctx else "",
            cursor=f'&cursor={ctx["cursor"]}' if "cursor" in ctx else "")

        res = self.http.get(policy_events_url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        ctx = {
            "limit": limit,
            "cursor": res.json()["page"].get("prev", None)
        }

        return [True, {"ctx": ctx, "data": res.json()["data"]}]

    def get_policy_events_range(self, from_sec, to_sec, filter=None):
        '''**Description**
            Fetch all policy events that occurred in the time range [from_sec:to_sec]. This method is used in conjunction
            with :func:`~sdcclient.SdSecureClient.get_more_policy_events` to provide paginated access to policy events.

        **Arguments**
            - from_sec: the start of the timerange for which to get events
            - end_sec: the end of the timerange for which to get events
            - filter: this is a SysdigMonitor-like filter (e.g. filter: 'severity in ("4","5") and freeText in ("Suspicious")')

        **Success Return Value**
            An array containing:
              - A context object that should be passed to later calls to get_more_policy_events.
              - An array of policy events, in JSON format. See :func:`~sdcclient.SdSecureClient.get_more_policy_events`
                for details on the contents of policy events.

        **Example**
            `examples/get_secure_policy_events.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_secure_policy_events.py>`_

        '''
        options = {"from": int(from_sec) * 1_000_000_000,
                   "to": int(to_sec) * 1_000_000_000,
                   "limit": 999,
                   "filter": filter}
        ctx = {k: v for k, v in options.items() if v is not None}
        return self._get_policy_events_int(ctx)

    def get_policy_events_duration(self, duration_sec, filter=None):
        '''**Description**
            Fetch all policy events that occurred in the last duration_sec seconds. This method is used in conjunction with
            :func:`~sdcclient.SdSecureClient.get_more_policy_events` to provide paginated access to policy events.

        **Arguments**
            - duration_sec: Fetch all policy events that have occurred in the last *duration_sec* seconds.
            - filter: this is a SysdigMonitor-like filter (e.g. filter: 'severity in ("4","5") and freeText in ("Suspicious")')

        **Success Return Value**
            An array containing:
              - A context object that should be passed to later calls to get_more_policy_events.
              - An array of policy events, in JSON format. See :func:`~sdcclient.SdSecureClient.get_more_policy_events`
                for details on the contents of policy events.

        **Example**
            `examples/get_secure_policy_events.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_secure_policy_events.py>`_

        '''
        to_sec = int((datetime.datetime.utcnow() - datetime.datetime.utcfromtimestamp(0)).total_seconds())
        from_sec = to_sec - (int(duration_sec))

        return self.get_policy_events_range(from_sec, to_sec, filter)

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
                 - id: a unique identifier for this policy event
                 - cursor: unique ID that can be used with get_more_policy_events context to retrieve paginated policy events
                 - timestamp: when the event occurred (ns since the epoch)
                 - source: the source of the policy event. It can be "syscall" or "k8s_audit"
                 - description: the description of the event
                 - severity: a severity level from 1-7
                 - agentId: the agent that reported this event
                 - machineId: the MAC of the machine that reported this event
                 - content: More information about what triggered the event
                     - falsePositive: if the event is considered a false-positive
                     - fields: raw information from the rule that fired this event
                     - output: Output from the rule that fired this event
                     - policyId: the ID of the policy that fired this event
                     - ruleName: name of the rule that fired this event
                     - ruleTags: tags from the rule that fired this event
                 - labels: more information from the scope of this event

            When the number of policy events returned is 0, there are no remaining events and you can stop calling get_more_policy_events().

        **Example**
            `examples/get_secure_policy_events.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_secure_policy_events.py>`_
        '''
        return self._get_policy_events_int(ctx)

    def get_policy_event(self, event_id):
        """

        Args:
            event_id: The ID of the Runtime Policy event to retrieve more info from.

        Returns:
            A tuple where the first parameter indicates if the request was successful, and the second parameter
            holds the info from the policy event or the error.
        """
        policy_events_url = f'{self.url}/api/v1/secureEvents/{event_id}'

        res = self.http.get(policy_events_url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return False, self.lasterr

        return True, res.json()
