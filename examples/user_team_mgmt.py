#!/usr/bin/env python
#
# This example shows the different aspects of user/team management
#

import os
import sys
import logging
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient
#
# Parse arguments
#
if len(sys.argv) != 4:
    print 'usage: %s <sysdig-token> team-name user-name' % sys.argv[0]
    print 'You can find your token at https://app.sysdigcloud.com/#/settings/user'
    sys.exit(1)

sdc_token = sys.argv[1]

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)

team_name = sys.argv[2]
user_name = sys.argv[3]

print 'Trying to invite a user ', user_name
res = sdclient.create_user_invite(user_name)
if res[0] == False:
    print 'User creation failed: ', res[1]
else:
    print 'User creation succeeded'

print 'Now trying to create a team with name ', team_name
res = sdclient.create_team(team_name)
if res[0] == False:
    print 'Team creation failed: ', res[1]
else:
    print 'Team creation succeeded.', res[1]

print 'Now trying to find team with name ', team_name
res = sdclient.get_team(team_name)
if res[0] == False:
    print 'Could not get team info'
else:
    print 'Team fetch succeeded'

print 'Now trying to edit team ', team_name
res = sdclient.edit_team(team_name, description='Nextgen2', users=['admin@draios.com', 'john-doe@sysdig.com'])
if res[0] == False:
    print 'Could not edit team ', res[1]
else:
    print 'Edited team to change description and add users'

print 'Now trying to edit user ', user_name
res = sdclient.edit_user(user_name, firstName='Just', lastName='Edited3', teams=[team_name], roles=['ROLE_CUSTOMER', 'ROLE_USER'])
if res[0] == False:
    print 'Could not edit user: ', res[1]
else:
    print 'Edit user succeeded'

print 'Now trying to delete the team ', team_name
res = sdclient.delete_team(team_name)
if res[0] == False:
    print 'Could not delete team: ', res[1]
else:
    print 'Delete team succeeded'

sys.exit(0)
