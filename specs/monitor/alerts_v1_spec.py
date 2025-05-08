import os

from expects import expect, have_key, have_keys, have_len
from expects.matchers.built_in import be_above_or_equal
from mamba import description, before, it, context, after

from sdcclient import SdMonitorClient
from specs import be_successful_api_call

_ALERT_NAME = "Test - Alert"
_ALERT_DESCRIPTION = "This alert was automatically created using the Sysdig SDK Python"

with description("Alerts v1", "integration") as self:
    with before.all:
        self.client = SdMonitorClient(
            sdc_url=os.getenv("SDC_MONITOR_URL", "https://app.sysdigcloud.com"),
            token=os.getenv("SDC_MONITOR_TOKEN"),
        )

    with before.each:
        self.cleanup_alerts()

    with after.each:
        self.cleanup_alerts()

    def cleanup_alerts(self):
        ok, res = self.client.get_alerts()
        expect((ok, res)).to(be_successful_api_call)

        for alert in res["alerts"]:
            if str(alert["name"]).startswith("Test -"):
                call = self.client.delete_alert(alert)
                expect(call).to(be_successful_api_call)

    def create_test_alert(self):
        ok, res = self.client.create_alert(
            name=_ALERT_NAME,
            description=_ALERT_DESCRIPTION,
            severity=6,
            for_atleast_s=60,
            condition="avg(cpu.used.percent) > 80",
            # We want to check this metric for every process on every machine.
            segmentby=["host.mac", "proc.name"],
            segment_condition="ANY",
            # if there is more than one tomcat process, this alert will fire when a single one of them crosses the
            # 80% threshold.
            user_filter='proc.name = "tomcat"',
            enabled=False,
        )

        if ok:
            self.test_alert = res["alert"]
        return ok, res

    with it("is able to create an alert"):
        ok, res = self.create_test_alert()
        expect((ok, res)).to(be_successful_api_call)
        expect(res).to(have_key("alert", have_keys("id", "name")))

    with it("is able to remove the alert"):
        self.create_test_alert()

        call = self.client.delete_alert(self.test_alert)
        expect(call).to(be_successful_api_call)

    with context("with existing alerts"):
        with before.each:
            self.create_test_alert()

        with it("is able to list all existing alerts"):
            ok, res = self.client.get_alerts()
            expect((ok, res)).to(be_successful_api_call)
            expect(res).to(have_key("alerts", have_len(be_above_or_equal(1))))

        with it("is able to update an alert"):
            self.test_alert["enabled"] = not self.test_alert["enabled"]

            call = self.client.update_alert(self.test_alert)
            expect(call).to(be_successful_api_call)
