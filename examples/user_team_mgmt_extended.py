#!/usr/bin/env python
#
# This example shows the different aspects of user/team management.
#

import sys

from sdcclient import SdcClient

#
# Parse arguments
#
if len(sys.argv) != 4:
    print(('usage: %s <sysdig-token> team-prefix user-name' % sys.argv[0]))
    print('You can find your token at https://app.sysdigcloud.com/#/settings/user')
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
userA = user_email_prefix + '+team_mgmt-a' + '@' + user_email_domain
userB = user_email_prefix + '+team_mgmt-b' + '@' + user_email_domain

teamA = team_prefix + 'A'
teamB = team_prefix + 'B'

print('Creating test users...')

try:
    ok, res = sdclient.create_user_invite(admin, first_name='TestUser', last_name='Admin', system_role='ROLE_CUSTOMER')
    if not ok:
        print(('-- User creation failed:', res, '. Exiting.'))
        sys.exit(1)
    else:
        print(('-- User \'', admin, '\' created successfully.'))

    ok, res = sdclient.create_user_invite(userA, first_name='TestUser', last_name='Alpha')
    if not ok:
        print(('-- User creation failed:', res, '. Exiting.'))
        sys.exit(1)
    else:
        print(('-- User \'', userA, '\' created successfully.'))

    ok, res = sdclient.create_user_invite(userB, first_name='TestUser', last_name='Beta')
    if not ok:
        print(('-- User creation failed:', res, '. Exiting.'))
        sys.exit(1)
    else:
        print(('-- User \'', userB, '\' created successfully.'))

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

    print('Creating test teams...')

    ok, res = sdclient.create_team(teamA)
    if not ok:
        print(('-- Team creation failed:', res, '. Exiting.'))
        sys.exit(1)
    else:
        print(('-- Team \'', teamA, '\' created successfully.'))

    ok, res = sdclient.create_team(teamB)
    if not ok:
        print(('-- Team creation failed:', res, '. Exiting.'))
        sys.exit(1)
    else:
        print(('-- Team \'', teamB, '\' created successfully.'))

    #
    # Membership manipulation
    #
    # Admins are part of all teams and their membership cannot be edited.
    #

    print('Membership manipulation...')

    ok, res = sdclient.list_memberships(teamA)
    if not ok:
        print(('-- Unable to fetch team memberships:', res, '. Exiting.'))
        sys.exit(1)
    elif admin not in list(res.keys()):
        print(('-- Admin should  be part of all teams!', 'Exiting.'))
        sys.exit(1)
    elif userA in list(res.keys()) or userB in list(res.keys()):
        print(('-- Users ', userA, ' and ', userB, ' should not be part of team ', teamA, '!', 'Exiting.'))
        sys.exit(1)

    ok, res = sdclient.list_memberships(teamB)
    if not ok:
        print(('-- Unable to fetch team memberships:', res, '. Exiting.'))
        sys.exit(1)
    elif admin not in list(res.keys()):
        print(('-- Admin should  be part of all teams!', 'Exiting.'))
        sys.exit(1)
    elif userA in list(res.keys()) or userB in list(res.keys()):
        print(('-- Users ', userA, ' and ', userB, ' should not be part of team ', teamB, '!', 'Exiting.'))
        sys.exit(1)

    #
    # Create team memberships
    #

    print('-- Create team memberships')

    # Manipulate with teamA

    ok, res = sdclient.save_memberships(teamA, {userA: 'ROLE_TEAM_EDIT'})
    if not ok:
        print(('-- Unable to add ', userA, ' to ', teamA, ' due to: ', res, '. Exiting.'))
        sys.exit(1)

    ok, res = sdclient.list_memberships(teamA)
    if not ok:
        print(('-- Unable to fetch team memberships:', res, '. Exiting.'))
        sys.exit(1)
    elif userA not in list(res.keys()) or admin not in list(res.keys()):
        print(('-- Users ', userA, ' and ', admin, ' should be part of team ', teamA, '!', 'Exiting.'))
        sys.exit(1)

    # Manipulate with teamB

    ok, res = sdclient.save_memberships(teamB, {userA: 'ROLE_TEAM_MANAGER', userB: 'ROLE_TEAM_READ'})
    if not ok:
        print(('-- Unable to add ', userA, ' and ', userB, ' to ', teamB, ' due to: ', res, '. Exiting.'))
        sys.exit(1)

    ok, res = sdclient.list_memberships(teamB)
    if not ok:
        print(('-- Unable to fetch team memberships:', res, '. Exiting.'))
        sys.exit(1)
    elif userA not in list(res.keys()) or userB not in list(res.keys()) or admin not in list(res.keys()):
        print(('-- Users ', userA, ', ', userB, ' and ', admin, ' should be part of team ', teamB, '!', 'Exiting.'))
        sys.exit(1)

    # Update team memberships

    print('-- Update team memberships')

    # Add new or update existing memberships
    ok, res = sdclient.save_memberships(teamA, {userA: 'ROLE_TEAM_READ', userB: 'ROLE_TEAM_EDIT'})
    if not ok:
        print(('-- Unable to modify membership for ', userA, ' and to add ', userB, ' to ', teamA, ' due to: ', res,
               '. Exiting.'))
        sys.exit(1)

    ok, res = sdclient.list_memberships(teamA)
    if not ok:
        print(('-- Unable to fetch team memberships:', res, '. Exiting.'))
        sys.exit(1)
    elif userA not in list(res.keys()) or userB not in list(res.keys()) or admin not in list(res.keys()):
        print(('-- Users ', userA, ', ', userB, ' and ', admin, ' should be part of team ', teamA, '!', 'Exiting.'))
        sys.exit(1)
    elif res[userA] != 'ROLE_TEAM_READ' or res[userB] != 'ROLE_TEAM_EDIT':
        print(('-- Users ', userA, ' and ', userB, ' should have appropriate roles assigned for team ', teamA, '!',
               'Exiting.'))
        sys.exit(1)

    # Remove team memberships

    print('-- Remove team memberships')

    ok, res = sdclient.remove_memberships(teamA, [userB])
    if not ok:
        print(('-- Unable to remove membership for ', userB, ' from team', teamA, ' due to: ', res, '. Exiting.'))
        sys.exit(1)

    ok, res = sdclient.list_memberships(teamA)
    if not ok:
        print(('-- Unable to fetch team memberships:', res, '. Exiting.'))
        sys.exit(1)
    elif userB in list(res.keys()):
        print(('-- User ', userB, ' should not be part of team ', teamA, '!', 'Exiting.'))
        sys.exit(1)

    # Admin user cannot be removed from any team
    ok, res = sdclient.remove_memberships(teamB, [admin, userA])
    if not ok:
        print(('-- Unable to remove membership for ', userB, ' from team', teamA, ' due to: ', res, '. Exiting.'))
        sys.exit(1)

    ok, res = sdclient.list_memberships(teamB)
    if not ok:
        print(('-- Unable to fetch team memberships:', res, '. Exiting.'))
        sys.exit(1)
    elif userA in list(res.keys()):
        print(('-- User ', userA, ' should not be part of team ', teamB, '!', 'Exiting.'))
        sys.exit(1)
    elif admin not in list(res.keys()):
        print(('-- User ', admin, ' should be always part of all teams!', 'Exiting.'))
        sys.exit(1)

finally:
    #
    # Clean-up
    #
    print('Cleaning up...')

    print('-- Deleting test teams.')

    try:
        ok, res = sdclient.delete_team(teamA)
        if not ok:
            print(('-- Team \'', teamA, '\' deletion failed: ', res))
    except Exception as exception:
        print(('-- Team \'', teamA, '\' deletion failed: ', exception))

    try:
        ok, res = sdclient.delete_team(teamB)
        if not ok:
            print(('-- Team \'', teamB, '\' deletion failed: ', res))
    except Exception as exception:
        print(('-- Team \'', teamB, '\' deletion failed: ', exception))

    print('-- Deleting test users.')

    try:
        ok, res = sdclient.delete_user(admin)
        if not ok:
            print(('-- User \'', admin, '\' deletion failed: ', res))
    except Exception as exception:
        print(('-- User \'', admin, '\' deletion failed: ', exception))

    try:
        ok, res = sdclient.delete_user(userA)
        if not ok:
            print(('-- User \'', userA, '\' deletion failed: ', res))
    except Exception as exception:
        print(('-- User \'', userA, '\' deletion failed: ', exception))

    try:
        ok, res = sdclient.delete_user(userB)
        if not ok:
            print(('-- User \'', userB, '\' deletion failed: ', res))
    except Exception as exception:
        print(('-- User \'', userB, '\' deletion failed: ', exception))

print('All done successfully!!!')

sys.exit(0)
