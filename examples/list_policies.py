#!/usr/bin/env python
#
# List the current set of secure policies.
#

import os
import sys
import json
import getopt
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdSecureClient

def usage():
    print 'usage: %s [-o|--order-only] <sysdig-token>' % sys.argv[0]
    print '-o|--order-only: Only display the list of policy ids in evaluation order. Suitable for use by set_policy_order.py'
    print 'You can find your token at https://secure.sysdig.com/#/settings/user'
    sys.exit(1)

try:
    opts, args = getopt.getopt(sys.argv[1:],"o",["order-only"])
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
sdclient = SdSecureClient(sdc_token, 'https://secure.sysdig.com')

res = sdclient.get_policy_priorities()

if not res[0]:
    print res[1]
    sys.exit(1)

# Strip the surrounding json to only keep the list of policy ids
res[1] = res[1]['priorities']['policyIds']

if not order_only:
    priorities = res[1]
    res = sdclient.list_policies()
    if res[0]:
        res[1]['policies'].sort(key=lambda p: priorities.index(p['id']))

#
# Return the result
#
if res[0]:
    print json.dumps(res[1], indent=2)
else:
    print res[1]
    sys.exit(1)


