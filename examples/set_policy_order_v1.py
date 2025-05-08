#!/usr/bin/env python
#
# Change the evaluation order of policies to match the provided json.
#

import json
import sys

from sdcclient import SdSecureClientV1


def usage():
    print(("usage: %s <sysdig-token>" % sys.argv[0]))
    print("Reads json representing new policy evaluation order from standard input")
    print("You can find your token at https://secure.sysdig.com/#/settings/user")
    sys.exit(1)


#
# Parse arguments
#
if len(sys.argv) != 2:
    usage()

sdc_token = sys.argv[1]
priorities_json = sys.stdin.read()

try:
    priorities_obj = json.loads(priorities_json)
except Exception as e:
    print(("priorities json is not valid json: {}".format(str(e))))
    sys.exit(1)

#
# Instantiate the SDC client
#
sdclient = SdSecureClientV1(sdc_token, "https://secure.sysdig.com")

#
# The argument to /api/policies/priorities is the list of ids wrapped
# in an object containing a version and dates. So fetch the list of
# priorities, update the list in-place and set it.
#

ok, res = sdclient.get_policy_priorities()

if not ok:
    print(res)
    sys.exit(1)

obj = res
obj["priorities"]["policyIds"] = priorities_obj

ok, res = sdclient.set_policy_priorities(json.dumps(obj))

#
# Return the result
#
if ok:
    print((json.dumps(res, indent=2)))
else:
    print(res)
    sys.exit(1)
