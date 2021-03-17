import json
import os

from expects import expect
from mamba import before, after, it, description

from sdcclient import SdSecureClient
from sdcclient.secure import policy_action_capture
from specs import be_successful_api_call

_POLICY_NAME = "Test - Terminal shell in container"
_POLICY_DESCRIPTION = "A shell was spawned by a program in a container with an attached terminal."
_POLICY_RULES = ["Terminal shell in container"]
_POLICY_ACTIONS = [policy_action_capture(file_name="TerminalShellInContainer", secs_before=10, secs_after=20)]


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


with description("Policies v2", "integration") as self:
    with before.all:
        self.client = SdSecureClient(sdc_url=os.getenv("SDC_SECURE_URL", "https://secure.sysdig.com"),
                                     token=os.getenv("SDC_SECURE_TOKEN"))

    with before.each:
        self.cleanup_policies()

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
                                         actions=_POLICY_ACTIONS,
                                         type="falco")

        expect((ok, res)).to(be_successful_api_call)

    with it("is able to delete all policies"):
        _, policies = self.client.list_policies()

        for policy in policies:
            ok, res = self.client.delete_policy_id(policy['id'])
            expect((ok, res)).to(be_successful_api_call)

    with it("is able to create the default policies"):
        ok, res = self.client.create_default_policies()
        expect((ok, res)).to(be_successful_api_call)
