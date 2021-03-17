import json

from sdcclient._common import _SdcCommon


def policy_action_stop():
    return {
        "type": "POLICY_ACTION_STOP",
    }


def policy_action_capture(file_name, secs_before=5, secs_after=15, filter=""):
    return {
        "afterEventNs": secs_after * 1_000_000_000,
        "beforeEventNs": secs_before * 1_000_000_000,
        "isLimitedToContainer": False,
        "type": "POLICY_ACTION_CAPTURE",
        "filter": filter,
        "name": file_name,
        "bucketName": "",
        "storageType": "S3"
    }


def policy_action_pause():
    return {
        "type": "POLICY_ACTION_PAUSE",
    }


def policy_action_kill():
    return {
        "type": "POLICY_ACTION_KILL",
    }


class PolicyClientV2(_SdcCommon):
    def __init__(self, token="", sdc_url='https://secure.sysdig.com', ssl_verify=True, custom_headers=None):
        super(PolicyClientV2, self).__init__(token, sdc_url, ssl_verify, custom_headers)
        self.product = "SDS"

    def create_default_policies(self):
        """
        Create new policies based on the currently available set of rules. For now, this only covers Falco rules, but we might extend
        the endpoint later. The backend should use the defaultPolicies property of a previously provided FalcoRulesFiles model as
        guidance on the set of policies to create. The backend should only create new policies (not delete or modify), and should only
        create new policies if there is not an existing policy with the same name.

        Returns: A touple (bool, res/err) where the first element indicates if the API call was successful and the second the error or the result.

        Examples:
            >>> from sdcclient.secure import PolicyClientV2
            >>> client = PolicyClientV2(sdc_url="https://secure.sysdig.com", token=SECURE_TOKEN)
            >>> ok, res = client.create_default_policies()
        """

        res = self.http.post(self.url + '/api/v2/policies/default', headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def delete_all_policies(self):
        """
        Delete all existing policies.

        Returns: A touple (bool, res/err) where the first element indicates if the API call was successful and the second the error or the result.

        Examples:
            >>> from sdcclient.secure import PolicyClientV2
            >>> client = PolicyClientV2(sdc_url="https://secure.sysdig.com", token=SECURE_TOKEN)
            >>> ok, res = client.delete_all_policies()
        """

        ok, res = self.list_policies()
        if not ok:
            return False, res

        for policy in res:
            ok, res = self.delete_policy_id(policy["id"])
            if not ok:
                return False, res

        return True, "Policies Deleted"

    def list_policies(self):
        """
        List the current set of policies.

        Returns: A touple (bool, res/err) where the first element indicates if the API call was successful and the second the error or the result.

        Examples:
            >>> from sdcclient.secure import PolicyClientV2
            >>> client = PolicyClientV2(sdc_url="https://secure.sysdig.com", token=SECURE_TOKEN)
            >>> ok, res = client.list_policies()
        """

        res = self.http.get(self.url + '/api/v2/policies', headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def get_policy(self, name):
        """
        Find the policy with name <name> and return its json description.

        Args:
            name(str): The name of the policy to fetch

        Returns: A touple (bool, res/err) where the first element indicates if the API call was successful and the
        second the error or the JSON object containing the policy.

        Examples:
            >>> import json
            >>> from sdcclient.secure import PolicyClientV2
            >>> client = PolicyClientV2(sdc_url="https://secure.sysdig.com", token=SECURE_TOKEN)
            >>> ok, res = client.get_policy(name="Terminal shell in container")
            >>> if ok:
            >>>     print((json.dumps(res, indent=2)))
        """

        ok, res = self.list_policies()
        if not ok:
            return [False, res]
        policies = res

        # Find the policy with the given name and return it.
        for policy in policies:
            if policy["name"] == name:
                return [True, policy]

        return [False, "No policy with name {}".format(name)]

    def get_policy_id(self, id):
        """
        Find the policy with id <id> and return its json description.

        Args:
            id(int): The id of the policy to fetch

        Returns: A touple (bool, res/err) where the first element indicates if the API call was successful and the
        second the error or the JSON object containing the policy.

        Examples:
            >>> import json
            >>> from sdcclient.secure import PolicyClientV2
            >>> client = PolicyClientV2(sdc_url="https://secure.sysdig.com", token=SECURE_TOKEN)
            >>> ok, res = client.get_policy_id(id=123456)
            >>> if ok:
            >>>     print((json.dumps(res, indent=2)))
        """

        res = self.http.get(self.url + '/api/v2/policies/{}'.format(id), headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def add_policy(self, name, description, rule_names=[], actions=[], scope=None, severity=0, enabled=True,
                   notification_channels=[], type="falco"):
        """
        Adds a new policy.

        Args:
            name(str): A short name for the policy
            description(str): Description of policy
            rule_names(list): Array of rule names. (They must be names instead of ids, as the rules list view is by name, to account for multiple rules having the same name).
            actions(list): It can be a `policy_action_stop()`, `policy_action_pause()`, `policy_action_capture()` or `policy_action_kill()` action
            scope(str): Where the policy is being applied- Container, Host etc.. (example: "container.image.repository = sysdig/agent")
            severity(int): True if the policy should be considered
            enabled(bool): How severe is this policy when violated. Range from 0 to 7 included.
            notification_channels(list): ids of the notification channels to subscribe to the policy
            type(str): Type of the Policy. It can be one of: `falco`, `list_matching`, `k8s_audit`.

        Returns: A touple (bool, res/err) where the first element indicates if the API call was successful and the second the error or the result.

        Examples:
            >>> from sdcclient.secure import PolicyClientV2, policy_action_stop
            >>> client = PolicyClientV2(sdc_url="https://secure.sysdig.com", token=SECURE_TOKEN)
            >>> ok, res = client.add_policy(name="Terminal shell in container",
                                            description="A shell was spawned by a program in a container with an attached terminal.",
                                            rule_names=["Terminal shell in container"],
                                            actions=[policy_action_stop()],
                                            type="falco")
        """

        policy = {
            "name": name,
            "description": description,
            "ruleNames": rule_names,
            "actions": actions,
            "scope": scope,
            "severity": severity,
            "enabled": enabled,
            "notificationChannelIds": notification_channels,
            "type": type,
        }

        res = self.http.post(self.url + '/api/v2/policies', headers=self.hdrs, data=json.dumps(policy),
                             verify=self.ssl_verify)
        return self._request_result(res)

    def add_policy_json(self, policy_json):
        """
        Add a new policy using the provided json.

        Args:
            policy_json: a description of the new policy

        Returns: A touple (bool, res/err) where the first element indicates if the API call was successful and the second the error or the result.

        Examples:
            >>> import sys
            >>> from sdcclient.secure import PolicyClientV2
            >>> client = PolicyClientV2(sdc_url="https://secure.sysdig.com", token=SECURE_TOKEN)
            >>> policy_json = sys.stdin.read()
            >>> ok, res = client.add_policy_json(policy_json)

        """

        try:
            policy_obj = json.loads(policy_json)
            if "origin" in policy_obj:
                del policy_obj["origin"]
        except Exception as e:
            return [False, "policy json is not valid json: {}".format(str(e))]

        res = self.http.post(self.url + '/api/v2/policies', headers=self.hdrs, data=json.dumps(policy_obj),
                             verify=self.ssl_verify)
        return self._request_result(res)

    def update_policy(self, id, name=None, description=None, rule_names=None, actions=None, scope=None,
                      severity=None, enabled=None, notification_channels=None):
        """
        Update policy with the provided values. Only the defined values will be updated.

        Args:
            id(int): The id of the policy to update
            name(str): A short name for the policy
            description(str): Description of policy
            rule_names(list): Array of rule names. (They must be names instead of ids, as the rules list view is by name, to account for multiple rules having the same name).
            actions(list): It can be a `policy_action_stop()`, `policy_action_pause()`, `policy_action_capture()` or `policy_action_kill()` action
            scope(str): Where the policy is being applied- Container, Host etc.. (example: "container.image.repository = sysdig/agent")
            severity(int): True if the policy should be considered
            enabled(bool): How severe is this policy when violated. Range from 0 to 7 included.
            notification_channels(list): ids of the notification channels to subscribe to the policy

        Returns: A touple (bool, res/err) where the first element indicates if the API call was successful and the second the error or the result.

        Examples:
            >>> from sdcclient.secure import PolicyClientV2, policy_action_stop
            >>> client = PolicyClientV2(sdc_url="https://secure.sysdig.com", token=SECURE_TOKEN)
            >>> ok, res = client.update_policy(name="Terminal shell in container",
                                               description="A shell was spawned by a program in a container with an attached terminal.",
                                               rule_names=["Terminal shell in container"],
                                               actions=[policy_action_stop()])
        """

        ok, res = self.get_policy_id(id)
        if not ok:
            return [False, res]
        policy = res

        if name is not None:
            policy["name"] = name
        if description is not None:
            policy["description"] = description
        if rule_names is not None:
            policy["ruleNames"] = rule_names
        if actions is not None:
            policy["actions"] = actions
        if scope is not None:
            policy["scope"] = scope
        if severity is not None:
            policy["severity"] = severity
        if enabled is not None:
            policy["enabled"] = enabled
        if notification_channels is not None:
            policy["notificationChannelIds"] = notification_channels

        res = self.http.put(self.url + '/api/v2/policies/{}'.format(id), headers=self.hdrs, data=json.dumps(policy),
                            verify=self.ssl_verify)
        return self._request_result(res)

    def update_policy_json(self, policy_json):
        """
        Update an existing policy using the provided json. The 'id' field from the policy is
        used to determine which policy to update.

        Args:
            policy_json(str): A description of the new policy

        Returns: A touple (bool, res/err) where the first element indicates if the API call was successful and the second the error or the result.

        Examples:
            >>> import sys
            >>> from sdcclient.secure import PolicyClientV2
            >>> client = PolicyClientV2(sdc_url="https://secure.sysdig.com", token=SECURE_TOKEN)
            >>> policy_json = sys.stdin.read()
            >>> ok, res = client.update_policy_json(policy_json)
        """

        try:
            policy_obj = json.loads(policy_json)
            if "origin" in policy_obj:
                del policy_obj["origin"]
        except Exception as e:
            return [False, "policy json is not valid json: {}".format(str(e))]

        if "id" not in policy_obj:
            return [False, "Policy Json does not have an 'id' field"]

        res = self.http.put(self.url + '/api/v2/policies/{}'.format(policy_obj["id"]), headers=self.hdrs,
                            data=json.dumps(policy_obj), verify=self.ssl_verify)
        return self._request_result(res)

    def delete_policy_name(self, name):
        """
        Delete the policy with the given name.

        Args:
            name(str): The name of the policy to delete

        Returns: A touple (bool, res/err) where the first element indicates if the API call was successful and the second the error or the JSON object representing the now-deleted policy.

        Examples:
            >>> from sdcclient.secure import PolicyClientV2
            >>> client = PolicyClientV2(sdc_url="https://secure.sysdig.com", token=SECURE_TOKEN)
            >>> ok, res = client.delete_policy_name(name="Terminal shell in container")
        """

        ok, res = self.list_policies()
        if not ok:
            return [False, res]

        # Find the policy with the given name and delete it
        for policy in res:
            if policy["name"] == name:
                return self.delete_policy_id(policy["id"])

        return [False, "No policy with name {}".format(name)]

    def delete_policy_id(self, id):
        """
        Delete the policy with the given name.

        Args:
            id(int): The id of the policy to delete

        Returns: A touple (bool, res/err) where the first element indicates if the API call was successful and the second the error or the JSON object representing the now-deleted policy.

        Examples:
            >>> from sdcclient.secure import PolicyClientV2
            >>> client = PolicyClientV2(sdc_url="https://secure.sysdig.com", token=SECURE_TOKEN)
            >>> ok, res = client.delete_policy_id(id=123456)
        """

        res = self.http.delete(self.url + '/api/v2/policies/{}'.format(id), headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)
