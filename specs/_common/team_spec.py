import os
from expects import expect, equal
from mamba import before, description, it
from sdcclient import SdSecureClient, SdMonitorClient
from specs import be_successful_api_call

with description("Teams", "integration", "teams") as self:
    with before.all:
        self.secure_client = SdSecureClient(
                sdc_url=os.getenv("SDC_SECURE_URL", "https://secure.sysdig.com"),
                token=os.getenv("SDC_SECURE_TOKEN")
        )
        self.monitor_client = SdMonitorClient(
                sdc_url=os.getenv("SDC_MONITOR_URL", "https://app.sysdigcloud.com"),
                token=os.getenv("SDC_MONITOR_TOKEN")
        )

    with it("is able to list only monitor teams"):
        ok, teams = self.monitor_client.get_teams()
        expect((ok, teams)).to(be_successful_api_call)

        secure_teams = [t for t in teams if 'SDS' in t['products']]
        expect(len(secure_teams)).to(equal(0))

    with it("is able to list only secure teams"):
        ok, teams = self.secure_client.get_teams()
        expect((ok, teams)).to(be_successful_api_call)

        monitor_teams = [t for t in teams if 'SDC' in t['products']]
        expect(len(monitor_teams)).to(equal(0))
