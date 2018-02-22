#!/usr/bin/env python
#
# This example shows the different aspects of user/team management.
#

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient
#
# Parse arguments
#
if len(sys.argv) != 4:
    print 'usage: %s <sysdig-token> team-prefix user-name' % sys.argv[0]
    print 'You can find your token at https://app.sysdigcloud.com/#/settings/user'
    sys.exit(1)

sdc_token = sys.argv[1]

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token, sdc_url='https://app.sysdigcloud.com')

team_prefix = sys.argv[2]

user_email_parts = sys.argv[3].split('@')
user_email_prefix = user_email_parts[0]
user_email_domain = user_email_parts[1]

#
# Create test users
#
# All users initially are part of default team.
#

admin = user_email_prefix + '+team_mgmt-admin' + '@' + user_email_domain
userA = user_email_prefix + '+team_mgmt-a'     + '@' + user_email_domain
userB = user_email_prefix + '+team_mgmt-b'     + '@' + user_email_domain

print 'Creating test users...'

res = sdclient.create_user_invite(admin, system_role='ROLE_CUSTOMER')
if res[0] is False:
    print '-- User creation failed:', res[1], '. Exiting.'
    sys.exit(1)
else:
    print '-- User \'', admin, '\' created successfully.'

res = sdclient.create_user_invite(userA)
if res[0] is False:
    print '-- User creation failed:', res[1], '. Exiting.'
    sys.exit(1)
else:
    print '-- User \'', userA, '\' created successfully.'

res = sdclient.create_user_invite(userB)
if res[0] is False:
    print '-- User creation failed:', res[1], '. Exiting.'
    sys.exit(1)
else:
    print '-- User \'', userB, '\' created successfully.'

#
# Create test teams
#
# Possible failures on Team creation might include having reached the
# max limit on Teams for this customer account or if the Team by that
# name already exists. Since a previous successful run of this test
# would have deleted the Team by the same name, and we need to be able
# to configure Teams for this test to pass, we'll treat both types of
# error as a genuine fail of the test.
#

teamA = team_prefix + 'A'
teamB = team_prefix + 'B'

print 'Creating test teams...'

res = sdclient.create_team(teamA)
if res[0] is False:
    print '-- Team creation failed:', res[1], '. Exiting.'
    sys.exit(1)
else:
    print '-- Team \'', teamA, '\' created successfully.'

res = sdclient.create_team(teamB)
if res[0] is False:
    print '-- Team creation failed:', res[1], '. Exiting.'
    sys.exit(1)
else:
    print '-- Team \'', teamB, '\' created successfully.'

#
# Membership manipulation
#
# Admins are part of all teams and their membership cannot be edited.
#

print 'Membership manipulation...'

res = sdclient.list_memberships(teamA)
if res[0] is False:
    print '-- Unable to fetch team memberships:', res[1], '. Exiting.'
    sys.exit(1)
elif admin not in res[1].keys():
    print '-- Admin should  be part of all teams!', 'Exiting.'
    sys.exit(1)
elif userA in res[1].keys() or userB in res[1].keys():
    print '-- Users ', userA, ' and ', userB, ' should not be part of team ', teamA, '!', 'Exiting.'
    sys.exit(1)

res = sdclient.list_memberships(teamB)
if res[0] is False:
    print '-- Unable to fetch team memberships:', res[1], '. Exiting.'
    sys.exit(1)
elif admin not in res[1].keys():
    print '-- Admin should  be part of all teams!', 'Exiting.'
    sys.exit(1)
elif userA in res[1].keys() or userB in res[1].keys():
    print '-- Users ', userA, ' and ', userB, ' should not be part of team ', teamB, '!', 'Exiting.'
    sys.exit(1)

#
# Create team memberships
#

print '-- Create team memberships'

# Manipulate with teamA

res = sdclient.save_memberships(teamA, {userA: 'ROLE_TEAM_EDIT'})
if res[0] is False:
    print '-- Unable to add ', userA, ' to ', teamA, ' due to: ', res[1], '. Exiting.'
    sys.exit(1)

res = sdclient.list_memberships(teamA)
if res[0] is False:
    print '-- Unable to fetch team memberships:', res[1], '. Exiting.'
    sys.exit(1)
elif userA not in res[1].keys() or admin not in res[1].keys():
    print '-- Users ', userA, ' and ', admin, ' should be part of team ', teamA, '!', 'Exiting.'
    sys.exit(1)

# Manipulate with teamB

res = sdclient.save_memberships(teamB, {userA: 'ROLE_TEAM_MANAGER', userB: 'ROLE_TEAM_READ'})
if res[0] is False:
    print '-- Unable to add ', userA, ' and ', userB, ' to ', teamB, ' due to: ', res[1], '. Exiting.'
    sys.exit(1)

res = sdclient.list_memberships(teamB)
if res[0] is False:
    print '-- Unable to fetch team memberships:', res[1], '. Exiting.'
    sys.exit(1)
elif userA not in res[1].keys() or userB not in res[1].keys() or admin not in res[1].keys():
    print '-- Users ', userA, ', ', userB, ' and ', admin, ' should be part of team ', teamB, '!', 'Exiting.'
    sys.exit(1)

# Update team memberships

print '-- Update team memberships'

# Add new or update existing memberships
res = sdclient.save_memberships(teamA, {userA: 'ROLE_TEAM_READ', userB: 'ROLE_TEAM_EDIT'})
if res[0] is False:
    print '-- Unable to modify membership for ', userA, ' and to add ', userB, ' to ', teamA, ' due to: ', res[1], '. Exiting.'
    sys.exit(1)

res = sdclient.list_memberships(teamA)
if res[0] is False:
    print '-- Unable to fetch team memberships:', res[1], '. Exiting.'
    sys.exit(1)
elif userA not in res[1].keys() or userB not in res[1].keys() or admin not in res[1].keys():
    print '-- Users ', userA, ', ', userB, ' and ', admin, ' should be part of team ', teamA, '!', 'Exiting.'
    sys.exit(1)
elif res[1][userA] != 'ROLE_TEAM_READ' or res[1][userB] != 'ROLE_TEAM_EDIT':
    print '-- Users ', userA, ' and ', userB, ' should have appropriate roles assigned for team ', teamA, '!', 'Exiting.'
    sys.exit(1)

# Remove team memberships

print '-- Remove team memberships'

res = sdclient.remove_memberships(teamA, [userB])
if res[0] is False:
    print '-- Unable to remove membership for ', userB, ' from team', teamA, ' due to: ', res[1], '. Exiting.'
    sys.exit(1)

res = sdclient.list_memberships(teamA)
if res[0] is False:
    print '-- Unable to fetch team memberships:', res[1], '. Exiting.'
    sys.exit(1)
elif userB in res[1].keys():
    print '-- User ', userB, ' should not be part of team ', teamA, '!', 'Exiting.'
    sys.exit(1)

# Admin user cannot be removed from any team
res = sdclient.remove_memberships(teamB, [admin, userA])
if res[0] is False:
    print '-- Unable to remove membership for ', userB, ' from team', teamA, ' due to: ', res[1], '. Exiting.'
    sys.exit(1)

res = sdclient.list_memberships(teamB)
if res[0] is False:
    print '-- Unable to fetch team memberships:', res[1], '. Exiting.'
    sys.exit(1)
elif userA in res[1].keys():
    print '-- User ', userA, ' should not be part of team ', teamB, '!', 'Exiting.'
    sys.exit(1)
elif admin not in res[1].keys():
    print '-- User ', admin, ' should be always part of all teams!', 'Exiting.'
    sys.exit(1)

#
# Clean-up
#

print 'Cleaning up...'

print '-- Deleting test teams.'

res = sdclient.delete_team(teamA)
if res[0] is False:
    print '-- Team \'', teamA, '\' deletion failed: ', res[1]

res = sdclient.delete_team(teamB)
if res[0] is False:
    print '-- Team \'', teamB, '\' deletion failed: ', res[1]


print '-- Deleting test users.'

res = sdclient.delete_user(admin)
if res[0] is False:
    print '-- User \'', admin, '\' deletion failed: ', res[1]

res = sdclient.delete_user(userA)
if res[0] is False:
    print '-- User \'', userA, '\' deletion failed: ', res[1]

res = sdclient.delete_user(userB)
if res[0] is False:
    print '-- User \'', userB, '\' deletion failed: ', res[1]


print 'All done successfully!!!'

sys.exit(0)
