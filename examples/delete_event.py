#!/usr/bin/env python
#
# Delete user events from Sysdig Cloud
#

import json
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient

#
# Parse arguments
#
if len(sys.argv) != 2:
    print 'usage: %s <sysdig-token>' % sys.argv[0]
    print 'You can find your token at https://app.sysdigcloud.com/#/settings/user'
    sys.exit(1)

sdc_token = sys.argv[1]

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)

#
# Get the events that match a name
#
res = sdclient.get_events(name='test event')

if not res[0]:
	print res[1]
	sys.exit(1)

#
# Delete the first event among the returned ones
#
for event in res[1]['events']:
	print "Deleting event " + event['name']

	res = sdclient.delete_event(event)

	if not res[0]:
		print res[1]
		sys.exit(1)
