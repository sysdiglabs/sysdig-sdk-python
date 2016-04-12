#!/usr/bin/env python
#
# Get user events from Sysdig Cloud
#

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient

#
# Parse arguments
#
# if len(sys.argv) < 4:
#     print 'usage: %s <sysdig-token> name description [severity]' % sys.argv[0]
#     print 'You can find your token at https://app.sysdigcloud.com/#/settings/user'
#     sys.exit(1)

sdc_token = sys.argv[1]

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)

#
# Get the entire list of events
#
res = sdclient.get_events()

print res[1]
if not res[0]:
	sys.exit(1)

#
# Get the events that match a period in time
#
res = sdclient.get_events(from_ts=1460365211, to_ts=1460465211)

print res[1]
if not res[0]:
	sys.exit(1)

#
# Get the events that match a name
#
res = sdclient.get_events(name='test event')

print res[1]
if not res[0]:
	sys.exit(1)

#
# Get the events that match a tag/value pair
#
res = sdclient.get_events(tags="tag1 = 'value1'")

print res[1]
if not res[0]:
	sys.exit(1)
