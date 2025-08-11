#!/usr/bin/env python
#
# Add a new policy
#

import json
import sys

from sdcclient import SdSecureClient


def usage():
    print(("usage: %s <sysdig-token>" % sys.argv[0]))
    print("Reads policy json from standard input")
    print("You can find your token at https://secure.sysdig.com/#/settings/user")
    sys.exit(1)


#
# Parse arguments
#
if len(sys.argv) != 2:
    usage()

sdc_token = sys.argv[1]

policy_json = sys.stdin.read()

#
# Instantiate the SDC client
#
sdclient = SdSecureClient(sdc_token, "https://secure.sysdig.com")

ok, res = sdclient.add_policy_json(policy_json)

#
# Return the result
#
if ok:
    print((json.dumps(res, indent=2)))
else:
    print(res)
    sys.exit(1)
