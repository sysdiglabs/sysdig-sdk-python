import os

from expects import *
from mamba import *

from sdcclient import SdScanningClient
from specs import be_successful_api_call

with description("Scanning Alerts") as self:
    with before.all:
        self.client = SdScanningClient(sdc_url=os.getenv("SDC_SECURE_URL", "https://secure.sysdig.com"),
                                       token=os.getenv("SDC_SECURE_TOKEN"))

    with after.all:
        ok, res = self.client.list_alerts()
        expect((ok, res)).to(be_successful_api_call)

        for alert in res["alerts"]:
            self.client.delete_alert(alert["alertId"])

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

    with context("when creating a repository alert"):
        with it("creates an alert with new image analyzed trigger"):
            ok, res = self.client.add_repository_alert(
                    name="A name",
                    registry="registry",
                    repository="repository",
                    tag="latest",
                    description="A description",
                    triggers=[SdScanningClient.RepositoryAlertTrigger.new_image_analyzed]
            )

            expect((ok, res)).to(be_successful_api_call)
            expect(res).to(have_keys(name="A name", description="A description", scope="", triggers=have_keys(analysis_update=be_true)))

        with it("creates an alert with scan result change trigger as 'Pass > Fail'"):
            ok, res = self.client.add_repository_alert(
                    name="A name",
                    registry="registry",
                    repository="repository",
                    tag="latest",
                    description="A description",
                    triggers=[SdScanningClient.RepositoryAlertTrigger.scan_result_change_fail]
            )

            expect((ok, res)).to(be_successful_api_call)
            expect(res).to(have_keys(name="A name", description="A description", scope="", triggers=have_keys(policy_eval=be_true), onlyPassFail=be_true))

        with it("creates an alert with scan result change trigger as 'Any Change'"):
            ok, res = self.client.add_repository_alert(
                    name="A name",
                    registry="registry",
                    repository="repository",
                    tag="latest",
                    description="A description",
                    triggers=[SdScanningClient.RepositoryAlertTrigger.scan_result_change_any]
            )

            expect((ok, res)).to(be_successful_api_call)
            expect(res).to(have_keys(name="A name", description="A description", scope="", triggers=have_keys(policy_eval=be_true), onlyPassFail=be_false))

        with it("creates an alert with cve update trigger"):
            ok, res = self.client.add_repository_alert(
                    name="A name",
                    registry="registry",
                    repository="repository",
                    tag="latest",
                    description="A description",
                    triggers=[SdScanningClient.RepositoryAlertTrigger.cve_update]
            )

            expect((ok, res)).to(be_successful_api_call)
            expect(res).to(have_keys(name="A name", description="A description", scope="", triggers=have_keys(vuln_update=be_true)))

        with it("creates an alert with multiple triggers"):
            ok, res = self.client.add_repository_alert(
                    name="A name",
                    registry="registry",
                    repository="repository",
                    tag="latest",
                    description="A description",
                    triggers=[SdScanningClient.RepositoryAlertTrigger.new_image_analyzed,
                              SdScanningClient.RepositoryAlertTrigger.scan_result_change_fail,
                              SdScanningClient.RepositoryAlertTrigger.cve_update]
            )

            expect((ok, res)).to(be_successful_api_call)
            expect(res).to(have_keys(name="A name", description="A description", scope="", triggers=have_keys(analysis_update=be_true, policy_eval=be_true, vuln_update=be_true), onlyPassFail=be_true))

    with it("removes an alert correctly"):
        ok, res = self.client.add_runtime_alert(
                name="A name",
                description="A description",
                scope="",
                triggers=[SdScanningClient.RuntimeAlertTrigger.unscanned_image]
        )

        expect((ok, res)).to(be_successful_api_call)

        alert_id = res["alertId"]
        ok, res = self.client.delete_alert(alert_id)
        expect((ok, res)).to(be_successful_api_call)

        ok, res = self.client.list_alerts()
        expect((ok, res)).to(be_successful_api_call)
        expect(res["alerts"]).to_not(contain(have_keys(id=alert_id)))

    with it("retrieves an alert correctly"):
        ok, res = self.client.add_runtime_alert(
                name="A name",
                description="A description",
                scope="",
                triggers=[SdScanningClient.RuntimeAlertTrigger.unscanned_image]
        )
        expect((ok, res)).to(be_successful_api_call)

        alert_id = res["alertId"]
        ok, res = self.client.get_alert(alert_id)
        expect((ok, res)).to(be_successful_api_call)
        expect(res).to(have_keys(name="A name", description="A description", scope="", triggers=have_keys(unscanned=be_true)))

    with it("updates a runtime alert correctly"):
        ok, res = self.client.add_runtime_alert(
                name="A name",
                description="A description",
                scope="",
                triggers=[SdScanningClient.RuntimeAlertTrigger.unscanned_image]
        )
        expect((ok, res)).to(be_successful_api_call)
        expect(res).to(have_keys(name="A name", description="A description", scope="", triggers=have_keys(unscanned=be_true)))

        alert_id = res["alertId"]
        ok, res = self.client.update_runtime_alert(
                id=alert_id,
                name="An updated name",
                description="An updated description",
                scope="agent.id = 'foo'",
                triggers=[SdScanningClient.RuntimeAlertTrigger.scan_result_change_fail]
        )
        expect((ok, res)).to(be_successful_api_call)
        expect(res).to(have_keys(name="An updated name", description="An updated description", scope="agent.id = 'foo'", triggers=have_keys(unscanned=be_false, policy_eval=be_true), onlyPassFail=be_true))

    with it("updates a repository alert correctly"):
        ok, res = self.client.add_repository_alert(
                name="A name",
                registry="registry",
                repository="repository",
                tag="latest",
                description="A description",
                triggers=[SdScanningClient.RepositoryAlertTrigger.new_image_analyzed]
        )

        expect((ok, res)).to(be_successful_api_call)
        expect(res).to(have_keys(name="A name", description="A description",
                                 repositories=contain_exactly(have_keys(registry="registry", repository="repository", tag="latest")),
                                 triggers=have_keys(analysis_update=be_true)))

        alert_id = res["alertId"]
        ok, res = self.client.update_repository_alert(
                id=alert_id,
                name="An updated name",
                registry="new_registry",
                repository="new_repository",
                tag="v1",
                description="An updated description",
                triggers=[SdScanningClient.RepositoryAlertTrigger.scan_result_change_fail]
        )
        expect((ok, res)).to(be_successful_api_call)
        expect(res).to(have_keys(name="An updated name",
                                 description="An updated description",
                                 repositories=contain_exactly(have_keys(registry="new_registry", repository="new_repository", tag="v1")),
                                 triggers=have_keys(unscanned=be_false, policy_eval=be_true), onlyPassFail=be_true))
