#!/usr/bin/env python
#
# Update a specific policy
#

import os
import sys
import json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdSecureClient


def usage():
    print('usage: %s <sysdig-token>' % sys.argv[0])
    print('Reads json representing updated policy from standard input')
    print('You can find your token at https://secure.sysdig.com/#/settings/user')
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
sdclient = SdSecureClient(sdc_token, 'https://secure.sysdig.com')

ok, res = sdclient.update_policy(policy_json)

#
# Return the result
#
if ok:
    print(json.dumps(res, indent=2))
else:
    print(res)
    sys.exit(1)


