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
sdclient = SdcClient(sdc_token, sdc_url='https://app.sysdigcloud.com')

team_name = sys.argv[2]
user_name = sys.argv[3]

print 'Trying to invite a user:', user_name
res = sdclient.create_user_invite(user_name)
if res[0] == False:
    if res[1] == 'user ' + user_name + ' already exists':
        print 'User creation failed because', user_name ,'already exists. Continuing.'
    else:
        print 'User creation failed:', res[1], '. Exiting.'
        sys.exit(1)
else:
    print 'User creation succeeded'

# Possible failures on Team creation might include having reached the
# max limit on Teams for this customer account or if the Team by that
# name already exists. Since a previous successful run of this test
# would have deleted the Team by the same name, and we need to be able
# to configure Teams for this test to pass, we'll treat both types of
# error as a genuine fail of the test.
print 'Now trying to create a team with name:', team_name
res = sdclient.create_team(team_name)
if res[0] == False:
    print 'Team creation failed:', res[1], '. Exiting.'
    sys.exit(1)
else:
    print 'Team creation succeeded.', res[1]

print 'Now trying to find team with name:', team_name
res = sdclient.get_team(team_name)
if res[0] == False:
    print 'Could not get team info:', res[1], '. Exiting.'
    sys.exit(1)
else:
    print 'Team fetch succeeded'

print 'Now trying to edit team:', team_name
memberships = {
    'admin@draios.com': 'ROLE_TEAM_MANAGER',
    'john-doe@sysdig.com': 'ROLE_TEAM_READ'
}
res = sdclient.edit_team(team_name, description='Nextgen2', memberships=memberships)
if res[0] == False:
    print 'Could not edit team:', res[1], '. Exiting.'
    sys.exit(1)
else:
    print 'Edited team to change description and add users'

print 'Now trying to edit user:', user_name
res = sdclient.edit_user(user_name, firstName='Just', lastName='Edited3', systemRole='ROLE_CUSTOMER')
if res[0] == False:
    print 'Could not edit user:', res[1], '. Exiting.'
    sys.exit(1)
else:
    print 'Edit user succeeded'

print 'Now trying to delete the team:', team_name
res = sdclient.delete_team(team_name)
if res[0] == False:
    print 'Could not delete team:', res[1], '. Exiting.'
    sys.exit(1)
else:
    print 'Delete team succeeded'

sys.exit(0)
