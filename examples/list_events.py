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
        event['sev'] = event.get('severity', 'not set')
        event['description'] = event.get('description', 'not set')
        print(('id: %(id)s, time: %(timestamp)d, name: %(name)s, description: %(description)s, severity: %(sev)s' % event))


#
# Parse arguments
#
if len(sys.argv) != 2:
    print(('usage: %s <sysdig-token>' % sys.argv[0]))
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
# Get the events before other event
#
ok, res = sdclient.get_events(pivot=res['events'][-1]["id"])

if ok:
    print_events(res)
else:
    print(res)
    sys.exit(1)

#
# Get the events that match a category
#
ok, res = sdclient.get_events(category=["kubernetes"])

if ok:
    print_events(res)
else:
    print(res)
    sys.exit(1)

#
# Get the events that match a status
#
ok, res = sdclient.get_events(status=['triggered', 'unacknowledged'])

if ok:
    print_events(res)
else:
    print(res)
    sys.exit(1)

#
# Get the last event only
#
ok, res = sdclient.get_events(limit=1)

if ok:
    print_events(res)
else:
    print(res)
    sys.exit(1)
