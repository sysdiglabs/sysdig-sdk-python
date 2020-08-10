#!/usr/bin/env python
#
# Delete a policy, by either id or name.
#

import getopt
import json
import sys

from sdcclient import SdSecureClientV1


def usage():
    print(('usage: %s [-i|--id <id>] [-n|--name <name>] <sysdig-token>' % sys.argv[0]))
    print('-i|--id: the id of the policy to delete')
    print('-n|--name: the name of the policy to delete')
    print('You can find your token at https://secure.sysdig.com/#/settings/user')
    sys.exit(1)


#
# Parse arguments
#
try:
    opts, args = getopt.getopt(sys.argv[1:], "i:n:", ["id=", "name="])
except getopt.GetoptError:
    usage()

id = ""
name = ""
for opt, arg in opts:
    if opt in ("-i", "--id"):
        id = arg
    elif opt in ("-n", "--name"):
        name = arg

if len(id) + len(name) == 0:
    usage()

if len(args) < 1:
    usage()

sdc_token = args[0]

#
# Instantiate the SDC client
#
sdclient = SdSecureClientV1(sdc_token, 'https://secure.sysdig.com')

if len(id) > 0:
    ok, res = sdclient.delete_policy_id(id)
else:
    ok, res = sdclient.delete_policy_name(name)

#
# Return the result
#
if ok:
    print((json.dumps(res, indent=2)))
else:
    print(res)
    sys.exit(1)
