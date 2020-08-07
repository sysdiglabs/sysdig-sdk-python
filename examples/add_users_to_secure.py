#!/usr/bin/env python
#
# Make sure all users are members of the Secure Operations team.
#
# As of when this script was written, there is only one team for
# all Secure users. Newly-created users that land in the default
# team for Monitor (such as those created via the API) will
# therefore not be in the Secure Operations team. If you have an
# environment where you want all users to have both Monitor and
# Secure access by default, you could run this script periodically
# (e.g. as a cron job) to make sure any such users are made part
# of the Secure Operations team as well.
#

import os
import sys
import json
import logging
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient

#
# Parse arguments
#
if len(sys.argv) != 2:
    print(('usage: %s <sysdig-token>' % sys.argv[0]))
    print('You can find your token at https://app.sysdigcloud.com/#/settings/user')
    sys.exit(1)

sdc_token = sys.argv[1]

SECURE_TEAM_NAME = 'Secure Operations'

#
# As of when this script was written, the Secure Operations team does
# not have the concepts of RBAC roles like "Read User" vs. "Edit User".
# Rather, all members of the Secure team have full visibility within
# Secure, which is associated with ROLE_TEAM_EDIT.
#
SECURE_TEAM_ROLE = 'ROLE_TEAM_EDIT'

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token, sdc_url='https://app.sysdigcloud.com')

ok, res = sdclient.list_memberships(SECURE_TEAM_NAME)

if not ok:
    print(('Unable to get memberships for ' + SECURE_TEAM_NAME + ' team: ', res))
    sys.exit(1)
memberships = res

ok, res = sdclient.get_users()

if not ok:
    print(('Unable to get users: ', res))
    sys.exit(1)
all_users = res

#
# The memberships passed into edit_team() are based on username
# rather than ID, so convert the IDs.
#
for user in all_users:
    if user['username'] in memberships:
        print(('Will preserve existing membership for: ' + user['username']))
    else:
        print(('Will add new member: ' + user['username']))
        memberships[user['username']] = SECURE_TEAM_ROLE

ok, res = sdclient.save_memberships(SECURE_TEAM_NAME, memberships=memberships)
if not ok:
    print(('Could not edit team:', res, '. Exiting.'))
    sys.exit(1)
else:
    print(('Finished syncing memberships of "' + SECURE_TEAM_NAME + '" team'))

sys.exit(0)
