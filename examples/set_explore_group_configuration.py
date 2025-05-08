#!/usr/bin/env python
#
# Set the group configuration in explore.
#

import sys

from sdcclient import SdcClient

#
# Parse arguments
#
if len(sys.argv) != 2:
    print(("usage: %s <sysdig-token>" % sys.argv[0]))
    print("You can find your token at https://app.sysdigcloud.com/#/settings/user")
    sys.exit(1)

sdc_token = sys.argv[1]

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)

#
# Fire the request, set the group configuration you need in the example below
#
groupConfig = ["agent.tag.role", "host.mac"]
ok, res = sdclient.set_explore_grouping_hierarchy(groupConfig)

#
# Show the error if there was one
#
if not ok:
    print(res)
