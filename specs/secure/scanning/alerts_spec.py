import os

from expects import *
from mamba import *

from sdcclient import SdScanningClient
from specs import be_successful_api_call

with description("Scanning Alerts") as self:
    with before.all:
        self.client = SdScanningClient(sdc_url=os.getenv("SDC_SECURE_URL", "https://secure.sysdig.com"),
                                       token=os.getenv("SDC_SECURE_TOKEN"))
    with it("lists all the scanning alerts"):
        ok, res = self.client.add_runtime_alert(
                name="A name",
                description="A description",
                scope="",
                triggers=[SdScanningClient.RuntimeAlertTrigger.unscanned_image]
        )
        expect((ok, res)).to(be_successful_api_call)

        ok, res = self.client.list_alerts()
        expect((ok, res)).to(be_successful_api_call)
        expect(res["alerts"]).to_not(be_empty)
        expect(res["alerts"]).to(contain(have_keys("customerId", "teamId", "alertId", "enabled", "type", "name", "description", "scope", "repositories", "triggers", "autoscan", "onlyPassFail", "skipEventSend", "notificationChannelIds")))

    with context("when creating a runtime alert"):
        with it("creates an alert with unscanned image trigger"):
            ok, res = self.client.add_runtime_alert(
                    name="A name",
                    description="A description",
                    scope="",
                    triggers=[SdScanningClient.RuntimeAlertTrigger.unscanned_image]
            )

            expect((ok, res)).to(be_successful_api_call)
            expect(res).to(have_keys(name="A name", description="A description", scope="", triggers=have_keys(unscanned=be_true)))

        with it("creates an alert with scan result change trigger as 'Pass > Fail'"):
            ok, res = self.client.add_runtime_alert(
                    name="A name",
                    description="A description",
                    scope="",
                    triggers=[SdScanningClient.RuntimeAlertTrigger.scan_result_change_fail]
            )

            expect((ok, res)).to(be_successful_api_call)
            expect(res).to(have_keys(name="A name", description="A description", scope="", triggers=have_keys(policy_eval=be_true), onlyPassFail=be_true))

        with it("creates an alert with scan result change trigger as 'Any Change'"):
            ok, res = self.client.add_runtime_alert(
                    name="A name",
                    description="A description",
                    scope="",
                    triggers=[SdScanningClient.RuntimeAlertTrigger.scan_result_change_any]
            )

            expect((ok, res)).to(be_successful_api_call)
            expect(res).to(have_keys(name="A name", description="A description", scope="", triggers=have_keys(policy_eval=be_true), onlyPassFail=be_false))

        with it("creates an alert with cve update trigger"):
            ok, res = self.client.add_runtime_alert(
                    name="A name",
                    description="A description",
                    scope="",
                    triggers=[SdScanningClient.RuntimeAlertTrigger.cve_update]
            )

            expect((ok, res)).to(be_successful_api_call)
            expect(res).to(have_keys(name="A name", description="A description", scope="", triggers=have_keys(vuln_update=be_true)))

        with it("creates an alert with multiple triggers"):
            ok, res = self.client.add_runtime_alert(
                    name="A name",
                    description="A description",
                    scope="",
                    triggers=[SdScanningClient.RuntimeAlertTrigger.unscanned_image,
                              SdScanningClient.RuntimeAlertTrigger.scan_result_change_fail,
                              SdScanningClient.RuntimeAlertTrigger.cve_update]
            )

            expect((ok, res)).to(be_successful_api_call)
            expect(res).to(have_keys(name="A name", description="A description", scope="", triggers=have_keys(unscanned=be_true, policy_eval=be_true, vuln_update=be_true), onlyPassFail=be_true))
