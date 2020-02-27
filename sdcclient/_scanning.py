import base64
import hashlib
import json
import re
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import time

try:
    from urllib.parse import quote_plus, unquote_plus
except ImportError:
    from urllib import quote_plus, unquote_plus

from sdcclient._common import _SdcCommon


class SdScanningClient(_SdcCommon):

    def __init__(self, token="", sdc_url='https://secure.sysdig.com', ssl_verify=True, custom_headers=None):
        super(SdScanningClient, self).__init__(token, sdc_url, ssl_verify, custom_headers)
        self.product = "SDS"

    def add_image(self, image, force=False, dockerfile=None, annotations={}, autosubscribe=True):
        '''**Description**
            Add an image to the scanner

        **Arguments**
            - image: Input image can be in the following formats: registry/repo:tag
            - dockerfile: The contents of the dockerfile as a str.
            - annotations: A dictionary of annotations {str: str}.
            - autosubscribe: Should active the subscription to this image?

        **Success Return Value**
            A JSON object representing the image that was added.
        '''
        itype = self._discover_inputimage_format(image)
        if itype != 'tag':
            return [False, "can only add a tag"]

        payload = {}
        if dockerfile:
            payload['dockerfile'] = base64.b64encode(dockerfile.encode()).decode("utf-8")
        payload['tag'] = image
        if annotations:
            payload['annotations'] = annotations

        url = "{base_url}/api/scanning/v1/anchore/images?autosubscribe={autosubscribe}{force}".format(
            base_url=self.url,
            autosubscribe=str(autosubscribe),
            force="&force=true" if force else "")

        res = requests.post(url, data=json.dumps(payload), headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def get_image(self, image, show_history=False):
        '''**Description**
            Find the image with the tag <image> and return its json description

        **Arguments**
            - image: Input image can be in the following formats: registry/repo:tag

        **Success Return Value**
            A JSON object representing the image.
        '''
        itype = self._discover_inputimage_format(image)
        if itype not in ['tag', 'imageid', 'imageDigest']:
            return [False, "cannot use input image string: no discovered imageDigest"]

        params = {}
        params['history'] = str(show_history and itype not in ['imageid', 'imageDigest']).lower()
        if itype == 'tag':
            params['fulltag'] = image

        url = self.url + "/api/scanning/v1/anchore/images"
        url += {
            'imageid': '/by_id/{}'.format(image),
            'imageDigest': '/{}'.format(image)
        }.get(itype, '')

        res = requests.get(url, params=params, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def list_images(self):
        '''**Description**
            List the current set of images in the scanner.

        **Arguments**
            - None

        **Success Return Value**
            A JSON object containing all the images.
        '''
        url = self.url + "/api/scanning/v1/anchore/images"
        res = requests.get(url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def query_image_content(self, image, content_type=""):
        '''**Description**
            Find the image with the tag <image> and return its content.

        **Arguments**
            - image: Input image can be in the following formats: registry/repo:tag
            - content_type: The content type can be one of the following types:
                - os: Operating System Packages
                - npm: Node.JS NPM Module
                - gem: Ruby GEM
                - files: Files

        **Success Return Value**
            A JSON object representing the image content.
        '''
        return self._query_image(image, query_group='content', query_type=content_type)

    def query_image_metadata(self, image, metadata_type=""):
        '''**Description**
            Find the image with the tag <image> and return its metadata.

        **Arguments**
            - image: Input image can be in the following formats: registry/repo:tag
            - metadata_type: The metadata type can be one of the types returned by running without a type specified

        **Success Return Value**
            A JSON object representing the image metadata.
        '''
        return self._query_image(image, query_group='metadata', query_type=metadata_type)

    def query_image_vuln(self, image, vuln_type="", vendor_only=True):
        '''**Description**
            Find the image with the tag <image> and return its vulnerabilities.

        **Arguments**
            - image: Input image can be in the following formats: registry/repo:tag
            - vuln_type: Vulnerability type can be one of the following types:
                - os: CVE/distro vulnerabilities against operating system packages

        **Success Return Value**
            A JSON object representing the image vulnerabilities.
        '''
        return self._query_image(image, query_group='vuln', query_type=vuln_type, vendor_only=vendor_only)

    def query_images_by_vulnerability(self, vulnerability_id, namespace=None, package=None, severity=None, vendor_only=True):
        '''**Description**
            Search system for images with the given vulnerability ID present

        **Arguments**
            - vulnerability_id: Search for images vulnerable to this vulnerability ID (e.g. CVE-1999-0001)
            - namespace: Filter results to images with vulnerable packages in the given namespace (e.g. debian:9)
            - package: Filter results to images with the given vulnerable package name (e.g. sed)
            - severity: Filter results to images with the given vulnerability severity (e.g. Medium)
            - vendor_only: Only show images with vulnerabilities explicitly deemed applicable by upstream OS vendor, if present

        **Success Return Value**
            A JSON object representing the images.
        '''
        url = "{base_url}/api/scanning/v1/anchore/query/images/by_vulnerability?vulnerability_id={vulnerability_id}{namespace}{package}{severity}&vendor_only={vendor_only}".format(
            base_url=self.url,
            vulnerability_id=vulnerability_id,
            namespace="&namespace={}".format(namespace) if namespace else "",
            package="&affected_package={}".format(package) if package else "",
            severity="&severity={}".format(severity) if severity else "",
            vendor_only=vendor_only)

        res = requests.get(url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def query_images_by_package(self, name, version=None, package_type=None):
        '''**Description**
            Search system for images with the given package installed

        **Arguments**
            - name: Search for images with this package name (e.g. sed)
            - version: Filter results to only packages with given version (e.g. 4.4-1)
            - package-type: Filter results to only packages of given type (e.g. dpkg)

        **Success Return Value**
            A JSON object representing the images.
        '''
        url = "{base_url}/api/scanning/v1/anchore/query/images/by_package?name={name}{version}{package_type}".format(
            base_url=self.url,
            name=name,
            version="&version={}".format(version) if version else "",
            package_type="&package_type={}".format(package_type) if package_type else "")

        res = requests.get(url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def _query_image(self, image, query_group="", query_type="", vendor_only=True):
        if not query_group:
            raise Exception("need to specify a query group")

        _, _, image_digest = self._discover_inputimage(image)
        if not image_digest:
            return [False, "cannot use input image string (no discovered imageDigest)"]

        url = "{base_url}/api/scanning/v1/anchore/images/{image_digest}/{query_group}/{query_type}{vendor_only}".format(
            base_url=self.url,
            image_digest=image_digest,
            query_group=query_group,
            query_type=query_type if query_type else '',
            vendor_only="?vendor_only={}".format(vendor_only) if query_group == 'vuln' else '')

        res = requests.get(url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def delete_image(self, image, force=False):
        '''**Description**
            Delete image from the scanner.

        **Arguments**
            - None
        '''
        _, _, image_digest = self._discover_inputimage(image)
        if not image_digest:
            return [False, "cannot use input image string: no discovered imageDigest"]

        url = self.url + "/api/scanning/v1/anchore/images/" + image_digest
        res = requests.delete(url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def check_image_evaluation(self, image, show_history=False, detail=False, tag=None, policy=None):
        '''**Description**
            Check the latest policy evaluation for an image

        **Arguments**
            - image: Input image can be in the following formats: registry/repo:tag
            - show_history: Show all previous policy evaluations
            - detail: Show detailed policy evaluation report
            - tag: Specify which TAG is evaluated for a given image ID or Image Digest
            - policy: Specify which POLICY to use for evaluate (defaults currently active policy)

        **Success Return Value**
            A JSON object representing the evaluation status.
        '''
        itype, _, image_digest = self._discover_inputimage(image)
        if not image_digest:
            return [False, "could not get image record from anchore"]
        if not tag and itype != 'tag':
            return [False, "input image name is not a tag, and no --tag is specified"]

        thetag = tag if tag else image

        url = "{base_url}/api/scanning/v1/anchore/images/{image_digest}/check?history={history}&detail={detail}&tag={tag}{policy_id}"
        url = url.format(
            base_url=self.url,
            image_digest=image_digest,
            history=str(show_history).lower(),
            detail=str(detail).lower(),
            tag=thetag,
            policy_id=("&policyId=%s" % policy) if policy else "")

        res = requests.get(url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def get_pdf_report(self, image, tag=None, date=None):
        '''**Description**
            Get a pdf report of one image

        **Arguments**
            - image: Input image can be in the following formats: registry/repo:tag
            - tag: Specify which TAG is evaluated for a given image ID or Image Digest
            - date: date for the report of interest, the format is 'YYYY-MM-DDTHH:MM:SSZ',
                    if not provided the latest report will be returned

        **Success Return Value**
            The pdf content
        '''
        image_type, _, image_digest = self._discover_inputimage(image)
        if not image_digest:
            return [False, "could not get image record from anchore"]
        if not tag and image_type != 'tag':
            return [False, "input image name is not a tag"]
        image_tag = tag if tag else image

        url = "{base_url}/api/scanning/v1/images/{image_digest}/report?tag={tag}{at}".format(
            base_url=self.url,
            image_digest=image_digest,
            tag=image_tag,
            at=("&at=%s" % date) if date else "")

        res = requests.get(url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.content]

    def get_latest_pdf_report_by_digest(self, image_digest, full_tag=None):
        '''**Description**
            Get the latest pdf report of one image digest

        **Arguments**
            - image_digest: Input image digest should be in the following formats: sha256:134dhgfd65765
            - tag: Specify which FULLTAG is evaluated for a given Image Digest: docker.io/alpine:latest

        **Success Return Value**
            The pdf content
        '''
        url = "{base_url}/api/scanning/v1/images/{image_digest}/report?tag={tag}".format(
            base_url=self.url,
            image_digest=image_digest,
            tag=full_tag)

        res = requests.get(url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.content]

    def import_image(self, infile, sync=False):
        '''**Description**
            Import an image archive

        **Arguments**
           - infile: An image archive file
           - sync: Whether the import should be synchronous or asynchronous

        **Success Return Value**
            If synchronous, A JSON object representing the image that was imported.

        '''
        try:
            m = MultipartEncoder(
                fields={'archive_file': (infile, open(infile, 'rb'), 'text/plain')}
            )
            if sync:
                url = self.url + "/api/scanning/v1/anchore/import/images"
            else:
                url = self.url + "/api/scanning/v1/import/images"

            headers = {'Authorization': 'Bearer ' + self.token, 'Content-Type': m.content_type}
            res = requests.post(url, data=m, headers=headers, verify=self.ssl_verify)
            if not self._checkResponse(res):
                return [False, self.lasterr]

            return [True, res.json() if sync else res.content]

        except Exception as err:
            print(err)

    def get_anchore_users_account(self):
        '''**Description**
            Get the anchore user account.

        **Arguments**
            - None

        **Success Return Value**
            A JSON object containing user account information.
        '''
        url = self.url + "/api/scanning/v1/anchore/account"
        res = requests.get(url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def get_image_scan_result_by_id(self, image_id, full_tag_name, detail):
        '''**Description**
            Get the anchore image scan result for an image id.

        **Arguments**
            - image_id: Docker image id of the image whose scan result is to be fetched.
            - full_tag_name: The complete tag name of the image for e.g. docker.io/alpine:3.10.
            - detail: Boolean to indicate whether full scan result API is needed.

        **Success Return Value**
            A JSON object containing pass/fail status of image scan policy.
        '''
        url = "{base_url}/api/scanning/v1/anchore/images/by_id/{image_id}/check?tag={full_tag_name}&detail={detail}".format(
                base_url=self.url,
                image_id=image_id,
                full_tag_name=full_tag_name,
                detail=detail)
        res = requests.get(url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def add_registry(self, registry, registry_user, registry_pass, insecure=False, registry_type="docker_v2", validate=True):
        '''**Description**
            Add image registry

        **Arguments**
            - registry: Full hostname/port of registry. Eg. myrepo.example.com:5000
            - registry_user: Username
            - registry_pass: Password
            - insecure: Allow connection to registry without SSL cert checks (ex: if registry uses a self-signed SSL certificate)
            - registry_type: Specify the registry type. 'docker_v2' and 'awsecr' are supported (default='docker_v2')
            - validate: If set to 'False' will not attempt to validate registry/creds on registry add

        **Success Return Value**
            A JSON object representing the registry.
        '''
        registry_types = ['docker_v2', 'awsecr']
        if registry_type and registry_type not in registry_types:
            return [False, "input registry type not supported (supported registry_types: " + str(registry_types)]
        if self._registry_string_is_valid(registry):
            return [False, "input registry name cannot contain '/' characters - valid registry names are of the form <host>:<port> where :<port> is optional"]

        if not registry_type:
            registry_type = self._get_registry_type(registry)

        payload = {
            'registry': registry,
            'registry_user': registry_user,
            'registry_pass': registry_pass,
            'registry_type': registry_type,
            'registry_verify': not insecure}
        url = "{base_url}/api/scanning/v1/anchore/registries?validate={validate}".format(
            base_url=self.url,
            validate=validate)

        res = requests.post(url, data=json.dumps(payload), headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def update_registry(self, registry, registry_user, registry_pass, insecure=False, registry_type="docker_v2", validate=True):
        '''**Description**
            Update an existing image registry.

        **Arguments**
            - registry: Full hostname/port of registry. Eg. myrepo.example.com:5000
            - registry_user: Username
            - registry_pass: Password
            - insecure: Allow connection to registry without SSL cert checks (ex: if registry uses a self-signed SSL certificate)
            - registry_type: Specify the registry type. 'docker_v2' and 'awsecr' are supported (default='docker_v2')
            - validate: If set to 'False' will not attempt to validate registry/creds on registry add

        **Success Return Value**
            A JSON object representing the registry.
        '''
        if self._registry_string_is_valid(registry):
            return [False, "input registry name cannot contain '/' characters - valid registry names are of the form <host>:<port> where :<port> is optional"]

        payload = {
            'registry': registry,
            'registry_user': registry_user,
            'registry_pass': registry_pass,
            'registry_type': registry_type,
            'registry_verify': not insecure}
        url = "{base_url}/api/scanning/v1/anchore/registries/{registry}?validate={validate}".format(
            base_url=self.url,
            registry=registry,
            validate=validate)

        res = requests.put(url, data=json.dumps(payload), headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def delete_registry(self, registry):
        '''**Description**
            Delete an existing image registry

        **Arguments**
            - registry: Full hostname/port of registry. Eg. myrepo.example.com:5000
        '''
        # do some input string checking
        if re.match(".*\\/.*", registry):
            return [False, "input registry name cannot contain '/' characters - valid registry names are of the form <host>:<port> where :<port> is optional"]

        url = self.url + "/api/scanning/v1/anchore/registries/" + registry
        res = requests.delete(url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def list_registry(self):
        '''**Description**
            List all current image registries

        **Arguments**
            - None

        **Success Return Value**
            A JSON object representing the list of registries.
        '''
        url = self.url + "/api/scanning/v1/anchore/registries"
        res = requests.get(url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def get_registry(self, registry):
        '''**Description**
            Find the registry and return its json description

        **Arguments**
            - registry: Full hostname/port of registry. Eg. myrepo.example.com:5000

        **Success Return Value**
            A JSON object representing the registry.
        '''
        if self._registry_string_is_valid(registry):
            return [False, "input registry name cannot contain '/' characters - valid registry names are of the form <host>:<port> where :<port> is optional"]

        url = self.url + "/api/scanning/v1/anchore/registries/" + registry
        res = requests.get(url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def _get_registry_type(self, registry):
        if re.match("[0-9]+\\.dkr\\.ecr\\..*\\.amazonaws\\.com", registry):
            return "awsecr"
        return "docker_v2"

    def _registry_string_is_valid(self, registry):
        return re.match(".*\\/.*", registry)

    def add_repo(self, repo, autosubscribe=True, lookuptag=None):
        '''**Description**
            Add a repository

        **Arguments**
            - repo: Input repository can be in the following formats: registry/repo
            - autosubscribe: If unset, instruct the engine to disable subscriptions for any discovered tags.
            - lookuptag: Specify a tag to use for repo tag scan if 'latest' tag does not exist in the repo.

        **Success Return Value**
            A JSON object representing the repo.
        '''
        url = "{base_url}/api/scanning/v1/anchore/repositories?repository={repo}&autosubscribe={autosubscribe}{lookuptag}".format(
            base_url=self.url,
            repo=repo,
            autosubscribe=autosubscribe,
            lookuptag="&lookuptag={}".format(lookuptag) if lookuptag else "")

        res = requests.post(url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def watch_repo(self, repo):
        '''**Description**
            Instruct engine to start automatically watching the repo for image updates

        **Arguments**
            - repo: Input repository can be in the following formats: registry/repo
        '''
        return self.activate_subscription('repo_update', repo)

    def unwatch_repo(self, repo):
        '''**Description**
            Instruct engine to stop automatically watching the repo for image updates

        **Arguments**
            - repo: Input repository can be in the following formats: registry/repo
        '''
        return self.deactivate_subscription('repo_update', repo)

    def delete_repo(self, repo):
        '''**Description**
            Delete a repository from the watch list (does not delete already analyzed images)

        **Arguments**
            - repo: Input repository can be in the following formats: registry/repo
        '''
        return self.delete_subscription('repo_update', repo)

    def list_repos(self):
        '''**Description**
            List added repositories

        **Arguments**
            - None

        **Success Return Value**
            A JSON object representing the list of repositories.
        '''
        return self.get_subscriptions("repo_update")

    def get_repo(self, repo):
        '''**Description**
            Get a repository

        **Arguments**
            - repo: Input repository can be in the following formats: registry/repo

        **Success Return Value**
            A JSON object representing the registry.
        '''
        return self.get_subscriptions("repo_update", repo)

    def add_policy(self, name, rules, comment="", bundleid=None):
        '''**Description**
            Create a new policy

        **Arguments**
            - name: The name of the policy.
            - rules: A list of Anchore PolicyRule elements (while creating/updating a policy, new rule IDs will be created backend side)
            - comment: A human-readable description.
            - bundleid: Target bundle. If not specified, the currently active bundle will be used.

        **Success Return Value**
            A JSON object containing the policy description.
        '''
        policy = {
            'name': name,
            'comment': comment,
            'rules': rules,
            'version': '1_0'
        }
        if bundleid:
            policy['policyBundleId'] = bundleid

        url = self.url + '/api/scanning/v1/policies'
        data = json.dumps(policy)
        res = requests.post(url, headers=self.hdrs, data=data, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def list_policy_bundles(self, detail=False):
        url = "{base_url}/api/scanning/v1/anchore/policies?detail={detail}".format(
            base_url=self.url,
            detail=str(detail))
        res = requests.get(url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def list_policies(self, bundleid=None):
        '''**Description**
            List the current set of scanning policies.

        **Arguments**
            - bundleid: Target bundle. If not specified, the currently active bundle will be used.

        **Success Return Value**
            A JSON object containing the list of policies.
        '''
        url = self.url + '/api/scanning/v1/policies'
        if bundleid:
            url += '?bundleId=' + bundleid

        res = requests.get(url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def get_policy(self, policyid, bundleid=None):
        '''**Description**
            Retrieve the policy with the given id in the targeted policy bundle

        **Arguments**
            - policyid: Unique identifier associated with this policy.
            - bundleid: Target bundle. If not specified, the currently active bundle will be used.

        **Success Return Value**
            A JSON object containing the policy description.
        '''
        ok, policies = self.list_policies(bundleid)
        if not ok:
            return [ok, policies]

        for policy in policies:
            if policy["id"] == policyid:
                return [True, policy]

        return [False, "Policy not found"]

    def update_policy(self, policyid, policy_description):
        '''**Description**
            Update the policy with the given id

        **Arguments**
            - policyid: Unique identifier associated with this policy.
            - policy_description: A dictionary with the policy description.

        **Success Return Value**
            A JSON object containing the policy description.
        '''
        url = self.url + '/api/scanning/v1/policies/' + policyid
        data = json.dumps(policy_description)
        res = requests.put(url, headers=self.hdrs, data=data, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def delete_policy(self, policyid, bundleid=None):
        '''**Description**
            Delete the policy with the given id in the targeted policy Bundle

        **Arguments**
            - policyid: Unique identifier associated with this policy.
            - policy_description: A dictionary with the policy description.
        '''
        url = self.url + '/api/scanning/v1/policies/' + policyid
        if bundleid:
            url += '?bundleId=' + bundleid

        res = requests.delete(url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.text]

    def add_alert(self, name, description=None, scope="", triggers={'failed': True, 'unscanned': True},
                  enabled=False, notification_channels=[]):
        '''**Description**
            Create a new alert

        **Arguments**
            - name: The name of the alert.
            - description: The descprition of the alert.
            - scope: An AND-composed string of predicates that selects the scope in which the alert will be applied. (like: 'host.domain = "example.com" and container.image != "alpine:latest"')
            - tiggers: A dict {str: bool} indicating wich triggers should be enabled/disabled. (default: {'failed': True, 'unscanned': True})
            - enabled: Whether this alert should actually be applied.
            - notification_channels: A list of notification channel ids.

        **Success Return Value**
            A JSON object containing the alert description.
        '''
        alert = {
            'name': name,
            'description': description,
            'triggers': triggers,
            'scope': scope,
            'enabled': enabled,
            'autoscan': True,
            'notificationChannelIds': notification_channels,
        }

        url = self.url + '/api/scanning/v1/alerts'
        data = json.dumps(alert)
        res = requests.post(url, headers=self.hdrs, data=data, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def list_alerts(self, limit=None, cursor=None):
        '''**Description**
            List the current set of scanning alerts.

        **Arguments**
            - limit: Maximum number of alerts in the response.
            - cursor: An opaque string representing the current position in the list of alerts. It's provided in the 'responseMetadata' of the list_alerts response.

        **Success Return Value**
            A JSON object containing the list of alerts.
        '''
        url = self.url + '/api/scanning/v1/alerts'
        if limit:
            url += '?limit=' + str(limit)
            if cursor:
                url += '&cursor=' + cursor

        res = requests.get(url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def get_alert(self, alertid):
        '''**Description**
            Retrieve the scanning alert with the given id

        **Arguments**
            - alertid: Unique identifier associated with this alert.

        **Success Return Value**
            A JSON object containing the alert description.
        '''
        url = self.url + '/api/scanning/v1/alerts/' + alertid
        res = requests.get(url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def update_alert(self, alertid, alert_description):
        '''**Description**
            Update the alert with the given id

        **Arguments**
            - alertid: Unique identifier associated with this alert.
            - alert_description: A dictionary with the alert description.

        **Success Return Value**
            A JSON object containing the alert description.
        '''
        url = self.url + '/api/scanning/v1/alerts/' + alertid
        data = json.dumps(alert_description)
        res = requests.put(url, headers=self.hdrs, data=data, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def delete_alert(self, policyid):
        '''**Description**
            Delete the alert with the given id

        **Arguments**
            - alertid: Unique identifier associated with this alert.
        '''
        url = self.url + '/api/scanning/v1/alerts/' + policyid
        res = requests.delete(url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.text]

    def get_subscriptions(self, subscription_type=None, subscription_key=None):
        '''**Description**
            Get the list of subscriptions

        **Arguments**
            - subscription_type: Type of subscription. Valid options:
                - 'tag_update': Receive notification when new image is pushed
                - 'policy_eval': Receive notification when image policy status changes
                - 'vuln_update': Receive notification when vulnerabilities are added, removed or modified
                - 'repo_update': Receive notification when a repo is updated
            - subscription_key: Fully qualified name of tag to subscribe to. Eg. docker.io/library/alpine:latest
        '''
        url = self.url + "/api/scanning/v1/anchore/subscriptions/"
        if subscription_key or subscription_type:
            url += "?"
            if subscription_key:
                url += "subscription_key={}&".format(subscription_key)
            if subscription_type:
                url += "subscription_type={}".format(subscription_type)
        res = requests.get(url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def activate_subscription(self, subscription_type, subscription_key):
        '''**Description**
            Activate a subscription

        **Arguments**
            - subscription_type: Type of subscription. Valid options:
                - 'tag_update': Receive notification when new image is pushed
                - 'policy_eval': Receive notification when image policy status changes
                - 'vuln_update': Receive notification when vulnerabilities are added, removed or modified
                - 'repo_update': Receive notification when a repo is updated
            - subscription_key: Fully qualified name of tag to subscribe to. Eg. docker.io/library/alpine:latest
        '''
        return self._update_subscription(subscription_type, subscription_key, True)

    def deactivate_subscription(self, subscription_type, subscription_key):
        '''**Description**
            Deactivate a subscription

        **Arguments**
            - subscription_type: Type of subscription. Valid options:
                - 'tag_update': Receive notification when new image is pushed
                - 'policy_eval': Receive notification when image policy status changes
                - 'vuln_update': Receive notification when vulnerabilities are added, removed or modified
                - 'repo_update': Receive notification when a repo is updated
            - subscription_key: Fully qualified name of tag to subscribe to. Eg. docker.io/library/alpine:latest
        '''
        return self._update_subscription(subscription_type, subscription_key, False)

    def delete_subscription(self, subscription_type, subscription_key):
        '''**Description**
            Delete a subscription

        **Arguments**
            - subscription_type: Type of subscription. Valid options:
                - 'tag_update': Receive notification when new image is pushed
                - 'policy_eval': Receive notification when image policy status changes
                - 'vuln_update': Receive notification when vulnerabilities are added, removed or modified
                - 'repo_update': Receive notification when a repo is updated
            - subscription_key: Fully qualified name of tag to subscribe to. Eg. docker.io/library/alpine:latest
        '''
        try:
            url = self._subscription_url(subscription_type, subscription_key)
        except Exception as err:
            return [False, err]

        res = requests.delete(url, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def _update_subscription(self, subscription_type, subscription_key, activate):
        try:
            url = self._subscription_url(subscription_type, subscription_key)
        except Exception as err:
            return [False, err]

        payload = {'active': activate, 'subscription_key': subscription_key, 'subscription_type': subscription_type}
        res = requests.put(url, data=json.dumps(payload), headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def _subscription_url(self, subscription_type, subscription_key):
        ok, res = self.get_subscriptions(subscription_type, subscription_key)
        if not ok:
            raise Exception(res)

        if len(res) != 1:
            raise Exception("Subscription {} doesn't exist".format(subscription_key))
        id = res[0].get("subscription_id", None)
        if not id:
            raise Exception("Subscription malformed")

        return self.url + "/api/scanning/v1/anchore/subscriptions/" + id

    def list_subscription(self):
        '''**Description**
            List all subscriptions

        **Arguments**
            - None

        **Success Return Value**
            A JSON object representing the list of subscriptions.
        '''
        return self.get_subscriptions()

    def list_runtime(self, scope="", skip_policy_evaluation=True, start_time=None, end_time=None):
        '''**Description**
            List runtime containers

        **Arguments**
            - scope: An AND-composed string of predicates that selects the scope in which the alert will be applied. (like: 'host.domain = "example.com" and container.image != "alpine:latest"')
            - skip_policy_evaluation: If true, no policy evaluations will be triggered for the images.
            - start_time: Start of the time range (integer of unix time).
            - end_time: End of the time range (integer of unix time).

        **Success Return Value**
            A JSON object representing the list of runtime containers.
        '''
        containers = {
            'scope': scope,
            'skipPolicyEvaluation': skip_policy_evaluation
        }
        if start_time or end_time:
            containers['time'] = {}
            containers['time']['from'] = int(start_time * 100000) if start_time else 0
            end_time = end_time if end_time else time.time()
            containers['time']['to'] = int(end_time * 1000000)

        url = self.url + '/api/scanning/v1/query/containers'
        data = json.dumps(containers)
        res = requests.post(url, headers=self.hdrs, data=data, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def _discover_inputimage_format(self, input_string):
        itype = None

        if re.match("^sha256:[0-9a-fA-F]{64}", input_string):
            itype = 'imageDigest'
        elif re.match("[0-9a-fA-F]{64}", input_string):
            itype = 'imageid'
        else:
            itype = 'tag'

        return itype

    def _discover_inputimage(self, input_string):
        patt = re.match(".*(sha256:.*)", input_string)
        if patt:
            urldigest = quote_plus(patt.group(1))
            return "digest", input_string, urldigest

        try:
            digest = unquote_plus(str(input_string))
            for tpe in ["sha256", "local"]:
                patt = re.match(".*({}:.*)".format(tpe), digest)
                if patt:
                    return "imageDigest", input_string, input_string
        except Exception:
            pass

        urldigest = None
        ret_type = "tag"
        ok, ret = self.get_image(input_string)
        if ok:
            image_record = ret[0]
            urldigest = image_record.get('imageDigest', None)
            for image_detail in image_record.get('image_detail', []):
                if input_string == image_detail.get('imageId', ''):
                    ret_type = "imageid"
                    break

        return ret_type, input_string, urldigest
