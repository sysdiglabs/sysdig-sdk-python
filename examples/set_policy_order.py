#!/usr/bin/env python
#
# Change the evaluation order of policies to match the provided json.
#

import os
import sys
import json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdSecureClient

def usage():
    print 'usage: %s <sysdig-token>' % sys.argv[0]
    print 'Reads json representing new policy evaluation order from standard input'
    print 'You can find your token at https://secure.sysdig.com/#/settings/user'
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
    print "priorities json is not valid json: {}".format(str(e))
    sys.exit(1)

#
# Instantiate the SDC client
#
sdclient = SdSecureClient(sdc_token, 'https://secure.sysdig.com')

#
# The argument to /api/policies/priorities is the list of ids wrapped
# in an object containing a version and dates. So fetch the list of
# priorities, update the list in-place and set it.
#

res = sdclient.get_policy_priorities()

if not res[0]:
    print res[1]
    sys.exit(1)

obj = res[1]
obj['priorities']['policyIds'] = priorities_obj

res = sdclient.set_policy_priorities(json.dumps(obj))

#
# Return the result
#
if res[0]:
    print json.dumps(res[1], indent=2)
else:
    print res[1]
    sys.exit(1)


