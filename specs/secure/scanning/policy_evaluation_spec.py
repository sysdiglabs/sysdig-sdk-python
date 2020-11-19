import os
from datetime import datetime

from expects import equal, expect, be_empty, be_above_or_equal, be_an, have_keys, not_
from mamba import before, context, description, it

from sdcclient import SdScanningClient
from specs import be_successful_api_call

with description("Policy Evaluation", "integration") as self:
    with before.all:
        self.client = SdScanningClient(sdc_url=os.getenv("SDC_SECURE_URL", "https://secure.sysdig.com"),
                                       token=os.getenv("SDC_SECURE_TOKEN"))

    with it("is able to retrieve the results for all the policies"):
        image_name = "alpine:latest"
        ok, res = self.client.get_image_scanning_results(image_name)

        expect((ok, res)).to(be_successful_api_call)
        expect(res).to(
            have_keys("image_digest", "image_id", "stop_results",
                      total_warn=be_above_or_equal(0), total_stop=be_above_or_equal(0),
                      last_evaluation=be_an(datetime),
                      status="pass", image_tag="docker.io/alpine:latest",
                      policy_id="*", policy_name="All policies",
                      warn_results=not_(be_empty))
        )

    with it("is able to retrieve the results for the default policy"):
        image_name = "alpine:latest"
        policy_id = "default"
        ok, res = self.client.get_image_scanning_results(image_name, policy_id)

        expect((ok, res)).to(be_successful_api_call)
        expect(res).to(
            have_keys("image_digest", "image_id", "stop_results",
                      total_warn=be_above_or_equal(0), total_stop=be_above_or_equal(0),
                      last_evaluation=be_an(datetime),
                      status="pass", image_tag="docker.io/alpine:latest",
                      policy_id="*", policy_name="All policies",
                      warn_results=not_(be_empty))
        )

    with context("but the image has not been scanned yet"):
        with it("returns an error saying that the image has not been found"):
            image_name = "unknown_image"
            ok, res = self.client.get_image_scanning_results(image_name)

            expect((ok, res)).to_not(be_successful_api_call)
            expect(res).to(equal("could not retrieve image digest for the given image name, "
                                 "ensure that the image has been scanned"))

    with context("but the provided policy id does not exist"):
        with it("returns an error saying that the policy id is not found"):
            image_name = "alpine"
            policy_id = "unknown_policy_id"
            ok, res = self.client.get_image_scanning_results(image_name, policy_id)

            expect((ok, res)).to_not(be_successful_api_call)
            expect(res).to(equal("the specified policy ID doesn't exist"))
