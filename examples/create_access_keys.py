#!/usr/bin/env python
#
# List all the access keys in a Sysdig Monitor environment. The token you provide must
# have Admin rights.
#

import sys

from sdcclient import SdcClient

#
# Parse arguments
#
if len(sys.argv) != 2:
    print('usage: %s <sysdig-token>' % sys.argv[0])
    print('You can find your token at https://app.sysdigcloud.com/#/settings/user')
    print('For this script to work, the user for the token must have Admin rights')
    sys.exit(1)

sdc_token = sys.argv[1]

# Maximum number of agents allowed to connect for this access key. Set to '' if not required
agent_limit = ''
# Number of agent licenses that are ALWAYS available to this access key. This directly counts against the maximum number of available licenses. Set to '' if not required.
agent_reserved = ''
# Team ID to which to assign the access key. Team ID must be valid. Set to '' if not required.
team_id = ''


#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token, 'https://app.sysdigcloud.com')

#
# Get the configuration
#
ok, res = sdclient.create_access_key(
    agent_limit,
    agent_reserved,
    team_id)

if ok:
    print('Access Key: {}\nTeam ID: {}\nAgent Limit: {}\nAgent Reserved: {}\n==========='.format(res['customerAccessKey']['accessKey'], res['customerAccessKey']['teamId'], res['customerAccessKey']['limit'], res['customerAccessKey']['reservation']))
else:
    print(res)
    sys.exit(1)
