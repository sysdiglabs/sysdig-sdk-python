import base64
import hashlib
import json
import re
import requests

try:
    from urllib.parse import quote_plus, unquote_plus
except ImportError:
    from urllib import quote_plus, unquote_plus

from sdcclient._common import _SdcCommon


class SdScanningClient(_SdcCommon):

    def __init__(self, token="", sdc_url='https://secure.sysdig.com', ssl_verify=True):
        super(SdScanningClient, self).__init__(token, sdc_url, ssl_verify)

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

    def import_image(self, image_data):
        '''**Description**
            Import an image from the scanner export

        **Arguments**
            - image_data: A JSON with the image information.

        **Success Return Value**
            A JSON object representing the image that was imported.
        '''
        url = self.url + "/api/scanning/v1/anchore/imageimport"
        res = requests.post(url, data=json.dumps(image_data), headers=self.hdrs, verify=self.ssl_verify)
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

    def activate_subscription(self, subscription_type, subscription_key):
        '''**Description**
            Activate a subscription

        **Arguments**
            - subscription_type: Type of subscription. Valid options:
                - 'tag_update': Receive notification when new image is pushed
                - 'policy_eval': Receive notification when image policy status changes
                - 'vuln_update': Receive notification when vulnerabilities are added, removed or modified
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
            - subscription_key: Fully qualified name of tag to subscribe to. Eg. docker.io/library/alpine:latest
        '''
        return self._update_subscription(subscription_type, subscription_key, False)

    def _update_subscription(self, subscription_type, subscription_key, activate):
        hashstr = '+'.join([self.token, subscription_key, subscription_type]).encode('utf-8')
        subscription_id = hashlib.md5(hashstr).hexdigest()
        url = self.url + "/api/scanning/v1/anchore/subscriptions/" + subscription_id
        payload = {'active': activate, 'subscription_key': subscription_key, 'subscription_type': subscription_type}

        res = requests.put(url, data=json.dumps(payload), headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, res.json()]

    def list_subscription(self):
        '''**Description**
            List all subscriptions

        **Arguments**
            - None

        **Success Return Value**
            A JSON object representing the list of subscriptions.
        '''
        url = self.url + "/api/scanning/v1/anchore/subscriptions"
        res = requests.get(url, headers=self.hdrs, verify=self.ssl_verify)
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
