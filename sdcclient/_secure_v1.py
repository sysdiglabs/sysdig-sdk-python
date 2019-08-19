import json
import requests

from sdcclient._secure import SdSecureClient


class SdSecureClientV1(SdSecureClient):
    '''**Description**
        Handles policies version 1 (ie. up to August 2019). For later Sysdig Secure versions, please use :class:`~SdSecureClient` instead.
    '''

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
        '''
        res = requests.post(self.url + '/api/policies/createDefault', headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def delete_all_policies(self):
        '''**Description**
            Delete all existing policies. The falco rules file is unchanged.

        **Arguments**
            - None

        **Success Return Value**
            The string "Policies Deleted"
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
        '''
        res = requests.get(self.url + '/api/policies', headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def get_policy_priorities(self):
        '''**Description**
            Get a list of policy ids in the order they will be evaluated.

        **Arguments**
            - None

        **Success Return Value**
            A JSON object representing the list of policy ids.
        '''

        res = requests.get(self.url + '/api/policies/priorities', headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def set_policy_priorities(self, priorities_json):
        '''**Description**
            Change the policy evaluation order

        **Arguments**
            - priorities_json: a description of the new policy order.

        **Success Return Value**
            A JSON object representing the updated list of policy ids.
        '''

        try:
            json.loads(priorities_json)
        except Exception as e:
            return [False, "priorities json is not valid json: {}".format(str(e))]

        res = requests.put(self.url + '/api/policies/priorities', headers=self.hdrs, data=priorities_json, verify=self.ssl_verify)
        return self._request_result(res)

    def get_policy(self, name):
        '''**Description**
            Find the policy with name <name> and return its json description.

        **Arguments**
            - name: the name of the policy to fetch

        **Success Return Value**
            A JSON object containing the description of the policy. If there is no policy with
            the given name, returns False.
        '''
        ok, res = self.list_policies()
        if not ok:
            return [False, res]

        policies = res["policies"]

        # Find the policy with the given name and return it.
        for policy in policies:
            if policy["name"] == name:
                return [True, policy]

        return [False, "No policy with name {}".format(name)]

    def get_policy_id(self, id):
        '''**Description**
            Find the policy with id <id> and return its json description.

        **Arguments**
            - id: the id of the policy to fetch

        **Success Return Value**
            A JSON object containing the description of the policy. If there is no policy with
            the given name, returns False.
        '''
        res = requests.get(self.url + '/api/policies/{}'.format(id), headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def add_policy(self, policy_json):
        '''**Description**
            Add a new policy using the provided json.

        **Arguments**
            - policy_json: a description of the new policy

        **Success Return Value**
            The string "OK"
        '''
        try:
            policy_obj = json.loads(policy_json)
        except Exception as e:
            return [False, "policy json is not valid json: {}".format(str(e))]

        body = {"policy": policy_obj}
        res = requests.post(self.url + '/api/policies', headers=self.hdrs, data=json.dumps(body), verify=self.ssl_verify)
        return self._request_result(res)

    def update_policy(self, policy_json):
        '''**Description**
            Update an existing policy using the provided json. The 'id' field from the policy is
            used to determine which policy to update.

        **Arguments**
            - policy_json: a description of the new policy

        **Success Return Value**
            The string "OK"
        '''

        try:
            policy_obj = json.loads(policy_json)
        except Exception as e:
            return [False, "policy json is not valid json: {}".format(str(e))]

        if "id" not in policy_obj:
            return [False, "Policy Json does not have an 'id' field"]

        body = {"policy": policy_obj}

        res = requests.put(self.url + '/api/policies/{}'.format(policy_obj["id"]), headers=self.hdrs, data=json.dumps(body), verify=self.ssl_verify)
        return self._request_result(res)

    def delete_policy_name(self, name):
        '''**Description**
            Delete the policy with the given name.

        **Arguments**
            - name: the name of the policy to delete

        **Success Return Value**
            The JSON object representing the now-deleted policy.
        '''
        ok, res = self.list_policies()
        if not ok:
            return [False, res]

        # Find the policy with the given name and delete it
        for policy in res["policies"]:
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
        '''
        res = requests.delete(self.url + '/api/policies/{}'.format(id), headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)
