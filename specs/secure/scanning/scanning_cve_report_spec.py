import os

from expects import *
from mamba import *

from sdcclient import SdScanningClient
from specs import be_successful_api_call

with description("CVE Reports", "integration") as self:
    with before.all:
        self.client = SdScanningClient(sdc_url=os.getenv("SDC_SECURE_URL", "https://secure.sysdig.com"),
                                       token=os.getenv("SDC_SECURE_TOKEN"))
    with fcontext("when the CSV of static can be downloaded"):
        with it("is able to download it for OS vulnerabilities"):
            ok, csv = self.client.download_cve_report_csv(vuln_type="os", scope_type="static")

            expect((ok, csv)).to(be_successful_api_call)
            expect(csv).to(start_with("Image Name,Tag,Package Name,Package Version,Package Path,Severity,Fixed In,"
                                      "Vulnerability ID,Links,Image Digest,Runtime Metadata"))

        with it("is able to download it for non-OS vulnerabilities"):
            ok, csv = self.client.download_cve_report_csv(vuln_type="non-os", scope_type="static")

            expect((ok, csv)).to(be_successful_api_call)
            expect(csv).to(start_with("Image Name,Tag,Package Name,Package Version,Package Path,Severity,Fixed In,"
                                      "Vulnerability ID,Links,Image Digest,Runtime Metadata"))

    with context("when the CSV of runtime can be downloaded"):
        with it("is able to download it for OS vulnerabilities"):
            ok, csv = self.client.download_cve_report_csv(vuln_type="os", scope_type="runtime")

            expect((ok, csv)).to(be_successful_api_call)
            expect(csv).to(start_with("Image Name,Tag,Package Name,Package Version,Package Path,Severity,Fixed In,"
                                      "Vulnerability ID,Links,Image Digest,Runtime Metadata"))

        with it("is able to download it for non-OS vulnerabilities"):
            ok, csv = self.client.download_cve_report_csv(vuln_type="non-os", scope_type="runtime")

            expect((ok, csv)).to(be_successful_api_call)
            expect(csv).to(start_with("Image Name,Tag,Package Name,Package Version,Package Path,Severity,Fixed In,"
                                      "Vulnerability ID,Links,Image Digest,Runtime Metadata"))
