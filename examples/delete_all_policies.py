#!/usr/bin/env python
#
# Delete all secure policies.
#

import sys

from sdcclient import SdSecureClient


def usage():
    print(('usage: %s <sysdig-token>' % sys.argv[0]))
    print('You can find your token at https://secure.sysdig.com/#/settings/user')
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
ok, res = sdclient.list_policies()
policies = []

if not ok:
    print(res)
    sys.exit(1)
else:
    policies = res

for policy in policies:
    print(("deleting policy: " + str(policy['id'])))
    ok, res = sdclient.delete_policy_id(policy['id'])
    if not ok:
        print(res)
        sys.exit(1)
