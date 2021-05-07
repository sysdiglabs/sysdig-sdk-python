import os

from expects import expect, contain, have_keys
from mamba import before, description, it

from sdcclient import SdScanningClient
from specs import be_successful_api_call

with description("Scanning list_images") as self:
    with before.all:
        self.client = SdScanningClient(sdc_url=os.getenv("SDC_SECURE_URL", "https://secure.sysdig.com"),
                                       token=os.getenv("SDC_SECURE_TOKEN"))
    with it("is able to list all the scanned images"):
        ok, res = self.client.list_images()

        expect((ok, res)).to(be_successful_api_call)
        expect(res).to(contain(
            have_keys("annotations", "imageDigest", "last_updated", "analysis_status", "image_content", "image_detail",
                      "image_status", "parentDigest", "userId", "created_at")))
