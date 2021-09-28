import json

from sdcclient._common import _SdcCommon


class ScanningAlertsClientV1(_SdcCommon):
    def __init__(self, token="", sdc_url='https://secure.sysdig.com', ssl_verify=True, custom_headers=None):
        super(ScanningAlertsClientV1, self).__init__(token, sdc_url, ssl_verify, custom_headers)
        self.product = "SDS"

    class RepositoryAlertTrigger:
        @staticmethod
        def new_image_analyzed(alert):
            alert["triggers"]["analysis_update"] = True

        @staticmethod
        def scan_result_change_fail(alert):
            alert["triggers"]["policy_eval"] = True
            alert["onlyPassFail"] = True

        @staticmethod
        def scan_result_change_any(alert):
            alert["triggers"]["policy_eval"] = True
            alert["onlyPassFail"] = False

        @staticmethod
        def cve_update(alert):
            alert["triggers"]["vuln_update"] = True

    def add_repository_alert(self, name, registry, repository, tag, description="", triggers=None, notification_channels=None, enabled=True):
        '''
        Create a new repository alert

        Args:
            name(str): The name of the alert.
            registry(str): Registry to alert (e.g. docker.io)
            repository(str): Repository to alert (e.g. sysdig/agent)
            tag(str): Tag to alert (e.g. latest)
            description(str): The description of the alert.
            triggers(list): A list of RepositoryAlertTrigger indicating which triggers should be enabled. (default: [ScanningAlertsClientV1.RuntimeAlertTrigger.new_image_analyzed])
            notification_channels(list): A list of notification channel ids.
            enabled(bool): Whether this alert should actually be applied. Defaults to true.
        Returns:
            The created alert.
        '''
        if not triggers:
            triggers = [ScanningAlertsClientV1.RepositoryAlertTrigger.new_image_analyzed]

        alert = {
                'name':                   name,
                'description':            description,
                'type':                   'repository',
                'triggers':               {
                        "unscanned":       False,
                        "analysis_update": False,
                        "vuln_update":     False,
                        "policy_eval":     False,
                        "failed":          False
                },
                'repositories':           [{
                        'registry':   registry,
                        'repository': repository,
                        'tag':        tag,
                }],
                "onlyPassFail":           False,
                "skipEventSend":          False,
                'enabled':                enabled,
                'notificationChannelIds': notification_channels,
        }

        for trigger in triggers:
            trigger(alert)

        res = self.http.post(f"{self.url}/api/scanning/v1/alerts", headers=self.hdrs, data=json.dumps(alert), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def update_repository_alert(self, id, name=None, registry=None, repository=None, tag=None, description=None, triggers=None, notification_channels=None, enabled=None):
        '''
        Updates a repository alert

        Args:
            id(str): Alert ID.
            name(str): The name of the alert.
            registry(str): Registry to alert (e.g. docker.io)
            repository(str): Repository to alert (e.g. sysdig/agent)
            tag(str): Tag to alert (e.g. latest)
            description(str): The description of the alert.
            triggers(list): A list of RepositoryAlertTrigger indicating which triggers should be enabled. (default: [ScanningAlertsClientV1.RuntimeAlertTrigger.unscanned_image])
            notification_channels(list): A list of notification channel ids.
            enabled(bool): Whether this alert should actually be applied. Defaults to true.
        Returns:
            The updated alert.
        '''
        ok, alert = self.get_alert(id)
        if not ok:
            return False, f"unable to retrieve alert by ID {id}: {alert}"

        if name is not None:
            alert["name"] = name
        if description is not None:
            alert["description"] = description
        if registry is not None:
            alert["repositories"][0]["registry"] = registry
        if repository is not None:
            alert["repositories"][0]["repository"] = repository
        if tag is not None:
            alert["repositories"][0]["tag"] = tag
        if triggers is not None:
            alert["triggers"] = {
                    "unscanned":       False,
                    "analysis_update": False,
                    "vuln_update":     False,
                    "policy_eval":     False,
                    "failed":          False
            }
            alert["onlyPassFail"] = False
            for trigger in triggers:
                trigger(alert)
        if notification_channels is not None:
            alert["notificationChannelIds"] = notification_channels
        if enabled is not None:
            alert["enabled"] = enabled

        res = self.http.put(f"{self.url}/api/scanning/v1/alerts/{id}", headers=self.hdrs, data=json.dumps(alert), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    class RuntimeAlertTrigger:
        @staticmethod
        def unscanned_image(alert):
            alert["triggers"]["unscanned"] = True

        @staticmethod
        def scan_result_change_fail(alert):
            alert["triggers"]["policy_eval"] = True
            alert["onlyPassFail"] = True

        @staticmethod
        def scan_result_change_any(alert):
            alert["triggers"]["policy_eval"] = True
            alert["onlyPassFail"] = False

        @staticmethod
        def cve_update(alert):
            alert["triggers"]["vuln_update"] = True

    def add_runtime_alert(self, name, description="", scope="", triggers=None, notification_channels=None, enabled=True):
        '''
        Create a new runtime alert

        Args:
            name(str): The name of the alert.
            description(str): The description of the alert.
            scope(str): An AND-composed string of predicates that selects the scope in which the alert will be applied. (like: 'host.domain = "example.com" and container.image != "alpine:latest"')
            triggers(list): A list of RuntimeAlertTrigger indicating which triggers should be enabled. (default: [ScanningAlertsClientV1.RuntimeAlertTrigger.unscanned_image])
            notification_channels(list): A list of notification channel ids.
            enabled(bool): Whether this alert should actually be applied. Defaults to true.
        Returns:
            The created alert.
        '''
        if not triggers:
            triggers = [ScanningAlertsClientV1.RuntimeAlertTrigger.unscanned_image]

        alert = {
                'name':                   name,
                'description':            description,
                'type':                   'runtime',
                'triggers':               {
                        "unscanned":       False,
                        "analysis_update": False,
                        "vuln_update":     False,
                        "policy_eval":     False,
                        "failed":          False
                },
                'scope':                  scope,
                "onlyPassFail":           False,
                "skipEventSend":          False,
                'enabled':                enabled,
                'notificationChannelIds': notification_channels,
        }

        for trigger in triggers:
            trigger(alert)

        res = self.http.post(f"{self.url}/api/scanning/v1/alerts", headers=self.hdrs, data=json.dumps(alert), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def update_runtime_alert(self, id, name=None, description=None, scope=None, triggers=None, notification_channels=None, enabled=None):
        '''
        Updates a runtime alert

        Args:
            id(str): Alert ID.
            name(str): The name of the alert.
            description(str): The description of the alert.
            scope(str): An AND-composed string of predicates that selects the scope in which the alert will be applied. (like: 'host.domain = "example.com" and container.image != "alpine:latest"')
            triggers(list): A list of RuntimeAlertTrigger indicating which triggers should be enabled. (default: [ScanningAlertsClientV1.RuntimeAlertTrigger.unscanned_image])
            notification_channels(list): A list of notification channel ids.
            enabled(bool): Whether this alert should actually be applied. Defaults to true.
        Returns:
            The updated alert.
        '''
        ok, alert = self.get_alert(id)
        if not ok:
            return False, f"unable to retrieve alert by ID {id}: {alert}"

        if name is not None:
            alert["name"] = name
        if description is not None:
            alert["description"] = description
        if scope is not None:
            alert["scope"] = scope
        if triggers is not None:
            alert["triggers"] = {
                    "unscanned":       False,
                    "analysis_update": False,
                    "vuln_update":     False,
                    "policy_eval":     False,
                    "failed":          False
            }
            alert["onlyPassFail"] = False
            for trigger in triggers:
                trigger(alert)
        if notification_channels is not None:
            alert["notificationChannelIds"] = notification_channels
        if enabled is not None:
            alert["enabled"] = enabled

        res = self.http.put(f"{self.url}/api/scanning/v1/alerts/{id}", headers=self.hdrs, data=json.dumps(alert), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def get_alert(self, alertid):
        '''
        Retrieve the scanning alert with the given id

        Args:
            alertid: Unique identifier associated with this alert.

        Returns:
            A JSON object containing the alert description.
        '''

        res = self.http.get(f"{self.url}/api/scanning/v1/alerts/{alertid}", headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def list_alerts(self, limit=None, cursor=None):
        '''
        List the current set of scanning alerts.
        Args:
            limit(int): Maximum number of alerts in the response.
            cursor: An opaque string representing the current position in the list of alerts. It's provided in the 'responseMetadata' of the list_alerts response.

        Returns:
            A JSON containing the list of alerts in the 'alerts' field, and the current cursor position in the 'responseMetadata' field.
        '''

        url = f"{self.url}/api/scanning/v1/alerts"
        if limit:
            url += '?limit=' + str(limit)
            if cursor:
                url += '&cursor=' + cursor

        res = self.http.get(url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def delete_alert(self, policyid):  # FIXME: policyid must be maintained for backwards compatibility reasons with older versions, but should be renamed to id or alert_id
        '''
        Delete the alert with the given id

        Args:
            policyid:  Unique identifier associated with this alert.
        '''

        res = self.http.delete(f"{self.url}/api/scanning/v1/alerts/{policyid}", headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.text]
