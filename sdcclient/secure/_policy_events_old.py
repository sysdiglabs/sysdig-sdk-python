import datetime
import json
from warnings import warn

from sdcclient._common import _SdcCommon


class PolicyEventsClientOld(_SdcCommon):
    def __init__(self, token="", sdc_url='https://secure.sysdig.com', ssl_verify=True, custom_headers=None):
        super(PolicyEventsClientOld, self).__init__(token, sdc_url, ssl_verify, custom_headers)
        self.product = "SDS"

    def _get_policy_events_int(self, ctx):
        warn("The PolicyEventsClientOld class is deprecated in favour of PolicyEventsClientV1; use it only if you have "
             "an old on-premises installation", DeprecationWarning, 3)
        policy_events_url = self.url + '/api/policyEvents{id}?from={frm:d}&to={to:d}&offset={offset}&limit={limit}{sampling}{aggregations}{scope}{filter}'.format(
            id="/%s" % ctx["id"] if "id" in ctx else "",
            frm=int(ctx['from']),
            to=int(ctx['to']),
            offset=ctx['offset'],
            limit=ctx['limit'],
            sampling='&sampling=%d' % int(ctx['sampling']) if "sampling" in ctx else "",
            aggregations='&aggregations=%s' % json.dumps(ctx['aggregations']) if "aggregations" in ctx else "",
            scope='&scopeFilter=%s' % ctx['scopeFilter'] if "scopeFilter" in ctx else "",
            filter='&eventFilter=%s' % ctx['eventFilter'] if "eventFilter" in ctx else "")

        res = self.http.get(policy_events_url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        # Increment the offset by limit
        ctx['offset'] += ctx['limit']

        return [True, {"ctx": ctx, "data": res.json()}]

    def get_policy_events_range(self, from_sec, to_sec, sampling=None, aggregations=None, scope_filter=None,
                                event_filter=None):
        '''**Description**
            Fetch all policy events that occurred in the time range [from_sec:to_sec]. This method is used in conjunction
            with :func:`~sdcclient.SdSecureClient.get_more_policy_events` to provide paginated access to policy events.

        **Arguments**
            - from_sec: the start of the timerange for which to get events
            - end_sec: the end of the timerange for which to get events
            - sampling: sample all policy events using *sampling* interval.
            - aggregations: When present it specifies how to aggregate events (sampling does not need to be specified, because when it's present it automatically means events will be aggregated). This field can either be a list of scope metrics or a list of policyEvents fields but (currently) not a mix of the two. When policy events fields are specified, only these can be used= severity, agentId, containerId, policyId, ruleType.
            - scope_filter: this is a SysdigMonitor-like filter (e.g 'container.image=ubuntu'). When provided, events are filtered by their scope, so only a subset will be returned (e.g. 'container.image=ubuntu' will provide only events that have happened on an ubuntu container).
            - event_filter: this is a SysdigMonitor-like filter (e.g. policyEvent.policyId=3). When provided, events are filtered by some of their properties. Currently the supported set of filters is policyEvent.all(which can be used just with matches, policyEvent.policyId, policyEvent.id, policyEvent.severity, policyEvent.ruleTye, policyEvent.ruleSubtype.

        **Success Return Value**
            An array containing:
              - A context object that should be passed to later calls to get_more_policy_events.
              - An array of policy events, in JSON format. See :func:`~sdcclient.SdSecureClient.get_more_policy_events`
                for details on the contents of policy events.

        **Example**
            `examples/get_secure_policy_events.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_secure_policy_events.py>`_

        '''
        options = {"from": int(from_sec) * 1000000,
                   "to": int(to_sec) * 1000000,
                   "offset": 0,
                   "limit": 1000,
                   "sampling": sampling,
                   "aggregations": aggregations,
                   "scopeFilter": scope_filter,
                   "eventFilter": event_filter}
        ctx = {k: v for k, v in options.items() if v is not None}
        return self._get_policy_events_int(ctx)

    def get_policy_events_duration(self, duration_sec, sampling=None, aggregations=None, scope_filter=None,
                                   event_filter=None):
        '''**Description**
            Fetch all policy events that occurred in the last duration_sec seconds. This method is used in conjunction with
            :func:`~sdcclient.SdSecureClient.get_more_policy_events` to provide paginated access to policy events.

        **Arguments**
            - duration_sec: Fetch all policy events that have occurred in the last *duration_sec* seconds.
            - sampling: Sample all policy events using *sampling* interval.
            - aggregations: When present it specifies how to aggregate events (sampling does not need to be specified, because when it's present it automatically means events will be aggregated). This field can either be a list of scope metrics or a list of policyEvents fields but (currently) not a mix of the two. When policy events fields are specified, only these can be used= severity, agentId, containerId, policyId, ruleType.
            - scope_filter: this is a SysdigMonitor-like filter (e.g 'container.image=ubuntu'). When provided, events are filtered by their scope, so only a subset will be returned (e.g. 'container.image=ubuntu' will provide only events that have happened on an ubuntu container).
            - event_filter: this is a SysdigMonitor-like filter (e.g. policyEvent.policyId=3). When provided, events are filtered by some of their properties. Currently the supported set of filters is policyEvent.all(which can be used just with matches, policyEvent.policyId, policyEvent.id, policyEvent.severity, policyEvent.ruleTye, policyEvent.ruleSubtype.

        **Success Return Value**
            An array containing:
              - A context object that should be passed to later calls to get_more_policy_events.
              - An array of policy events, in JSON format. See :func:`~sdcclient.SdSecureClient.get_more_policy_events`
                for details on the contents of policy events.

        **Example**
            `examples/get_secure_policy_events.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_secure_policy_events.py>`_
        '''
        epoch = datetime.datetime.utcfromtimestamp(0)
        to_ts = (datetime.datetime.utcnow() - epoch).total_seconds() * 1000 * 1000
        from_ts = to_ts - (int(duration_sec) * 1000 * 1000)

        options = {"to": to_ts,
                   "from": from_ts,
                   "offset": 0,
                   "limit": 1000,
                   "sampling": sampling,
                   "aggregations": aggregations,
                   "scopeFilter": scope_filter,
                   "eventFilter": event_filter}
        ctx = {k: v for k, v in options.items() if v is not None}
        return self._get_policy_events_int(ctx)

    def get_policy_events_id_range(self, id, from_sec, to_sec, sampling=None, aggregations=None, scope_filter=None,
                                   event_filter=None):
        '''**Description**
            Fetch all policy events with id that occurred in the time range [from_sec:to_sec]. This method is used in conjunction
            with :func:`~sdcclient.SdSecureClient.get_more_policy_events` to provide paginated access to policy events.

        **Arguments**
            - id: the id of the policy events to fetch.
            - from_sec: the start of the timerange for which to get events
            - end_sec: the end of the timerange for which to get events
            - sampling: sample all policy events using *sampling* interval.
            - scope_filter: this is a SysdigMonitor-like filter (e.g 'container.image=ubuntu'). When provided, events are filtered by their scope, so only a subset will be returned (e.g. 'container.image=ubuntu' will provide only events that have happened on an ubuntu container).
            - event_filter: this is a SysdigMonitor-like filter (e.g. policyEvent.policyId=3). When provided, events are filtered by some of their properties. Currently the supported set of filters is policyEvent.all(which can be used just with matches, policyEvent.policyId, policyEvent.id, policyEvent.severity, policyEvent.ruleTye, policyEvent.ruleSubtype.
            - aggregations: When present it specifies how to aggregate events (sampling does not need to be specified, because when it's present it automatically means events will be aggregated). This field can either be a list of scope metrics or a list of policyEvents fields but (currently) not a mix of the two. When policy events fields are specified, only these can be used= severity, agentId, containerId, policyId, ruleType.

        **Success Return Value**
            An array containing:
              - A context object that should be passed to later calls to get_more_policy_events.
              - An array of policy events, in JSON format. See :func:`~sdcclient.SdSecureClient.get_more_policy_events`
                for details on the contents of policy events.

        **Example**
            `examples/get_secure_policy_events.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_secure_policy_events.py>`_
        '''

        options = {"id": id,
                   "from": int(from_sec) * 1000000,
                   "to": int(to_sec) * 1000000,
                   "offset": 0,
                   "limit": 1000,
                   "sampling": sampling,
                   "aggregations": aggregations,
                   "scopeFilter": scope_filter,
                   "eventFilter": event_filter}
        ctx = {k: v for k, v in options.items() if v is not None}
        return self._get_policy_events_int(ctx)

    def get_policy_events_id_duration(self, id, duration_sec, sampling=None, aggregations=None, scope_filter=None,
                                      event_filter=None):
        '''**Description**
            Fetch all policy events with id that occurred in the last duration_sec seconds. This method is used in conjunction with
            :func:`~sdcclient.SdSecureClient.get_more_policy_events` to provide paginated access to policy events.

        **Arguments**
            - id: the id of the policy events to fetch.
            - duration_sec: Fetch all policy events that have occurred in the last *duration_sec* seconds.
            - sampling: Sample all policy events using *sampling* interval.
            - aggregations: When present it specifies how to aggregate events (sampling does not need to be specified, because when it's present it automatically means events will be aggregated). This field can either be a list of scope metrics or a list of policyEvents fields but (currently) not a mix of the two. When policy events fields are specified, only these can be used= severity, agentId, containerId, policyId, ruleType.
            - scope_filter: this is a SysdigMonitor-like filter (e.g 'container.image=ubuntu'). When provided, events are filtered by their scope, so only a subset will be returned (e.g. 'container.image=ubuntu' will provide only events that have happened on an ubuntu container).
            - event_filter: this is a SysdigMonitor-like filter (e.g. policyEvent.policyId=3). When provided, events are filtered by some of their properties. Currently the supported set of filters is policyEvent.all(which can be used just with matches, policyEvent.policyId, policyEvent.id, policyEvent.severity, policyEvent.ruleTye, policyEvent.ruleSubtype.

        **Success Return Value**
            An array containing:
              - A context object that should be passed to later calls to get_more_policy_events.
              - An array of policy events, in JSON format. See :func:`~sdcclient.SdSecureClient.get_more_policy_events`
                for details on the contents of policy events.

        **Example**
            `examples/get_secure_policy_events.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_secure_policy_events.py>`_
        '''
        epoch = datetime.datetime.utcfromtimestamp(0)
        to_ts = (datetime.datetime.utcnow() - epoch).total_seconds() * 1000 * 1000
        from_ts = to_ts - (int(duration_sec) * 1000 * 1000)

        options = {"id": id,
                   "to": to_ts,
                   "from": from_ts,
                   "offset": 0,
                   "limit": 1000,
                   "sampling": sampling,
                   "aggregations": aggregations,
                   "scopeFilter": scope_filter,
                   "eventFilter": event_filter}
        ctx = {k: v for k, v in options.items() if v is not None}
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
