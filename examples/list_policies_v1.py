#!/usr/bin/env python
#
# List the current set of secure policies.
#

import os
import sys
import json
import getopt
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdSecureClientV1


def usage():
    print(('usage: %s [-o|--order-only] <sysdig-token>' % sys.argv[0]))
    print('-o|--order-only: Only display the list of policy ids in evaluation order. Suitable for use by set_policy_order.py')
    print('You can find your token at https://secure.sysdig.com/#/settings/user')
    sys.exit(1)


try:
    opts, args = getopt.getopt(sys.argv[1:], "o", ["order-only"])
except getopt.GetoptError:
    usage()

order_only = False
for opt, arg in opts:
    if opt in ("-o", "--order-only"):
        order_only = True

#
# Parse arguments
#
if len(args) < 1:
    usage()

sdc_token = args[0]

#
# Instantiate the SDC client
#
sdclient = SdSecureClientV1(sdc_token, 'https://secure.sysdig.com')

ok, res = sdclient.get_policy_priorities()

if not ok:
    print(res)
    sys.exit(1)

# Strip the surrounding json to only keep the list of policy ids
res = res['priorities']['policyIds']

if not order_only:
    priorities = res
    ok, res = sdclient.list_policies()
    if ok:
        res['policies'].sort(key=lambda p: priorities.index(p['id']))

#
# Return the result
#
if ok:
    print((json.dumps(res, indent=2)))
else:
    print(res)
    sys.exit(1)
