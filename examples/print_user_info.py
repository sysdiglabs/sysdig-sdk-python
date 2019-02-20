#!/usr/bin/env python
#
# Print email, current and maximum number of agents for the Sysdig Cloud user
# identified by the given token.
#

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient

#
# Parse arguments
#
if len(sys.argv) != 2:
    print('usage: %s <sysdig-token>' % sys.argv[0])
    print('You can find your token at https://app.sysdigcloud.com/#/settings/user')
    sys.exit(1)

sdc_token = sys.argv[1]

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)

#
# Get the required info
#
ok, res = sdclient.get_user_info()

if ok:
    uinfo = res
else:
    print(res)
    sys.exit(1)

ok, res = sdclient.get_n_connected_agents()

#
# Print the results
#
if ok:
    nagents = res
else:
    print(res)
    sys.exit(1)

print('User Email: ' + uinfo['user']['username'])
print('Current Agents: %d' % nagents)
print('Max Agents: %s' % uinfo['user']['customerSettings']['plan']['maxAgents'])
