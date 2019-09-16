import datetime
import json
import requests
import shutil
import time
import os
import yaml

from sdcclient._common import _SdcCommon


class SdSecureClient(_SdcCommon):

    def __init__(self, token="", sdc_url='https://secure.sysdig.com', ssl_verify=True, custom_headers=None):
        super(SdSecureClient, self).__init__(token, sdc_url, ssl_verify, custom_headers)

        self.customer_id = None
        self.product = "SDS"

    def _get_falco_rules(self, kind):
        res = requests.get(self.url + '/api/settings/falco/{}RulesFile'.format(kind), headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        data = res.json()
        return [True, data]

    def get_system_falco_rules(self):
        '''**Description**
            Get the system falco rules file in use for this customer. See the `Falco wiki <https://github.com/draios/falco/wiki/Falco-Rules>`_ for documentation on the falco rules format.

        **Arguments**
            - None

        **Success Return Value**
            The contents of the system falco rules file.

        **Example**
            `examples/get_secure_system_falco_rules.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_secure_system_falco_rules.py>`_
        '''

        return self._get_falco_rules("system")

    def get_user_falco_rules(self):
        '''**Description**
            Get the user falco rules file in use for this customer. See the `Falco wiki <https://github.com/draios/falco/wiki/Falco-Rules>`_ for documentation on the falco rules format.

        **Arguments**
            - None

        **Success Return Value**
            The contents of the user falco rules file.

        **Example**
            `examples/get_secure_user_falco_rules.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_secure_user_falco_rules.py>`_
        '''
        return self._get_falco_rules("user")

    def _set_falco_rules(self, kind, rules_content):
        payload = self._get_falco_rules(kind)

        if not payload[0]:
            return payload

        payload[1]["{}RulesFile".format(kind)]["content"] = rules_content  # pylint: disable=unsubscriptable-object

        res = requests.put(self.url + '/api/settings/falco/{}RulesFile'.format(kind), headers=self.hdrs, data=json.dumps(payload[1]), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def set_system_falco_rules(self, rules_content):
        '''**Description**
            Set the system falco rules file in use for this customer. NOTE: This API endpoint can *only* be used in on-premise deployments. Generally the system falco rules file is only modified in conjunction with Sysdig support. See the `Falco wiki <https://github.com/draios/falco/wiki/Falco-Rules>`_ for documentation on the falco rules format.

        **Arguments**
            - A string containing the system falco rules.

        **Success Return Value**
            The contents of the system falco rules file that were just updated.

        **Example**
            `examples/set_secure_system_falco_rules.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_secure_system_falco_rules.py>`_

        '''
        return self._set_falco_rules("system", rules_content)

    def set_user_falco_rules(self, rules_content):
        '''**Description**
            Set the user falco rules file in use for this customer. See the `Falco wiki <https://github.com/draios/falco/wiki/Falco-Rules>`_ for documentation on the falco rules format.

        **Arguments**
            - A string containing the user falco rules.

        **Success Return Value**
            The contents of the user falco rules file that were just updated.

        **Example**
            `examples/set_secure_user_falco_rules.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_secure_user_falco_rules.py>`_

        '''
        return self._set_falco_rules("user", rules_content)

    # Only one kind for now called "default", but might add a "custom" kind later.
    def _get_falco_rules_files(self, kind):

        res = requests.get(self.url + '/api/settings/falco/{}RulesFiles'.format(kind), headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        data = res.json()

        return [True, data]

    def get_default_falco_rules_files(self):
        '''**Description**
            Get the set of falco rules files from the backend. The _files programs and endpoints are a
               replacement for the system_file endpoints and allow for publishing multiple files instead
               of a single file as well as publishing multiple variants of a given file that are compatible
               with different agent versions.

        **Arguments**
            - None

        **Success Return Value**
            A dict with the following keys:
               - tag: A string used to uniquely identify this set of rules. It is recommended that this tag change every time the set of rules is updated.
               - files: An array of dicts. Each dict has the following keys:
                     - name: the name of the file
                     - variants: An array of dicts with the following keys:
                          - requiredEngineVersion: the minimum falco engine version that can read this file
                          - content: the falco rules content
            An example would be:
               {'tag': 'v1.5.9',
                'files': [
                    {
                        'name': 'falco_rules.yaml',
                        'variants': [
                            {
                                'content': '- required_engine_version: 29\n\n- list: foo\n',
                                'requiredEngineVersion': 29
                            },
                            {
                                'content': '- required_engine_version: 1\n\n- list: foo\n',
                                'requiredEngineVersion': 1
                            }
                        ]
                    },
                    {
                        'name': 'k8s_audit_rules.yaml',
                        'variants': [
                            {
                                'content': '# some comment\n',
                                'requiredEngineVersion': 0
                            }
                        ]
                    }
                ]
              }

        **Example**
            `examples/get_default_falco_rules_files.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_default_falco_rules_files.py>`_
        '''

        res = self._get_falco_rules_files("default")

        if not res[0]:
            return res
        else:
            res_obj = res[1]["defaultFalcoRulesFiles"]

            # Copy only the tag and files over
            ret = {}

            if "tag" in res_obj:
                ret["tag"] = res_obj["tag"]

            if "files" in res_obj:
                ret["files"] = res_obj["files"]

            if "defaultPolicies" in res_obj:
                ret["defaultPolicies"] = res_obj["defaultPolicies"]

            return [True, ret]

    def save_default_falco_rules_files(self, fsobj, save_dir):
        '''**Description**
            Given a dict returned from get_default_falco_rules_files, save those files to a set of files below save_dir.
               The first level below save_dir is a directory with the tag name and an optional default_policies.yaml file,
               which groups rules into recommended default policies. The second level is a directory per file.
               The third level is a directory per variant. Finally the files are at the lowest level, in a file called "content".
            For example, using the example dict in get_default_falco_rules_files(), the directory layout would look like:
                save_dir/
                    default_policies.yaml
                    v1.5.9/
                        falco_rules.yaml/
                            29/
                                content: a file containing "- required_engine_version: 29\n\n- list: foo\n"
                            1/
                                content: a file containing "- required_engine_version: 1\n\n- list: foo\n"
                        k8s_audit_rules.yaml/
                            0/
                                content: a file containing "# some comment"
        **Arguments**
            - fsobj: a python dict matching the structure returned by get_default_falco_rules_files()
            - save_dir: a directory path under which to save the files. If the path already exists, it will be removed first.

        **Success Return Value**
            - None

        **Example**
            `examples/get_default_falco_rules_files.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_default_falco_rules_files.py>`_
        '''
        if os.path.exists(save_dir):
            try:
                if os.path.isdir(save_dir):
                    shutil.rmtree(save_dir)
                else:
                    os.unlink(save_dir)
            except Exception as e:
                return [False, "Could not remove existing save dir {}: {}".format(save_dir, str(e))]

        prefix = os.path.join(save_dir, fsobj["tag"])
        try:
            os.makedirs(prefix)
        except Exception as e:
            return [False, "Could not create tag directory {}: {}".format(prefix, str(e))]

        if "defaultPolicies" in fsobj:
            with open(os.path.join(save_dir, "default_policies.yaml"), 'w') as outfile:
                yaml.safe_dump(fsobj["defaultPolicies"], outfile)

        if "files" in fsobj:
            for fobj in fsobj["files"]:
                fprefix = os.path.join(prefix, fobj["name"])
                try:
                    os.makedirs(fprefix)
                except Exception as e:
                    return [False, "Could not create file directory {}: {}".format(fprefix, str(e))]
                for variant in fobj["variants"]:
                    vprefix = os.path.join(fprefix, str(variant["requiredEngineVersion"]))
                    try:
                        os.makedirs(vprefix)
                    except Exception as e:
                        return [False, "Could not create variant directory {}: {}".format(vprefix, str(e))]
                    cpath = os.path.join(vprefix, "content")
                    try:
                        with open(cpath, "w") as cfile:
                            cfile.write(variant["content"])
                    except Exception as e:
                        return [False, "Could not write content to {}: {}".format(cfile, str(e))]

        return [True, None]

    # Only One kind for now, but might add a "custom" kind later.
    def _set_falco_rules_files(self, kind, rules_files):

        payload = self._get_falco_rules_files(kind)

        if not payload[0]:
            return payload

        obj = payload[1]["{}FalcoRulesFiles".format(kind)]  # pylint: disable=unsubscriptable-object

        obj["tag"] = rules_files["tag"]
        obj["files"] = rules_files["files"]
        if "defaultPolicies" in rules_files:
            obj["defaultPolicies"] = rules_files["defaultPolicies"]

        res = requests.put(self.url + '/api/settings/falco/{}RulesFiles'.format(kind), headers=self.hdrs, data=json.dumps(payload[1]), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def set_default_falco_rules_files(self, rules_files):
        '''**Description**
            Update the set of falco rules files to the provided set of files. See the `Falco wiki <https://github.com/draios/falco/wiki/Falco-Rules>`_ for documentation on the falco rules format.
               The _files programs and endpoints are a replacement for the system_file endpoints and
               allow for publishing multiple files instead of a single file as well as publishing
               multiple variants of a given file that are compatible with different agent versions.

        **Arguments**
            - rules_files: a dict with the same structure as returned by get_default_falco_rules_files.

        **Success Return Value**
            The contents of the default falco rules files that were just updated.

        **Example**
            `examples/set_default_falco_rules_files.py <https://github.com/draios/python-sdc-client/blob/master/examples/set_default_falco_rules_files.py>`_

        '''

        return self._set_falco_rules_files("default", rules_files)

    def load_default_falco_rules_files(self, save_dir):
        '''**Description**
            Given a file and directory layout as described in save_default_falco_rules_files(), load those files and
            return a dict representing the contents. This dict is suitable for passing to set_default_falco_rules_files().

        **Arguments**
            - save_dir: a directory path from which to load the files.

        **Success Return Value**
            - A dict matching the format described in get_default_falco_rules_files.

        **Example**
            `examples/set_default_falco_rules_files.py <https://github.com/draios/python-sdc-client/blob/master/examples/set_default_falco_rules_files.py>`_
        '''

        tags = os.listdir(save_dir)

        try:
            tags.remove("default_policies.yaml")
        except ValueError as e:
            # Do nothing, it wasn't in the list of files
            pass

        if len(tags) != 1:
            return [False, "Directory {} did not contain exactly 1 entry".format(save_dir)]

        tpath = os.path.join(save_dir, tags[0])

        if not os.path.isdir(tpath):
            return [False, "Tag path {} is not a directory".format(tpath)]

        defjson = []
        defpath = os.path.join(save_dir, "default_policies.yaml")
        if os.path.exists(defpath):
            try:
                with open(defpath, "r") as infile:
                    defjson = yaml.safe_load(infile)
            except Exception as e:
                return [False, "Could not load default_policies.yaml: " + exc]

        ret = {"tag": os.path.basename(tpath), "files": [], "defaultPolicies": defjson}

        for fdir in os.listdir(tpath):
            fpath = os.path.join(tpath, fdir)
            if not os.path.isdir(fpath):
                return [False, "File path {} is not a directory".format(fpath)]
            fobj = {"name": os.path.basename(fpath), "variants": []}
            for vdir in os.listdir(fpath):
                vpath = os.path.join(fpath, vdir)
                if not os.path.isdir(vpath):
                    return [False, "Variant path {} is not a directory".format(vpath)]
                cpath = os.path.join(vpath, "content")
                try:
                    with open(cpath, 'r') as content_file:
                        try:
                            required_engine_version = int(os.path.basename(vpath))
                            if vpath < 0:
                                return [False, "Variant directory {} must be a positive number".format(vpath)]
                            fobj["variants"].append({
                                "requiredEngineVersion": required_engine_version,
                                "content": content_file.read()
                            })
                        except ValueError:
                            return [False, "Variant directory {} must be a number".format(vpath)]
                except Exception as e:
                    return [False, "Could not read content at {}: {}".format(cpath, str(e))]

            ret["files"].append(fobj)

        return [True, ret]

    def _get_policy_events_int(self, ctx):
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

        res = requests.get(policy_events_url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        # Increment the offset by limit
        ctx['offset'] += ctx['limit']

        return [True, {"ctx": ctx, "data": res.json()}]

    def get_policy_events_range(self, from_sec, to_sec, sampling=None, aggregations=None, scope_filter=None, event_filter=None):
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

    def get_policy_events_duration(self, duration_sec, sampling=None, aggregations=None, scope_filter=None, event_filter=None):
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

    def get_policy_events_id_range(self, id, from_sec, to_sec, sampling=None, aggregations=None, scope_filter=None, event_filter=None):
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

    def get_policy_events_id_duration(self, id, duration_sec, sampling=None, aggregations=None, scope_filter=None, event_filter=None):
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

        ctx = {"id": id,
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

        **Example**
            `examples/create_default_policies.py <https://github.com/draios/python-sdc-client/blob/master/examples/create_default_policies.py>`_

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

        **Example**
            `examples/delete_all_policies.py <https://github.com/draios/python-sdc-client/blob/master/examples/delete_all_policies.py>`_

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

        **Example**
            `examples/list_policies.py <https://github.com/draios/python-sdc-client/blob/master/examples/list_policies.py>`_

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

        **Example**
            `examples/list_policies.py <https://github.com/draios/python-sdc-client/blob/master/examples/list_policies.py>`_

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

        **Example**
            `examples/set_policy_order.py <https://github.com/draios/python-sdc-client/blob/master/examples/set_policy_order.py>`_

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

        **Example**
            `examples/get_policy.py <https://github.com/draios/python-sdc-client/blob/master/examples/get_policy.py>`_

        '''
        res = requests.get(self.url + '/api/policies', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        policies = res.json()["policies"]

        # Find the policy with the given name and return it.
        for policy in policies:
            if policy["name"] == name:
                return [True, policy]

        return [False, "No policy with name {}".format(name)]

    def add_policy(self, policy_json):
        '''**Description**
            Add a new policy using the provided json.

        **Arguments**
            - policy_json: a description of the new policy

        **Success Return Value**
            The string "OK"

        **Example**
            `examples/add_policy.py <https://github.com/draios/python-sdc-client/blob/master/examples/add_policy.py>`_

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

        **Example**
            `examples/update_policy.py <https://github.com/draios/python-sdc-client/blob/master/examples/update_policy.py>`_

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

        **Example**
            `examples/delete_policy.py <https://github.com/draios/python-sdc-client/blob/master/examples/delete_policy.py>`_

        '''
        res = requests.get(self.url + '/api/policies', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        # Find the policy with the given name and delete it
        for policy in res.json()["policies"]:
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

        **Example**
            `examples/delete_policy.py <https://github.com/draios/python-sdc-client/blob/master/examples/delete_policy.py>`_

        '''
        res = requests.delete(self.url + '/api/policies/{}'.format(id), headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def add_compliance_task(self, name, module_name='docker-bench-security', schedule='06:00:00Z/PT12H', scope=None, enabled=True):
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
        res = requests.post(self.url + '/api/complianceTasks', data=json.dumps(task), headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def list_compliance_tasks(self):
        '''**Description**
            Get the list of all compliance tasks.

        **Arguments**
            - None

        **Success Return Value**
            A JSON list with the representation of each compliance task.
        '''
        res = requests.get(self.url + '/api/complianceTasks', headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def get_compliance_task(self, id):
        '''**Description**
            Get a compliance task.

        **Arguments**
            - id: the id of the compliance task to get.

        **Success Return Value**
            A JSON representation of the compliance task.
        '''
        res = requests.get(self.url + '/api/complianceTasks/{}'.format(id), headers=self.hdrs, verify=self.ssl_verify)
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
        res = requests.put(self.url + '/api/complianceTasks/{}'.format(id), data=json.dumps(task), headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def delete_compliance_task(self, id):
        '''**Description**
            Delete the compliance task with the given id

        **Arguments**
            - id: the id of the compliance task to delete
        '''
        res = requests.delete(self.url + '/api/complianceTasks/{}'.format(id), headers=self.hdrs, verify=self.ssl_verify)
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
        res = requests.get(url, headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def get_compliance_results(self, id):
        '''**Description**
            Retrieve the details for a specific compliance task run result.

        **Arguments**
            - id: the id of the compliance task run to get.

        **Success Return Value**
            A JSON representation of the compliance task run result.
        '''
        res = requests.get(self.url + '/api/complianceResults/{}'.format(id), headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def get_compliance_results_csv(self, id):
        '''**Description**
            Retrieve the details for a specific compliance task run result in csv.

        **Arguments**
            - id: the id of the compliance task run to get.

        **Success Return Value**
            A CSV representation of the compliance task run result.
        '''
        res = requests.get(self.url + '/api/complianceResults/{}/csv'.format(id), headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return False, self.lasterr

        return True, res.text

    def list_commands_audit(self, from_sec=None, to_sec=None, scope_filter=None, command_filter=None, limit=100, offset=0, metrics=[]):
        '''**Description**
            List the commands audit.

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
            frm=int(from_sec * 10**6),
            to=int(to_sec * 10**6),
            scope="&scopeFilter=" + scope_filter if scope_filter else "",
            commandFilter="&commandFilter=" + command_filter if command_filter else "",
            metrics="&metrics=" + json.dumps(metrics) if metrics else "")
        res = requests.get(url, headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def get_command_audit(self, id, metrics=[]):
        '''**Description**
            Get a command audit.

        **Arguments**
            - id: the id of the command audit to get.

        **Success Return Value**
            A JSON representation of the command audit.
        '''
        url = "{url}/api/commands/{id}?from=0&to={to}{metrics}".format(
            url=self.url,
            id=id,
            to=int(time.time() * 10**6),
            metrics="&metrics=" + json.dumps(metrics) if metrics else "")
        res = requests.get(url, headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def list_image_profiles(self):
        '''**Description**
            List the current set of image profiles.

        **Arguments**
            - None

        **Success Return Value**
            A JSON object containing the details of each profile.

        '''
        url = "{url}/api/profiling/v1/secure/profileGroups/0/profiles".format(
            url = self.url
        )

        res = requests.get(url, headers=self.hdrs, verify=self.ssl_verify)
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
            url = "{url}/api/profiling/v1/secure/profiles/{profileId}".format(
                url = self.url,
                profileId = matched_profiles[0]['profileId']
            )
            
            res = requests.get(url, headers=self.hdrs, verify=self.ssl_verify)
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

