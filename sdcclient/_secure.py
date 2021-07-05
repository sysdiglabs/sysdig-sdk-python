import json
import time

from sdcclient._common import _SdcCommon
from sdcclient.secure import FalcoRulesFilesClientOld, PolicyEventsClientV1, PolicyEventsClientOld, PolicyClientV2


class SdSecureClient(FalcoRulesFilesClientOld,
                     PolicyEventsClientV1,
                     PolicyEventsClientOld,
                     PolicyClientV2,
                     _SdcCommon):
    def __init__(self, token="", sdc_url='https://secure.sysdig.com', ssl_verify=True, custom_headers=None):
        super(SdSecureClient, self).__init__(token, sdc_url, ssl_verify, custom_headers)

        self.product = "SDS"
        self._policy_v2 = None

    @property
    def policy_v2(self):
        '''**Description**
            True if policy V2 API is available
        '''
        if self._policy_v2 is None:
            res = self.http.get(self.url + '/api/v2/policies/default', headers=self.hdrs, verify=self.ssl_verify)
            self._policy_v2 = res.status_code != 404
        return self._policy_v2

    def list_rules(self):
        '''**Description**
            Returns the list of rules in the system. These are grouped by name
            and do not necessarily represent individual rule objects, as multiple
            rules can have the same name.

        **Arguments**
            - None

        **Success Return Value**
            A JSON object representing the list of rules.
        '''
        res = self.http.get(self.url + '/api/secure/rules/summaries', headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def get_rules_group(self, name):
        '''**Description**
            Retrieve a group of all rules having the given name. This is used to
            show how a base rule is modified by later rules that override/append
            to the rule.

        **Arguments**
            - name: the name of the rule group

        **Success Return Value**
            A JSON object representing the list of rules.
        '''
        res = self.http.get(self.url + '/api/secure/rules/groups?name={}'.format(name), headers=self.hdrs,
                            verify=self.ssl_verify)
        return self._request_result(res)

    def get_rule_id(self, id):
        '''**Description**
            Retrieve info about a single rule

        **Arguments**
            - id: the id of the rule

        **Success Return Value**
            A JSON object representing the rule.
        '''
        res = self.http.get(self.url + '/api/secure/rules/{}'.format(id), headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def add_rule(self, name, details={}, description="", tags=[]):
        '''**Description**
            Create a new rule

        **Arguments**
            - name: A name for this object. Should exactly be the value of the "rule" property of the yaml object.
            - details: The rule description as a python dictionary.
            - description: A description of this rule. No newlines/formatting.
            - tags: The set of tags.

        **Success Return Value**
            A JSON object representing the rule.
        '''
        rule = {
            "name": name,
            "description": description,
            "details": details,
            "tags": tags
        }
        res = self.http.post(self.url + '/api/secure/rules', data=json.dumps(rule), headers=self.hdrs,
                             verify=self.ssl_verify)
        return self._request_result(res)

    def update_rule(self, id, details={}, description="", tags=[]):
        '''**Description**
            Update info associated with a rule

        **Arguments**
            - id: The rule id
            - details: The rule description as a python dictionary.
            - description: A description of this rule. No newlines/formatting.
            - tags: The set of tags.

        **Success Return Value**
            A JSON object representing the rule.
        '''
        ok, res = self.get_rule_id(id)
        if not ok:
            return [False, res]
        rule = res

        if details:
            rule['details'] = details
        if description:
            rule['description'] = description
        if tags:
            rule['tags'] = tags
        res = self.http.put(self.url + '/api/secure/rules/{}'.format(id), data=json.dumps(rule), headers=self.hdrs,
                            verify=self.ssl_verify)
        return self._request_result(res)

    def delete_rule(self, id):
        '''**Description**
            Delete the rule with given id.

        **Arguments**
            - id: The rule id

        **Success Return Value**
            A JSON object representing the rule.
        '''
        res = self.http.delete(self.url + '/api/secure/rules/{}'.format(id), headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def list_falco_macros(self):
        '''**Description**
            Returns the list of macros in the system. These are grouped by name
            and do not necessarily represent individual macro objects, as multiple
            macros can have the same name.

        **Arguments**
            - None

        **Success Return Value**
            A JSON object representing the list of falco macros.
        '''
        res = self.http.get(self.url + '/api/secure/falco/macros/summaries', headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def get_falco_macros_group(self, name):
        '''**Description**
            Retrieve a group of all falco groups having the given name. This is used
            to show how a base macro is modified by later macrosthat override/append
            to the macro.

        **Arguments**
            - name: the name of the falco macros group

        **Success Return Value**
            A JSON object representing the list of falco macros.
        '''
        res = self.http.get(self.url + '/api/secure/falco/macros/groups?name={}'.format(name), headers=self.hdrs,
                            verify=self.ssl_verify)
        return self._request_result(res)

    def get_falco_macro_id(self, id):
        '''**Description**
            Retrieve info about a single falco macro

        **Arguments**
            - id: the id of the falco macro

        **Success Return Value**
            A JSON object representing the falco macro.
        '''
        res = self.http.get(self.url + '/api/secure/falco/macros/{}'.format(id), headers=self.hdrs,
                            verify=self.ssl_verify)
        return self._request_result(res)

    def add_falco_macro(self, name, condition, append=False):
        '''**Description**
            Create a new macro

        **Arguments**
            - name: A name for this object. Should exactly be the value of the "macro" property of the yaml object.
            - condition: the full condition text exactly as represented in the yaml file.

        **Success Return Value**
            A JSON object representing the falco macro.
        '''
        macro = {
            "name": name,
            "condition": {
                "components": [],
                "condition": condition
            },
            "append": append
        }
        res = self.http.post(self.url + '/api/secure/falco/macros', data=json.dumps(macro), headers=self.hdrs,
                             verify=self.ssl_verify)
        return self._request_result(res)

    def update_falco_macro(self, id, condition):
        '''**Description**
            Update info associated with a macro

        **Arguments**
            - id: The rule id
            - condition: the full condition text exactly as represented in the yaml file.

        **Success Return Value**
            A JSON object representing the macro.
        '''
        ok, res = self.get_falco_macro_id(id)
        if not ok:
            return [False, res]
        macro = res
        macro['condition']['condition'] = condition

        res = self.http.put(self.url + '/api/secure/falco/macros/{}'.format(id), data=json.dumps(macro),
                            headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def delete_falco_macro(self, id):
        '''**Description**
            Delete the macro with given id.

        **Arguments**
            - id: The macro id

        **Success Return Value**
            A JSON object representing the macro.
        '''
        res = self.http.delete(self.url + '/api/secure/falco/macros/{}'.format(id), headers=self.hdrs,
                               verify=self.ssl_verify)
        return self._request_result(res)

    def list_falco_lists(self):
        '''**Description**
            Returns the list of falco lists in the system. These are grouped by
            name and do not necessarily represent individual falco list objects,
            as multiple falco lists can have the same name.

        **Arguments**
            - None

        **Success Return Value**
            A JSON object representing the list of falco lists.
        '''
        res = self.http.get(self.url + '/api/secure/falco/lists/summaries', headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def get_falco_lists_group(self, name):
        '''**Description**
            Retrieve a group of all falco lists having the given name. This is used
            to show how a base list is modified by later lists that override/append
            to the list.

        **Arguments**
            - name: the name of the falco lists group

        **Success Return Value**
            A JSON object representing the list of falco lists.
        '''
        res = self.http.get(self.url + '/api/secure/falco/lists/groups?name={}'.format(name), headers=self.hdrs,
                            verify=self.ssl_verify)
        return self._request_result(res)

    def get_falco_list_id(self, id):
        '''**Description**
            Retrieve info about a single falco list

        **Arguments**
            - id: the id of the falco list

        **Success Return Value**
            A JSON object representing the falco list.
        '''
        res = self.http.get(self.url + '/api/secure/falco/lists/{}'.format(id), headers=self.hdrs,
                            verify=self.ssl_verify)
        return self._request_result(res)

    def add_falco_list(self, name, items, append=False):
        '''**Description**
            Create a new list

        **Arguments**
            - name: A name for this object. Should exactly be the value of the "list" property of the yaml object.
            - items: the array of items as represented in the yaml List.

        **Success Return Value**
            A JSON object representing the falco list.
        '''
        flist = {
            "name": name,
            "items": {
                "items": items
            },
            "append": append
        }
        res = self.http.post(self.url + '/api/secure/falco/lists', data=json.dumps(flist), headers=self.hdrs,
                             verify=self.ssl_verify)
        return self._request_result(res)

    def update_falco_list(self, id, items):
        '''**Description**
            Update info associated with a list

        **Arguments**
            - id: The rule id
            - items: the array of items as represented in the yaml List.

        **Success Return Value**
            A JSON object representing the list.
        '''
        ok, res = self.get_falco_list_id(id)
        if not ok:
            return [False, res]
        flist = res
        flist['items']['items'] = items

        res = self.http.put(self.url + '/api/secure/falco/lists/{}'.format(id), data=json.dumps(flist),
                            headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def delete_falco_list(self, id):
        '''**Description**
            Delete the list with given id.

        **Arguments**
            - id: The list id

        **Success Return Value**
            A JSON object representing the list.
        '''
        res = self.http.delete(self.url + '/api/secure/falco/lists/{}'.format(id), headers=self.hdrs,
                               verify=self.ssl_verify)
        return self._request_result(res)

    def add_compliance_task(self, name, module_name='docker-bench-security', schedule='06:00:00Z/PT12H', scope=None,
                            enabled=True):
        '''**Description**
            Add a new compliance task.

        **Arguments**
            - name: The name of the task e.g. 'Check Docker Compliance'.
            - module_name: The name of the module that implements this task. Separate from task name in case you want to use the same module to run separate tasks with different scopes or schedules. [ 'docker-bench-security', 'kube-bench' ]
            - schedule: The frequency at which this task should run. Expressed as an `ISO 8601 Duration <https://en.wikipedia.org/wiki/ISO_8601#Durations>`_
            - scope: The agent will only run the task on hosts matching this scope or on hosts where containers match this scope.
            - enabled: Whether this task should actually run as defined by its schedule.

        **Success Return Value**
            A JSON representation of the compliance task.
        '''
        task = {
            "id": None,
            "name": name,
            "moduleName": module_name,
            "enabled": enabled,
            "scope": scope,
            "schedule": schedule
        }
        res = self.http.post(self.url + '/api/complianceTasks', data=json.dumps(task), headers=self.hdrs,
                             verify=self.ssl_verify)
        return self._request_result(res)

    def list_compliance_tasks(self):
        '''**Description**
            Get the list of all compliance tasks.

        **Arguments**
            - None

        **Success Return Value**
            A JSON list with the representation of each compliance task.
        '''
        res = self.http.get(self.url + '/api/complianceTasks', headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def get_compliance_task(self, id):
        '''**Description**
            Get a compliance task.

        **Arguments**
            - id: the id of the compliance task to get.

        **Success Return Value**
            A JSON representation of the compliance task.
        '''
        res = self.http.get(self.url + '/api/complianceTasks/{}'.format(id), headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def update_compliance_task(self, id, name=None, module_name=None, schedule=None, scope=None, enabled=None):
        '''**Description**
            Update an existing compliance task.

        **Arguments**
            - id: the id of the compliance task to be updated.
            - name: The name of the task e.g. 'Check Docker Compliance'.
            - module_name: The name of the module that implements this task. Separate from task name in case you want to use the same module to run separate tasks with different scopes or schedules. [ 'docker-bench-security', 'kube-bench' ]
            - schedule: The frequency at which this task should run. Expressed as an `ISO 8601 Duration <https://en.wikipedia.org/wiki/ISO_8601#Durations>`_
            - scope: The agent will only run the task on hosts matching this scope or on hosts where containers match this scope.
            - enabled: Whether this task should actually run as defined by its schedule.

        **Success Return Value**
            A JSON representation of the compliance task.
        '''
        ok, res = self.get_compliance_task(id)
        if not ok:
            return ok, res

        task = res
        options = {
            'name': name,
            'moduleName': module_name,
            'schedule': schedule,
            'scope': scope,
            'enabled': enabled
        }
        task.update({k: v for k, v in options.items() if v is not None})
        res = self.http.put(self.url + '/api/complianceTasks/{}'.format(id), data=json.dumps(task), headers=self.hdrs,
                            verify=self.ssl_verify)
        return self._request_result(res)

    def delete_compliance_task(self, id):
        '''**Description**
            Delete the compliance task with the given id

        **Arguments**
            - id: the id of the compliance task to delete
        '''
        res = self.http.delete(self.url + '/api/complianceTasks/{}'.format(id), headers=self.hdrs,
                               verify=self.ssl_verify)
        if not self._checkResponse(res):
            return False, self.lasterr

        return True, None

    def list_compliance_results(self, limit=50, direction=None, cursor=None, filter=""):
        '''**Description**
            Get the list of all compliance tasks runs.

        **Arguments**
            - limit: Maximum number of alerts in the response.
            - direction: the direction (PREV or NEXT) that determines which results to return in relation to cursor.
            - cursor: An opaque string representing the current position in the list of alerts. It's provided in the 'responseMetadata' of the list_alerts response.
            - filter: an optional case insensitive filter used to match against the completed task name and return matching results.

        **Success Return Value**
            A JSON list with the representation of each compliance task run.
        '''
        url = "{url}/api/complianceResults?cursor{cursor}&filter={filter}&limit={limit}{direction}".format(
            url=self.url,
            limit=limit,
            direction="&direction=%s" % direction if direction else "",
            cursor="=%d" % cursor if cursor is not None else "",
            filter=filter)
        res = self.http.get(url, headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def get_compliance_results(self, id):
        '''**Description**
            Retrieve the details for a specific compliance task run result.

        **Arguments**
            - id: the id of the compliance task run to get.

        **Success Return Value**
            A JSON representation of the compliance task run result.
        '''
        res = self.http.get(self.url + '/api/complianceResults/{}'.format(id), headers=self.hdrs,
                            verify=self.ssl_verify)
        return self._request_result(res)

    def get_compliance_results_csv(self, id):
        '''**Description**
            Retrieve the details for a specific compliance task run result in csv.

        **Arguments**
            - id: the id of the compliance task run to get.

        **Success Return Value**
            A CSV representation of the compliance task run result.
        '''
        res = self.http.get(self.url + '/api/complianceResults/{}/csv'.format(id), headers=self.hdrs,
                            verify=self.ssl_verify)
        if not self._checkResponse(res):
            return False, self.lasterr

        return True, res.text

    def list_commands_audit(self, from_sec=None, to_sec=None, scope_filter=None, command_filter=None, limit=100,
                            offset=0, metrics=[]):
        '''**Description**
            List the commands audit.

        **DEPRECATED**: Use sdcclient.secure.ActivityAuditClientV1 instead. This is maintained for old on-prem versions, but will be removed over time.

        **Arguments**
            - from_sec: the start of the timerange for which to get commands audit.
            - end_sec: the end of the timerange for which to get commands audit.
            - scope_filter: this is a SysdigMonitor-like filter (e.g 'container.image=ubuntu'). When provided, commands are filtered by their scope, so only a subset will be returned (e.g. 'container.image=ubuntu' will provide only commands that have happened on an ubuntu container).
            - command_filter: this is a SysdigMonitor-like filter (e.g. command.comm="touch"). When provided, commands are filtered by some of their properties. Currently the supported set of filters is command.comm, command.cwd, command.pid, command.ppid, command.uid, command.loginshell.id, command.loginshell.distance
            - limit: Maximum number of commands in the response.
            - metrics: A list of metric values to include in the return.

        **Success Return Value**
            A JSON representation of the commands audit.
        '''
        if to_sec is None:
            to_sec = time.time()
        if from_sec is None:
            from_sec = to_sec - (24 * 60 * 60)  # 1 day

        url = "{url}/api/commands?from={frm}&to={to}&offset={offset}&limit={limit}{scope}{commandFilter}{metrics}".format(
            url=self.url,
            offset=offset,
            limit=limit,
            frm=int(from_sec * 10 ** 6),
            to=int(to_sec * 10 ** 6),
            scope="&scopeFilter=" + scope_filter if scope_filter else "",
            commandFilter="&commandFilter=" + command_filter if command_filter else "",
            metrics="&metrics=" + json.dumps(metrics) if metrics else "")
        res = self.http.get(url, headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def get_command_audit(self, id, metrics=[]):
        '''**Description**
            Get a command audit.

        **DEPRECATED**: Use sdcclient.secure.ActivityAuditClientV1 instead. This is maintained for old on-prem versions, but will be removed over time.

        **Arguments**
            - id: the id of the command audit to get.

        **Success Return Value**
            A JSON representation of the command audit.
        '''
        url = "{url}/api/commands/{id}?from=0&to={to}{metrics}".format(
            url=self.url,
            id=id,
            to=int(time.time() * 10 ** 6),
            metrics="&metrics=" + json.dumps(metrics) if metrics else "")
        res = self.http.get(url, headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def list_image_profiles(self):
        '''**Description**
            List the current set of image profiles.

        **Arguments**
            - None

        **Success Return Value**
            A JSON object containing the details of each profile.

        '''
        url = "{url}/api/v1/profiling/profileGroups/0/profiles".format(
            url=self.url
        )

        res = self.http.get(url, headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def get_image_profile(self, profileId):
        '''**Description**
            Find the image profile with a (partial) profile ID <profileId> and return its json description.

        **Arguments**
            - name: the name of the image profile to fetch

        **Success Return Value**
            A JSON object containing the description of the image profile. If there is no image profile with
            the given name, returns False. Moreover, it could happen that more than one profile IDs have a collision.
            It is due to the fact that a partial profile ID can be passed and interpreted; in this case a set of
            collision profiles is returned, and the full complete ID string is printed. In this case, it returns
            false.

        '''

        # RETRIEVE ALL THE IMAGE PROFILES
        ok, image_profiles = self.list_image_profiles()

        if not ok:
            return [False, self.lasterr]

        '''
        The content of the json stored in the image_profiles dictionary:

        {
            "offset": 0,
            "limit": 99,
            "canLoadMore": false,
            "profiles": [
            ...
            ]
        }
        '''

        matched_profiles = self.__get_matched_profileIDs(profileId, image_profiles['profiles'])

        # Profile ID not found
        if len(matched_profiles) == 0:
            return [False, "No profile with ID {}".format(profileId)]

        # Principal workflow. Profile ID found
        elif len(matched_profiles) == 1:
            # Matched id. Return information
            url = "{url}/api/v1/profiling/profiles/{profileId}".format(
                url=self.url,
                profileId=matched_profiles[0]['profileId']
            )

            res = self.http.get(url, headers=self.hdrs, verify=self.ssl_verify)
            return self._request_result(res)

        # Collision detected. The full profile IDs are returned
        elif len(matched_profiles) >= 2:
            return [False, matched_profiles]

    def __get_matched_profileIDs(self, requested_profile, profile_list):
        '''
        **Description**
            Helper function for  retrieving the list of matching profile

        **Arguments**
            - the requested profile Id (string)
            - List of dictionary, where each dictionary contains the profile information

        **Success Return Value**
            List of dictionary, where each dictionary represents a profile with the ID prefix substring
            matching the requested one

        **Content structure of the profile_list parameter**
        This array of profiles contains all the relevant information. For the purposes of this function, only
        the profileId field is relevant.

        [
            {
            "profileGroupId": 0,
            "profileId": "00000000000000000000000000000000000000000000",
            "profileVersion": 0,
            "profileName": "AAA/BBB:XYZ@0000000000000000000000",
            "imageId": "00000000000000000000000000000000000000000000",
            "imageName": "AAA/BBB:XYZ",
            "processesProposal": {
                "subcategories": [
                                    {
                                    "name": "process",
                                    "ruleName": "process - 00000000000000000000000000000000000000000000",
                                    "ruleType": "PROCESS",
                                    "score": 000
                                    }
                                ],
                                "score": 000
            },
            "fileSystemProposal": {
                "subcategories": [
                                    {
                                    "name": "filesystem",
                                    "ruleName": "filesystem - 00000000000000000000000000000000000000000000",
                                    "ruleType": "FILESYSTEM",
                                    "score": 000
                                    }
                                ],
                                "score": 000
            },
            "syscallProposal": {
                "subcategories": [
                                    {
                                    "name": "syscalls",
                                    "ruleName": "syscalls - 00000000000000000000000000000000000000000000",
                                    "ruleType": "SYSCALL",
                                    "score": 000
                                    }
                                ],
                                "score": 000
            },
            "networkProposal": {
                "subcategories": [
                                    {
                                    "name": "network",
                                    "ruleName": "network - 00000000000000000000000000000000000000000000",
                                    "ruleType": "NETWORK",
                                    "score": 000
                                    }
                                ],
                                "score": 000
            },
            "containerImagesProposal": {
                "subcategories": [
                                    {
                                    "name": "container image",
                                    "ruleName": "container image - 00000000000000000000000000000000000000000000",
                                    "ruleType": "CONTAINER",
                                    "score": 0
                                    }
                                ],
                                "score": 0
            },
            "status": "STATUS_VALUE",
            "score": 000
            },
            ...
        ]
        '''

        matched_profiles = []

        request_len = len(requested_profile)
        for profile in profile_list:

            # get the length of the substring to match
            str_len_match = min(len(profile), request_len)

            if profile['profileId'][0:str_len_match] == requested_profile[0:str_len_match]:
                matched_profiles.append(profile)

        return matched_profiles
