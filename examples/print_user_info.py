#!/usr/bin/env python
#
# Print email, current and maximum number of agents for the Sysdig Cloud user 
# identified by the given token.
#

import sys
sys.path.insert(0, '../')
from sdcclient import SdcClient

#
# Parse arguments
#
if len(sys.argv) != 2:
    print 'usage: %s <sysdig-token>' % sys.argv[0]
    print 'You can find your token at https://app.sysdigcloud.com/#/settings/user'
    sys.exit(0)

sdc_token = sys.argv[1]

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token, 'https://app.sysdigcloud.com')

#
# Get the required info
#
res = sdclient.get_user_info()

if res[0]:
	uinfo = res[1]
else:
	print res[1]
	sys.exit(0)

res = sdclient.get_n_connected_agents()

#
# Print the results
#
if res[0]:
	nagents = res[1]
else:
	print res[1]
	sys.exit(0)

print 'User Email: ' + uinfo['user']['username']
print 'Current Agents: %d' % nagents
print 'Max Agents: %s' % uinfo['user']['customerSettings']['plan']['maxAgents']
