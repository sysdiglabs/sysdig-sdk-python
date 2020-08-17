import json
import os

from expects import expect
from mamba import before, description, after, it

from sdcclient import SdSecureClientV1
from specs import be_successful_api_call

_POLICY_NAME = "Test - Launch Suspicious Network Tool on Host"
_POLICY_DESCRIPTION = "Detect network tools launched on the host"
_POLICY_RULES_REGEX = "Launch Suspicious Network Tool on Host"
_POLICY_ACTIONS = [
    {
        "type": "POLICY_ACTION_STOP",
        "msg": ""
    },
    {
        "type": "POLICY_ACTION_PAUSE",
        "msg": ""
    },
    {
        "type": "POLICY_ACTION_CAPTURE",
        "beforeEventNs": 5000000000,
        "afterEventNs": 18000000000,
        "isLimitedToContainer": True
    }
]
def policy_json():
    return """\
{
  "name": "%s",
  "description": "%s", 
  "notificationChannelIds": [], 
  "severity": 0, 
  "hostScope": true, 
  "enabled": true, 
  "actions": %s, 
  "falcoConfiguration": {
    "fields": [], 
    "ruleNameRegEx": "%s", 
    "onDefault": "DEFAULT_MATCH_EFFECT_NEXT"
  }, 
  "policyEventsCount": 0,  
  "isManual": true, 
  "isBuiltin": true, 
  "containerScope": true, 
  "modifiedOn": 1597646118000, 
  "createdOn": 1597646118000
}
""" % (_POLICY_NAME, _POLICY_DESCRIPTION, json.dumps(_POLICY_ACTIONS), _POLICY_RULES_REGEX)

with description("Policies v1") as self:
    with before.all:
        self.clientV1 = SdSecureClientV1(sdc_url=os.getenv("SDC_SECURE_URL", "https://secure.sysdig.com"),
                                     token=os.getenv("SDC_SECURE_TOKEN"))
    with after.each:
        self.cleanup_policies()

    def cleanup_policies(self):
        _, res = self.clientV1.list_policies()
        for policy in res['policies']:
            if str(policy["name"]).startswith("Test - "):
                ok, res = self.clientV1.delete_policy_id(policy["id"])
                expect((ok, res)).to(be_successful_api_call)

    with it("is able to list all existing policies"):
        ok, res = self.clientV1.list_policies()
        expect((ok, res)).to(be_successful_api_call)

    with it("is able to list all policies priorities"):
        ok, res = self.clientV1.get_policy_priorities()
        expect((ok, res)).to(be_successful_api_call)

    with it("is able to change the evaluation order of policies"):
        ok, res = self.clientV1.get_policy_priorities()
        random.shuffle(res['priorities']['policyIds'])
        ok, res = self.clientV1.set_policy_priorities(json.dumps(res))
        expect((ok, res)).to(be_successful_api_call)

    with it("is able to add a policy from JSON"):
        call = self.clientV1.add_policy(policy_json())
        expect(call).to(be_successful_api_call)

    with it("is able to get a policy"):
        ok, res = self.clientV1.list_policies()
        name = res['policies'][0]['name']
        call = self.clientV1.get_policy(name)
        expect(call).to(be_successful_api_call)

    with it("is able to update a policy from JSON"):
        ok, res = self.clientV1.list_policies()
        policy_json = res['policies'][0]
        policy_json['description'] = "Updated description"
        call = self.clientV1.update_policy(json.dumps(policy_json))
        expect(call).to(be_successful_api_call)

    with it("is able to delete all policies"):
        ok, res = self.clientV1.list_policies()
        expect((ok, res)).to(be_successful_api_call)  

    with it("is able to delete all policies at once"):
        ok, res = self.clientV1.delete_all_policies()
        expect((ok, res)).to(be_successful_api_call)

    with it("is able to create the default policies"):
        ok, res = self.clientV1.create_default_policies()
        expect((ok, res)).to(be_successful_api_call)
