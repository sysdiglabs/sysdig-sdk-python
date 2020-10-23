import os
import time

from expects import expect, have_key, contain, have_keys, be_empty, equal, be_false
from expects.matchers.built_in import have_len
from mamba import it, before, description

from sdcclient.monitor import EventsClientV2
from specs import be_successful_api_call

with description("Events v2", "integration") as self:
    with before.all:
        self.client = EventsClientV2(sdc_url=os.getenv("SDC_MONITOR_URL", "https://app.sysdigcloud.com"),
                                     token=os.getenv("SDC_MONITOR_TOKEN"))
        self.event_name = "event_v2_test_ci"

    with it("is able to create a custom event"):
        call = self.client.post_event(name=self.event_name,
                                      description="This event was created in a CI pipeline for the Python SDK library")
        expect(call).to(be_successful_api_call)

    with it("is able to list the events happened without any filter"):
        time.sleep(3)  # Wait for the event to appear in the feed
        ok, res = self.client.get_events()
        expect((ok, res)).to(be_successful_api_call)
        expect(res).to(have_key("events"))

    with it("is able to list the events created by the tests"):
        time.sleep(3)  # Wait for the event to appear in the feed
        ok, res = self.client.get_events(category=["custom"])
        expect((ok, res)).to(be_successful_api_call)
        expect(res).to(have_key("events", contain(have_keys(name=self.event_name))))

    with it("fails to retrieve the events with an incorrect category"):
        ok, res = self.client.get_events(category=['incorrect_category'])

        expect(ok).to(be_false)
        expect(res).to(equal("Invalid category 'incorrect_category'"))

    with it("is able to retrieve events that match a status"):
        ok, res = self.client.get_events(status=['triggered'])
        expect((ok, res)).to(be_successful_api_call)
        expect(res).to(have_key("events", contain(have_keys(name=self.event_name))))

    with it("fails to retrieve the events with an incorrect status"):
        ok, res = self.client.get_events(status=['incorrect_status'])

        expect(ok).to(be_false)
        expect(res).to(equal("Invalid status 'incorrect_status'"))

    with it("retrieves the events correctly specifying direction 'before'"):
        ok, res = self.client.get_events(direction="before")

        expect((ok, res)).to(be_successful_api_call)
        expect(res).to(have_keys('events', 'total', 'matched'))

    with it("retrieves the events correctly specifying direction 'after'"):
        ok, res = self.client.get_events(direction="after")

        expect((ok, res)).to(be_successful_api_call)
        expect(res).to(have_keys('events', 'total', 'matched'))

    with it("fails to retrieve the events with an incorrect direction"):
        ok, res = self.client.get_events(direction="incorrect_direction")

        expect(ok).to(be_false)
        expect(res).to(equal("Invalid direction 'incorrect_direction', must be either 'before' or 'after'"))

    with it("is able to retrieve events by name"):
        ok, res = self.client.get_events(name=self.event_name)

        expect((ok, res)).to(be_successful_api_call)
        expect(res).to(have_key("events", contain(have_key("name", equal(self.event_name)))))

    with it("retrieves an empty list when the name provided is not found"):
        ok, res = self.client.get_events(name="RandomUnexistingEvent")

        expect((ok, res)).to(be_successful_api_call)
        expect(res).to(have_key("events", be_empty))

    with it("is able to retrieve the last event only"):
        ok, res = self.client.get_events(limit=1)
        expect((ok, res)).to(be_successful_api_call)
        expect(res).to(have_key("events", have_len(1)))

    with it("is able to remove the event from the feed"):
        time.sleep(3)  # Wait for the event to appear in the feed
        _, res = self.client.get_events(category=["custom"])

        events = [event for event in res["events"] if event["name"] == self.event_name]
        expect(events).to_not(be_empty)

        call = self.client.delete_event(events[0])
        expect(call).to(be_successful_api_call)
