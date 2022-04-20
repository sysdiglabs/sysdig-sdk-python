import datetime
import os

from expects import be_above, be_empty, contain, expect, have_keys, have_len
from mamba import _it, before, context, description, it

from sdcclient.secure import ActivityAuditClientV1 as ActivityAuditClient, ActivityAuditDataSource
from specs import be_successful_api_call

with description("Activity Audit v1", "integration") as self:
    with before.all:
        self.client = ActivityAuditClient(sdc_url=os.getenv("SDC_SECURE_URL", "https://secure.sysdig.com"),
                                          token=os.getenv("SDC_SECURE_TOKEN"))

    with it("is able to list the most recent commands with the default parameters"):
        ok, res = self.client.list_events()

        expect((ok, res)).to(be_successful_api_call)
        expect(res).to_not(be_empty)

    with context("when listing the most recent commands with a limit of 5"):
        with it("retrieves the 5 events"):
            ok, res = self.client.list_events(limit=5)

            expect((ok, res)).to(be_successful_api_call)
            expect(res).to_not(have_len(5))

    with context("when listing the events from the last 3 days"):
        with it("retrieves all the events"):
            three_days_ago = datetime.datetime.now() - datetime.timedelta(days=3)
            ok, res = self.client.list_events(from_date=three_days_ago)

            expect((ok, res)).to(be_successful_api_call)
            expect(res).to_not(be_empty)

    with context("when listing events from a specific type"):
        with it("retrieves the events of this event type only"):
            ok, res = self.client.list_events(data_sources=[ActivityAuditDataSource.CMD])

            expect((ok, res)).to(be_successful_api_call)
            expect(res).to(contain(have_keys(type=ActivityAuditDataSource.CMD)))
            expect(res).to_not(contain(have_keys(type=ActivityAuditDataSource.KUBE_EXEC)))
            expect(res).to_not(contain(have_keys(type=ActivityAuditDataSource.FILE)))
            expect(res).to_not(contain(have_keys(type=ActivityAuditDataSource.NET)))

    with context("when retrieving the inner events of a traceable event"):
        with _it("retrieves the trace of these events"):
            ok, res = self.client.list_events(data_sources=[ActivityAuditDataSource.KUBE_EXEC])
            expect((ok, res)).to(be_successful_api_call)

            expect(res).to(contain(have_keys(traceable=True)))

            traceable_events = [event for event in res if event["traceable"]]
            ok, res = self.client.list_trace(traceable_events[0])

            expect((ok, res)).to(be_successful_api_call)
            expect(res).to(contain(have_keys(type=ActivityAuditDataSource.CMD)))
            expect(res).to(have_len(be_above(0)))  # Not using be_empty, because we want to ensure this is a list
