#!/usr/bin/env python
#
# Delete user events from Sysdig Cloud
#

import getopt
import json
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient

#
# Parse arguments
#
def usage():
    print 'usage: %s [-e|--event <name>] <sysdig-token>' % sys.argv[0]
    print '-e|--event: Name of event to delete'
    print 'You can find your token at https://app.sysdigcloud.com/#/settings/user'
    sys.exit(1)

try:
    opts, args = getopt.getopt(sys.argv[1:],"e:",["event="])
except getopt.GetoptError:
    usage()

event_name = "test_event_name"
for opt, arg in opts:
    if opt in ("-e", "--event"):
        event_name = arg

if len(args) != 1:
    usage()

sdc_token = args[0]

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)

#
# Get the events that match a name
#
res = sdclient.get_events(name=event_name)

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
