#!/usr/bin/env python
#
# Get all policy events for a given time range or in the last N seconds.
# The events are written in jsonl format to stdout.
# Progress information is written to standard error.
#

import os
import sys
import json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdSecureClient

def usage():
    print 'usage: %s <sysdig-token> [<duration sec>|<from sec> <to sec>]' % sys.argv[0]
    print 'You can find your token at https://secure.sysdig.com/#/settings/user'
    sys.exit(1)

#
# Parse arguments
#
if len(sys.argv) < 3:
    usage()

sdc_token = sys.argv[1]

duration = None
from_sec = None
to_sec = None

if len(sys.argv) == 3:
    duration = sys.argv[2]
elif len(sys.argv) == 4:
    from_sec = sys.argv[2]
    to_sec = sys.argv[3]
else:
    usage()

#
# Instantiate the SDC client
#
sdclient = SdSecureClient(sdc_token, 'https://secure.sysdig.com')

if duration is not None:
    res = sdclient.get_policy_events_duration(duration)
else:
    res = sdclient.get_policy_events_range(from_sec, to_sec)

while True:

    #
    # Return the result
    #
    if not res[0]:
        print res[1]
        sys.exit(1)

    if len(res[1]['data']['policyEvents']) == 0:
        break

    sys.stderr.write("offset={}\n".format(res[1]['ctx']['offset']))

    for event in res[1]['data']['policyEvents']:
        sys.stdout.write(json.dumps(event) + "\n")

    res = sdclient.get_more_policy_events(res[1]['ctx'])
