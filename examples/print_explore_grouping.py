#!/usr/bin/env python
#
# Print the user's Explore grouping hierarchy.
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
# Fire the request
#
_, res = sdclient.get_explore_grouping_hierarchy()

#
# Show the result
#
print(res)
