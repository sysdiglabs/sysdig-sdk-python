import os
from datetime import datetime

from expects import be_above_or_equal, be_an, equal, expect, have_keys
from mamba import before, context, description, it

from sdcclient import SdScanningClient
from specs import be_successful_api_call

with description("Policy Evaluation", "integration") as self:
    with before.all:
        self.client = SdScanningClient(sdc_url=os.getenv("SDC_SECURE_URL", "https://secure.sysdig.com"),
                                       token=os.getenv("SDC_SECURE_TOKEN"))
        self.image_name = "quay.io/sysdig/agent:latest"

    with it("is able to retrieve the results for all the policies"):
        ok, res = self.client.get_image_scanning_results(self.image_name)

        expect((ok, res)).to(be_successful_api_call)
        expect(res).to(
            have_keys("image_digest", "image_id", "stop_results", "warn_results",
                      total_warn=be_above_or_equal(0), total_stop=be_above_or_equal(0),
                      last_evaluation=be_an(datetime),
                      status="pass", image_tag=self.image_name,
                      policy_id="*", policy_name="All policies")
        )

    with it("is able to retrieve the results for the default policy"):
        policy_id = "default"
        ok, res = self.client.get_image_scanning_results(self.image_name, policy_id)

        expect((ok, res)).to(be_successful_api_call)
        expect(res).to(
            have_keys("image_digest", "image_id", "stop_results", "warn_results",
                      total_warn=be_above_or_equal(0), total_stop=be_above_or_equal(0),
                      last_evaluation=be_an(datetime),
                      status="pass", image_tag=self.image_name,
                      policy_id="default", policy_name="DefaultPolicy")
        )

    with context("but the image has not been scanned yet"):
        with it("returns an error saying that the image has not been found"):
            ok, res = self.client.get_image_scanning_results("unknown_image")

            expect((ok, res)).to_not(be_successful_api_call)
            expect(res).to(equal("could not retrieve image digest for the given image name, "
                                 "ensure that the image has been scanned"))

    with context("but the provided policy id does not exist"):
        with it("returns an error saying that the policy id is not found"):
            policy_id = "unknown_policy_id"
            ok, res = self.client.get_image_scanning_results(self.image_name, policy_id)

            expect((ok, res)).to_not(be_successful_api_call)
            expect(res).to(equal("the specified policy ID doesn't exist"))
