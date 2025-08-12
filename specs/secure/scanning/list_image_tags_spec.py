import os

from expects import expect, contain, have_keys
from mamba import before, description, it

from sdcclient import SdScanningClient
from specs import be_successful_api_call

with description("Scanning list_image_tags") as self:
    with before.all:
        self.client = SdScanningClient(
            sdc_url=os.getenv("SDC_SECURE_URL", "https://secure.sysdig.com"),
            token=os.getenv("SDC_SECURE_TOKEN"),
        )

    with it("is able to retrieve all the image tags"):
        ok, res = self.client.list_image_tags()

        expect((ok, res)).to(be_successful_api_call)
        expect(res).to(
            contain(
                have_keys(
                    "analyzed_at",
                    "created_at",
                    "fulltag",
                    "imageDigest",
                    "imageId",
                    "parentDigest",
                    "tag_detected_at",
                    "analysis_status",
                )
            )
        )
