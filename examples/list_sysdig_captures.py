#!/usr/bin/env python
#
# Print the list of sysdig captures.
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
# Fire the request.
#
ok, res = sdclient.get_sysdig_captures()

#
# Show the list of metrics
#
if ok:
    captures = res["dumps"]
else:
    print(res)
    sys.exit(1)

for capture in captures:
    print(
        (
            "Folder %s, Name %s, Host: %s, Size: %d, Status: %s"
            % (
                capture["folder"],
                capture["name"],
                capture["agent"]["hostName"],
                capture["size"],
                capture["status"],
            )
        )
    )
