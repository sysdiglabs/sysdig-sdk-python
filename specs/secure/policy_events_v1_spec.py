import datetime
import os

from expects import be_within, have_len, expect, contain, have_key, be_empty, have_keys
from mamba import before, context, description, it, _context

from sdcclient.secure import PolicyEventsClientV1
from specs import be_successful_api_call

with description("Policy Events v1", "integration") as self:
    with before.each:
        self.client = PolicyEventsClientV1(sdc_url=os.getenv("SDC_SECURE_URL", "https://secure.sysdig.com"),
                                           token=os.getenv("SDC_SECURE_TOKEN"))
    with context("when we try to retrieve policy events from the last 7 days"):
        with it("returns the list of all events happened"):
            day_in_seconds = 7 * 24 * 60 * 60

            ok, res = self.client.get_policy_events_duration(day_in_seconds)

            expect((ok, res)).to(be_successful_api_call)
            expect(res).to(have_keys("ctx", "data"))
            expect(res["data"]).to(
                contain(have_keys("id", "timestamp", "customerId", "source", "name", "description", "cursor")))

        with it("returns the list of all events from a range"):
            to_sec = int((datetime.datetime.utcnow() - datetime.datetime.utcfromtimestamp(0)).total_seconds())
            from_sec = to_sec - (7 * 24 * 60 * 60)

            ok, res = self.client.get_policy_events_range(from_sec, to_sec)

            expect((ok, res)).to(be_successful_api_call)
            expect(res).to(have_keys("ctx", "data"))
            expect(res["data"]).to(
                contain(have_keys("id", "timestamp", "customerId", "source", "name", "description", "cursor")))

        with it("returns the list of all events from the last 7 days that match a filter"):
            day_in_seconds = 7 * 24 * 60 * 60

            ok, res = self.client.get_policy_events_duration(day_in_seconds, filter='severity in ("4","5")')

            expect((ok, res)).to(be_successful_api_call)
            expect(res).to(have_keys("ctx", "data"))
            expect(res["data"]).to(contain(have_key("severity", be_within(3, 6))))

        with it("returns an empty list if the filter does not match"):
            day_in_seconds = 7 * 24 * 60 * 60

            ok, res = self.client.get_policy_events_duration(day_in_seconds, filter='severity in ("-1")')

            expect((ok, res)).to(be_successful_api_call)
            expect(res).to(have_keys("ctx", "data"))
            expect(res["data"]).to(be_empty)

    with _context("and from the first event we retrieve the rest of events"):
        # Deactivated tests. There seems to be a bug in the API -- need confirmation
        with it("returns the list of all events except the first"):
            day_in_seconds = 7 * 24 * 60 * 60
            _, res = self.client.get_policy_events_duration(day_in_seconds)
            ctx = {"cursor": res["data"][0]["cursor"]}
            qty_before = len(res["data"])

            ok, res = self.client.get_more_policy_events(ctx)

            expect((ok, res)).to(be_successful_api_call)
            expect(res["data"]).to(have_len(qty_before - 1))

    with context("when the parameters are wrong"):
        with it("returns an error retrieving events"):
            wrong_duration = -1
            ok, res = self.client.get_policy_events_duration(wrong_duration)
            expect((ok, res)).to_not(be_successful_api_call)

        with it("returns an error with an incorrect context"):
            wrong_context = {
                "limit": -1,
            }
            call = self.client.get_more_policy_events(wrong_context)
            expect(call).to_not(be_successful_api_call)
