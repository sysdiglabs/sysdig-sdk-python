import os

from expects import expect, contain, have_keys, equal
from mamba import before, it, context, description

from sdcclient import SdScanningClient
from specs import be_successful_api_call

with description("Query Image Content", "integration") as self:
    with before.each:
        self.client = SdScanningClient(sdc_url=os.getenv("SDC_SECURE_URL", "https://secure.sysdig.com"),
                                       token=os.getenv("SDC_SECURE_TOKEN"))
        self.image_to_scan = "quay.io/sysdig/agent:latest"

    with it("is able to retrieve the OS contents"):
        ok, res = self.client.query_image_content(self.image_to_scan, "os")

        expect((ok, res)).to(be_successful_api_call)
        expect(res["content"]).to(contain(have_keys("license", "origin", "package", "size", "type", "version")))
        expect(res["content_type"]).to(equal("os"))

    with it("is able to retrieve the npm contents"):
        ok, res = self.client.query_image_content(self.image_to_scan, "npm")

        expect((ok, res)).to(be_successful_api_call)
        expect(res["content_type"]).to(equal("npm"))

    with it("is able to retrieve the gem contents"):
        ok, res = self.client.query_image_content(self.image_to_scan, "gem")

        expect((ok, res)).to(be_successful_api_call)
        expect(res["content_type"]).to(equal("gem"))

    with it("is able to retrieve the python contents"):
        ok, res = self.client.query_image_content(self.image_to_scan, "python")

        expect((ok, res)).to(be_successful_api_call)
        expect(res["content_type"]).to(equal("python"))

    with it("is able to retrieve the java contents"):
        ok, res = self.client.query_image_content(self.image_to_scan, "java")

        expect((ok, res)).to(be_successful_api_call)
        expect(res["content_type"]).to(equal("java"))

    with it("is able to retrieve the files contents"):
        ok, res = self.client.query_image_content(self.image_to_scan, "files")

        expect((ok, res)).to(be_successful_api_call)
        expect(res["content"]).to(
            contain(have_keys("filename", "gid", "linkdest", "mode", "sha256", "size", "type", "uid")))
        expect(res["content_type"]).to(equal("files"))

    with context("when the type is not in the supported list"):
        with it("returns an error indicating the type is incorrect"):
            ok, res = self.client.query_image_content(self.image_to_scan, "Unknown")

            expect((ok, res)).not_to(be_successful_api_call)
            expect(res).to(equal(
                "unsupported type provided: unknown, must be one of ['os', 'files', 'npm', 'gem', 'python', 'java']"))
