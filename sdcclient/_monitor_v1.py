from sdcclient._monitor import SdMonitorClient

try:
    basestring
except NameError:
    basestring = str


class SdMonitorClientV1(SdMonitorClient):
    '''**Description**
        Handles dashboards version 1 (ie. up to February 2019). For later Sysdig Monitor versions, please use :class:`~SdMonitorClient` instead.
    '''

    def __init__(self, token="", sdc_url='https://app.sysdigcloud.com', ssl_verify=True):
        super(SdMonitorClientV1, self).__init__(token, sdc_url, ssl_verify)
        self._dashboards_api_endpoint = '/ui/dashboards'
        self._default_dashboards_api_endpoint = '/api/defaultDashboards'
