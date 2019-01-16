#!/usr/bin/env python
#
# Delete all secure policies.
#

import os
import sys
import json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdSecureClient

def usage():
    print 'usage: %s <sysdig-token>' % sys.argv[0]
    print 'You can find your token at https://secure.sysdig.com/#/settings/user'
    sys.exit(1)

#
# Parse arguments
#
if len(sys.argv) != 2:
    usage()

sdc_token = sys.argv[1]

#
# Instantiate the SDC client
#
sdclient = SdSecureClient(sdc_token, 'https://secure.sysdig.com')

# Get a list of policyIds
res = sdclient.list_policies()
policies = []

if not res[0]:
    print res[1]
    sys.exit(1)
else:
    policies = res[1]['policies']

for policy in policies:
    print "deleting policy: " + str(policy['id'])
    res = sdclient.delete_policy_id(policy['id'])
    if not res[0]:
        print res[1]
        sys.exit(1)
