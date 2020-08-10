import os

from expects import equal, expect, contain, have_key, be_empty, be_true, be_false, be_above_or_equal, \
    have_keys
from expects.matchers import _Or
from mamba import before, context, description, it

from sdcclient import SdcClient

with description("Events") as self:
    with before.each:
        self.client = SdcClient(
            sdc_url=os.getenv("SDC_MONITOR_URL", "https://app.sysdigcloud.com"),
            token=os.getenv("SDC_MONITOR_TOKEN"),
        )

    with context("when retrieving the events"):
        with it("retrieves the events correctly with the default parameters"):
            ok, res = self.client.get_events()

            expect(ok).to(be_true)
            expect(res).to(have_keys('events', 'total', 'matched'))
            expect(len(res['events'])).to_not(equal(0))

        with it("retrieves the events correctly specifying other limit"):
            ok, res = self.client.get_events(limit=1)

            expect(ok).to(be_true)
            expect(res).to(have_keys('events', 'total', 'matched'))
            expect(res['total']).to(be_above_or_equal(2))
            expect(res['matched']).to(be_above_or_equal(2))
            expect(len(res['events'])).to(equal(1))

        with it("retrieves the events correctly specifying a correct category"):
            for category in ['alert', 'custom', 'docker', 'containerd', 'kubernetes']:
                ok, res = self.client.get_events(category=[category])

                expect(ok).to(be_true)
                expect(res).to(have_keys('events', 'total', 'matched'))
                expect(res["total"]).to(be_above_or_equal(0))

        with it("fails to retrieve the events with an incorrect category"):
            ok, res = self.client.get_events(category=['incorrect_category'])

            expect(ok).to(be_false)
            expect(res).to(equal("Invalid category 'incorrect_category'"))

        with it("retrieves the events correctly specifying a valid status"):
            for status in ["triggered", "resolved", "acknowledged", "unacknowledged"]:
                ok, res = self.client.get_events(status=[status])

                expect(ok).to(be_true)
                expect(res).to(have_keys('events', 'total', 'matched'))
                expect(len(res['events'])).to_not(equal(0))

        with it("fails to retrieve the events with an incorrect status"):
            ok, res = self.client.get_events(status=['incorrect_status'])

            expect(ok).to(be_false)
            expect(res).to(equal("Invalid status 'incorrect_status'"))


        with it("retrieves the events correctly specifying a valid direction"):
            for direction in ["before", "after"]:
                ok, res = self.client.get_events(direction=direction)

                expect(ok).to(be_true)
                expect(res).to(have_keys('events', 'total', 'matched'))
                expect(len(res['events'])).to_not(equal(0))

        with it("fails to retrieve the events with an incorrect direction"):
            ok, res = self.client.get_events(direction="incorrect_direction")

            expect(ok).to(be_false)
            expect(res).to(equal("Invalid direction 'incorrect_direction', must be either 'before' or 'after'"))

        with it("is able to retrieve events by name"):
            ok, res = self.client.get_events(name="Container")

            expect(ok).to(be_true)
            expect(res).to(have_key("events"))
            expect(res["events"]).to(_Or(contain(have_key("name", contain("Container"))), be_empty))

        with it("retrieves an empty list when the name provided is not found"):
            ok, res = self.client.get_events(name="RandomUnexistingEvent")

            expect(ok).to(be_true)
            expect(res).to(have_key("events"))
            expect(res["events"]).to(be_empty)