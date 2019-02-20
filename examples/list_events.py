#!/usr/bin/env python
#
# Get user events from Sysdig Cloud
#

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient


def print_events(data):
    for event in data['events']:
        event['sev'] = event['severity'] if event.get('severity') else 'not set'
        print('time: %(timestamp)d, name: %(name)s, description: %(description)s, severity: %(sev)s' % event)


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
# Get the entire list of events
#
ok, res = sdclient.get_events()

if ok:
    print_events(res)
else:
    print(res)
    sys.exit(1)

#
# Get the events that match a period in time
#
ok, res = sdclient.get_events(from_ts=1460365211, to_ts=1460465211)

if ok:
    print_events(res)
else:
    print(res)
    sys.exit(1)

#
# Get the events that match a name
#
ok, res = sdclient.get_events(name='test event')

if ok:
    print_events(res)
else:
    print(res)
    sys.exit(1)

#
# Get the events that match a tag/value pair
#
ok, res = sdclient.get_events(tags="tag1 = 'value1'")

if ok:
    print_events(res)
else:
    print(res)
    sys.exit(1)
