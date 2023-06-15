import os
import uuid
from expects import expect, equal
from mamba import before, after, description, it
from sdcclient import SdSecureClient, SdMonitorClient
from specs import be_successful_api_call

TEAM_PREFIX_NAME = 'sysdig-sdk - '

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

    with before.each:
        self.cleanup_teams()

    with after.each:
        self.cleanup_teams()

    def cleanup_teams(self):
        ok, secure_teams = self.secure_client.get_teams()
        expect((ok, secure_teams)).to(be_successful_api_call)

        for team in [t for t in secure_teams if t['name'].startswith(TEAM_PREFIX_NAME)]:
            self.secure_client.delete_team(team['name'])

        ok, monitor_teams = self.monitor_client.get_teams()
        expect((ok, secure_teams)).to(be_successful_api_call)

        for team in [t for t in monitor_teams if t['name'].startswith(TEAM_PREFIX_NAME)]:
            self.monitor_client.delete_team(team['name'])

    with it("it should list only monitor teams"):
        ok, team = self.secure_client.create_team(f'{TEAM_PREFIX_NAME}{uuid.uuid4()}')
        expect((ok, team)).to(be_successful_api_call)

        ok, teams = self.monitor_client.get_teams()
        expect((ok, teams)).to(be_successful_api_call)

        secure_teams = [t for t in teams if 'SDS' in t['products']]
        expect(len(secure_teams)).to(equal(0))

    with it("it should list only secure teams"):
        ok, team = self.monitor_client.create_team(f'{TEAM_PREFIX_NAME}{uuid.uuid4()}')
        expect((ok, team)).to(be_successful_api_call)

        ok, teams = self.secure_client.get_teams()
        expect((ok, teams)).to(be_successful_api_call)

        monitor_teams = [t for t in teams if 'SDC' in t['products']]
        expect(len(monitor_teams)).to(equal(0))
