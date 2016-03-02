#!/usr/bin/env python
#
# Print email and agent limit of the Sysdig Cloud user identified 
# by the given token
#

import sys
sys.path.insert(0, '../')
from sdcclient import SdcClient

#
# Parse arguments
#
if len(sys.argv) != 2:
    print 'usage: %s <sysdig-token>' % sys.argv[0]
    sys.exit(0)

sdc_token = sys.argv[1]

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token, 'https://app.sysdigcloud.com')

#
# Post the event
#
res = sdclient.get_user_info()

#
# Return the result
#
if res[0]:
	uinfo = res[1]
else:
	print res[1]
	sys.exit(0)

print 'User Email: ' + uinfo['user']['username']
print 'Agent Limit: %s' % uinfo['user']['customerSettings']['plan']['maxAgents']
