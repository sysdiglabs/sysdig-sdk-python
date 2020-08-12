import json
import os

from expects import expect
from mamba import before, description, after, it

from sdcclient import SdSecureClient
from specs import be_successful_api_call

_POLICY_NAME = "Test - Terminal shell in container"
_POLICY_DESCRIPTION = "A shell was spawned by a program in a container with an attached terminal."
_POLICY_RULES = ["Terminal shell in container"]
_POLICY_ACTIONS = [{
    "type": "POLICY_ACTION_CAPTURE",
    "name": "Terminal shell in container",
    "filter": "",
    "storageType": "S3",
    "bucketName": "",
    "isLimitedToContainer": False,
    "beforeEventNs": 10000000000,
    "afterEventNs": 20000000000
}]


def policy_json():
    return """\
{
  "name": "%s",
  "description": "%s",
  "origin": "Secure UI",
  "versionId": "0.0.0",
  "severity": 0,
  "enabled": true,
  "ruleNames": %s,
  "notificationChannelIds": [],
  "actions": %s,
  "createdOn": 1596902934000,
  "modifiedOn": 1597138586000
}
""" % (_POLICY_NAME, _POLICY_DESCRIPTION, json.dumps(_POLICY_RULES), json.dumps(_POLICY_ACTIONS))


with description("Policies v2") as self:
    with before.all:
        self.client = SdSecureClient(sdc_url=os.getenv("SDC_SECURE_URL", "https://secure.sysdig.com"),
                                     token=os.getenv("SDC_SECURE_TOKEN"))
    with after.each:
        self.cleanup_policies()


    def cleanup_policies(self):
        _, res = self.client.list_policies()
        for policy in res:
            if str(policy["name"]).startswith("Test - "):
                ok, res = self.client.delete_policy_id(policy["id"])
                expect((ok, res)).to(be_successful_api_call)


    with it("is able to list all existing policies"):
        ok, res = self.client.list_policies()
        expect((ok, res)).to(be_successful_api_call)

    with it("is able to add a policy from JSON"):
        call = self.client.add_policy_json(policy_json())
        expect(call).to(be_successful_api_call)

    with it("is able to create a policy with parameters"):
        ok, res = self.client.add_policy(name=_POLICY_NAME,
                                         description=_POLICY_DESCRIPTION,
                                         rule_names=_POLICY_RULES,
                                         actions=_POLICY_ACTIONS)

        expect((ok, res)).to(be_successful_api_call)

    with it("is able to create the default policies"):
        ok, res = self.client.create_default_policies()
        expect((ok, res)).to(be_successful_api_call)
