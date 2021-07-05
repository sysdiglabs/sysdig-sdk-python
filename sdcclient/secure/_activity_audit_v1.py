import datetime

from sdcclient._common import _SdcCommon


class ActivityAuditDataSource:
    CMD = "command"
    NET = "connection"
    KUBE_EXEC = "kubernetes"
    FILE = "fileaccess"


_seconds_to_nanoseconds = 10 ** 9


class ActivityAuditClientV1(_SdcCommon):
    def __init__(self, token="", sdc_url='https://secure.sysdig.com', ssl_verify=True, custom_headers=None):
        super(ActivityAuditClientV1, self).__init__(token, sdc_url, ssl_verify, custom_headers)
        self.product = "SDS"

    def list_events(self, from_date=None, to_date=None, scope_filter=None, limit=0,
                    data_sources=None):
        """
        List the events in the Activity Audit.

        Args:
            from_date (datetime.datetime): the start of the time range from which to get events. The default value is yesterday.
            to_date (datetime.datetime): the end of the time range from which to get events. The default value is now.
            scope_filter (List): a list of Sysdig Monitor-like filter (e.g `processName in ("ubuntu")`).
            limit (int): max number of events to retrieve. A limit of 0 or negative will retrieve all events.
            data_sources (List): a list of data sources to retrieve events from. None or an empty list retrieves all events.

        Examples:
            >>> client = ActivityAuditClientV1(token=SECURE_TOKEN)
            >>>
            >>> now = datetime.datetime.utcnow()
            >>> three_days_ago = now - datetime.timedelta(days=3)
            >>> max_event_number_retrieved = 50
            >>> data_sources = [ActivityAuditDataSource.CMD, ActivityAuditDataSource.KUBE_EXEC]
            >>>
            >>> ok, events = client.list_events(from_date=three_days_ago,
            >>>                                 to_date=now,
            >>>                                 limit=max_event_number_retrieved,
            >>>                                 data_sources=data_sources)

        Returns:
            A list of event objects from the Activity Audit.
        """
        number_of_events_per_query = 50

        if from_date is None:
            from_date = datetime.datetime.utcnow() - datetime.timedelta(days=1)
        if to_date is None:
            to_date = datetime.datetime.utcnow()

        filters = scope_filter if scope_filter else []
        if data_sources:
            quoted_data_sources = [f'"{data_source}"' for data_source in data_sources]
            data_source_filter = f'type in ({",".join(quoted_data_sources)})'
            filters.append(data_source_filter)

        query_params = {
            "from": int(from_date.timestamp()) * _seconds_to_nanoseconds,
            "to": int(to_date.timestamp()) * _seconds_to_nanoseconds,
            "limit": number_of_events_per_query,
            "filter": " and ".join(filters),
        }

        res = self.http.get(self.url + '/api/v1/activityAudit/events', headers=self.hdrs, verify=self.ssl_verify,
                            params=query_params)
        ok, res = self._request_result(res)
        if not ok:
            return False, res

        events = []

        # Pagination required by Secure API
        while "page" in res and \
                "total" in res["page"] and \
                res["page"]["total"] > number_of_events_per_query:
            events = events + res["data"]

            if 0 < limit < len(events):
                events = events[0:limit - 1]
                break

            paginated_query_params = {
                "limit": number_of_events_per_query,
                "filter": " and ".join(filters),
                "cursor": res["page"]["prev"]
            }

            res = self.http.get(self.url + '/api/v1/activityAudit/events', headers=self.hdrs, verify=self.ssl_verify,
                                params=paginated_query_params)
            ok, res = self._request_result(res)
            if not ok:
                return False, res
        else:
            events = events + res["data"]

        return True, events

    def list_trace(self, traceable_event):
        """
        Lists the events from an original traceable event.

        Args:
            traceable_event(object): an event retrieved from the list_events method. The event must be traceable,
                                     this is, it must have the "traceable" key as true.

        Examples:
            >>> client = ActivityAuditClientV1(token=SECURE_TOKEN)
            >>>
            >>> ok, events = client.list_events()
            >>> if not ok:
            >>>     return
            >>> traceable_events = [event for event in events if event["traceable"]]
            >>>
            >>> ok, trace = client.list_trace(traceable_events[0])
            >>> if not ok:
            >>>     return
            >>>
            >>> for event in trace:
            >>>     print(event)

        Returns:
            All the related events that are the trace of the given event.
        """
        if not traceable_event or not traceable_event["traceable"]:
            return False, "a traceable event must be provided"

        endpoint = f'/api/v1/activityAudit/events/{traceable_event["type"]}/{traceable_event["id"]}/trace'
        res = self.http.get(self.url + endpoint, headers=self.hdrs, verify=self.ssl_verify)
        ok, res = self._request_result(res)
        if not ok:
            return False, res
        return True, res["data"]
