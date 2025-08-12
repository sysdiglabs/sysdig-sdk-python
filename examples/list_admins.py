#!/usr/bin/env python
#
# List all the Admin users in a Sysdig Monitor environment. The token you
# provide must have Admin rights.
# If you're running this script in an On-Premise install of Sysdig Montior,
# the "super" Admin (the first Admin user that was created at initial
# install) will be highlighted.
#

import sys

from sdcclient import SdcClient

#
# Parse arguments
#
if len(sys.argv) != 2:
    print(("usage: %s <sysdig-token>" % sys.argv[0]))
    print("You can find your token at https://app.sysdigcloud.com/#/settings/user")
    print("For this script to work, the user for the token must have Admin rights")
    sys.exit(1)

sdc_token = sys.argv[1]

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token, "https://app.sysdigcloud.com")

#
# Get the configuration
#
ok, res = sdclient.get_users()
if ok:
    admins = []
    superadmins = []
    for user in res:
        if "ROLE_CUSTOMER" in user["roles"]:
            admins.append(user["username"])
        if "ROLE_ADMIN" in user["roles"]:
            superadmins.append(user["username"])
    print("Admin users")
    print("-----------")
    for username in admins:
        print(username)
    print("\nSuper Admins")
    print("------------")
    for username in superadmins:
        print(username)
else:
    print(res)
    sys.exit(1)
