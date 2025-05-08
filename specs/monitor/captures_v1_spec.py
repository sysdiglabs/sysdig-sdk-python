import os
import random
import socket
import string
import time

from expects import expect, have_key, contain
from expects.matchers import _Or
from expects.matchers.built_in import have_keys, equal
from mamba import description, it, before, after, _it

from sdcclient import SdMonitorClient
from specs import be_successful_api_call


def randomword(length):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for _ in range(length))


with description("Captures v1", "integration-agent") as self:
    with before.all:
        self.client = SdMonitorClient(sdc_url=os.getenv("SDC_MONITOR_URL", "https://app.sysdigcloud.com"),
                                      token=os.getenv("SDC_MONITOR_TOKEN"))
        self.capture_name = f"apicapture-sdk-{randomword(10)}"
        self.hostname = socket.gethostname()

    with after.all:
        ok, res = self.client.get_sysdig_captures()
        expect((ok, res)).to(be_successful_api_call)

        for capture in res["dumps"]:
            ok, res = self.client.delete_sysdig_capture(capture["id"])
            expect((ok, res)).to(be_successful_api_call)

    with it("is able to create a capture"):
        ok, res = self.client.create_sysdig_capture(hostname=self.hostname,
                                                    capture_name=self.capture_name,
                                                    duration=10)
        expect((ok, res)).to(be_successful_api_call)

    with it("is able to retrieve the capture we have created"):
        ok, res = self.client.get_sysdig_captures()

        expect((ok, res)).to(be_successful_api_call)
        expect(res).to(have_key(
            "dumps", contain(
                have_keys(
                    "size",
                    "status",
                    "folder",
                    agent=have_key("hostName", equal(self.hostname)),
                    name=equal(f"{self.capture_name}.scap"),
                ))
        ))

    # DEACTIVATED: This test is not enabled because sometimes the agent does not trigger the capture
    # and therefore this test fails. As it is not our duty to verify that the agent is able to create the capture,
    # we assume this won't be covered by the library.
    with _it("polls the status of the capture until it's done"):
        _, res = self.client.get_sysdig_captures()
        capture = [capture for capture in res["dumps"] if capture["name"] == f"{self.capture_name}.scap"][0]

        status = "undefined"
        for _ in range(300):
            ok, res = self.client.poll_sysdig_capture(capture)
            expect((ok, res)).to(be_successful_api_call)
            expect(res).to(have_key("dump", have_key("status")))

            status = res["dump"]["status"]
            if status in ["done", "uploaded", "error", "uploadingError"]:
                break

            time.sleep(1)

        expect(status).to(_Or(equal("done"), equal("uploaded")))

    # DEACTIVATED: This test is not enabled because sometimes the agent does not trigger the capture
    # and therefore this test fails. As it is not our duty to verify that the agent is able to create the capture,
    # we assume this won't be covered by the library.
    with _it("is able to download the capture"):
        _, res = self.client.get_sysdig_captures()
        capture = [capture for capture in res["dumps"] if capture["name"] == f"{self.capture_name}.scap"][0]

        call = self.client.download_sysdig_capture(capture["id"])
        expect(call).to(be_successful_api_call)
