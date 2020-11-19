import json
import os
import shutil

import yaml

from sdcclient._common import _SdcCommon


class FalcoRulesFilesClientOld(_SdcCommon):
    def __init__(self, token="", sdc_url='https://secure.sysdig.com', ssl_verify=True, custom_headers=None):
        super(FalcoRulesFilesClientOld, self).__init__(token, sdc_url, ssl_verify, custom_headers)
        self.product = "SDS"

    # TODO: Remove this one, deprecated
    def _get_falco_rules(self, kind):
        res = self.http.get(self.url + '/api/settings/falco/{}RulesFile'.format(kind), headers=self.hdrs,
                            verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        data = res.json()
        return [True, data]

    # TODO: Change this one to use newestDefaultRulesFiles endpoint
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
            `examples/get_secure_user_falco_rules.py <https://github.com/draios/python-sdc-client/blob/master/examples/newestDefaultRulesFiles>`_
        '''
        ok, res = self._get_user_falco_rules()
        if not ok:
            return [False, res]

        local_rules_file = [file
                            for file in res["customFalcoRulesFiles"]["files"]
                            if file["name"] == "falco_rules_local.yaml"]
        if len(local_rules_file) == 0:
            return [False, "Expected falco_rules_local.yaml file, but no file found"]

        return [True, local_rules_file[0]["variants"][0]["content"]]

    def _get_user_falco_rules(self):
        res = self.http.get(self.url + '/api/settings/falco/customRulesFiles', headers=self.hdrs,
                            verify=self.ssl_verify)

        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, (res.json())]

    # TODO: Remove this
    def _set_falco_rules(self, kind, rules_content):
        payload = self._get_falco_rules(kind)

        if not payload[0]:
            return payload

        payload[1]["{}RulesFile".format(kind)]["content"] = rules_content  # pylint: disable=unsubscriptable-object

        res = self.http.put(self.url + '/api/settings/falco/{}RulesFile'.format(kind), headers=self.hdrs,
                            data=json.dumps(payload[1]), verify=self.ssl_verify)
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
        ok, res = self._get_user_falco_rules()

        if not ok:
            return res

        local_rules_file = [file
                            for file in res["customFalcoRulesFiles"]["files"]
                            if file["name"] == "falco_rules_local.yaml"]
        if len(local_rules_file) == 0:
            return [False, "Expected falco_rules_local.yaml file, but no file found"]

        local_rules_file[0]["variants"][0]["content"] = rules_content

        res = self.http.put(self.url + '/api/settings/falco/customRulesFiles', headers=self.hdrs,
                            data=json.dumps(res), verify=self.ssl_verify)

        if not self._checkResponse(res):
            return [False, self.lasterr]
        res_json = res.json()
        return [True, res_json["customFalcoRulesFiles"]["files"][0]["variants"][0]["content"]]

    # get_falco_syscall_rules()

    # get_falco_ka_rules()

    # Only one kind for now called "default", but might add a "custom" kind later.
    # TODO Remove this one
    def _get_falco_rules_files(self, kind):

        res = self.http.get(self.url + '/api/settings/falco/{}RulesFiles'.format(kind), headers=self.hdrs,
                            verify=self.ssl_verify)
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

        res = self.http.put(self.url + '/api/settings/falco/{}RulesFiles'.format(kind), headers=self.hdrs,
                            data=json.dumps(payload[1]), verify=self.ssl_verify)
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
        except ValueError:
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
            except Exception as exc:
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
                            if int(os.path.basename(vpath)) < 0:
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
