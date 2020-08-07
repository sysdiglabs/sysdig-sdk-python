#!/usr/bin/env python
#
# Get alert notifications from Sysdig Cloud
#

import os
import sys
import time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient


def print_notifications(notifications):
    for notification in notifications:
        values = []
        for entity in notification['entities']:
            for value in entity['metricValues']:
                values.append(str(value['value']))
        notification.update({'values': ','.join(values)})
        print("#%(id)s, State: %(state)s, Severity: %(severity)s, Scope: %(filter)s, Condition: %(condition)s, Value: %(values)s, Resolved: %(resolved)s" %
              notification)


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
# Get the notifications in the last day
#
ok, res = sdclient.get_notifications(
    from_ts=int(time.time() - 86400),
    to_ts=int(time.time()))

print_notifications(res['notifications'])
if not ok:
    sys.exit(1)

#
# Get the notifications in the last day and active state
#
ok, res = sdclient.get_notifications(
    from_ts=int(time.time() - 86400),
    to_ts=int(time.time()), state='ACTIVE')

print_notifications(res['notifications'])
if not ok:
    sys.exit(1)

#
# Get the notifications in the last day and active state
#
ok, res = sdclient.get_notifications(
    from_ts=int(time.time() - 86400),
    to_ts=int(time.time()), state='OK')

print_notifications(res['notifications'])
if not ok:
    sys.exit(1)

#
# Get the notifications in the last day and resolved state
#
ok, res = sdclient.get_notifications(
    from_ts=int(time.time() - 86400),
    to_ts=int(time.time()),
    resolved=True)

print_notifications(res['notifications'])
if not ok:
    sys.exit(1)
