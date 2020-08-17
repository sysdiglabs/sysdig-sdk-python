import os
import time

from expects import expect, have_key, have_keys
from expects.matchers import _Or
from expects.matchers.built_in import be_empty, contain, be_above_or_equal
from mamba import before, it, description, after

from sdcclient import SdcClient
from specs import be_successful_api_call


def _mysql_app_check():
    return """\
app_checks:
  - name: mysql
    pattern:
      comm: mysqld
    conf:
      server: 127.0.0.1
      user: sysdig-cloud
      pass: sysdig-cloud-password
"""


def _debug_enabled():
    return """\
log:
  console_priority: debug
"""


# See https://docs.sysdig.com/en/agent-auto-config.html for more information
def _agent_configuration():
    return {
        "files": [
            {
                "filter": "host.mac = \"08:00:27:de:5b:b9\"",
                "content": _mysql_app_check()
            },
            {
                "filter": "*",
                "content": _debug_enabled()
            }
        ]
    }


with description("Agent") as self:
    with before.all:
        self.client = SdcClient(sdc_url=os.getenv("SDC_MONITOR_URL", "https://app.sysdigcloud.com"),
                                token=os.getenv("SDC_MONITOR_TOKEN"))

    with it("is able to retrieve the agent configuration"):
        ok, res = self.client.get_agents_config()

        expect((ok, res)).to(be_successful_api_call)
        expect(res).to(have_key("files", _Or(be_empty, contain(have_key("content")))))

    with it("is able to set up the agent configuration"):
        ok, res = self.client.set_agents_config(_agent_configuration())

        expect((ok, res)).to(be_successful_api_call)
        expect(res).to(have_key("files", contain(have_key("content", contain(_mysql_app_check())))))
        expect(res).to(have_key("files", contain(have_key("content", contain(_debug_enabled())))))

    with it("is able to clean up the agent configuration"):
        ok, res = self.client.clear_agents_config()

        expect((ok, res)).to(be_successful_api_call)
        expect(res).to(have_key("files", be_empty))

    with it("is able to retrieve the number of connected agents"):
        ok, res = self.client.get_n_connected_agents()

        expect((ok, res)).to(be_successful_api_call)
        expect(res).to(be_above_or_equal(1))

    with it("is able to retrieve the info from the connected agents"):
        ok, res = self.client.get_connected_agents()

        expect((ok, res)).to(be_successful_api_call)
        expect(res).to(contain(have_keys(
            "customer",
            "machineId",
            "hostName",
            connected=True,
            attributes=have_keys(
                "hidden",
                "version",
            )
        )))
