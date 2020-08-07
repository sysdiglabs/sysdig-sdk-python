#!/usr/bin/env python
#
# Resolve alert notifications from Sysdig Cloud
#

import os
import sys
import time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient

#
# Parse arguments
#
if len(sys.argv) != 3:
    print(('usage: %s <sysdig-token> <num-days-to-resolve>' % sys.argv[0]))
    print('You can find your token at https://app.sysdigcloud.com/#/settings/user')
    sys.exit(1)

sdc_token = sys.argv[1]
num_days_to_resolve = sys.argv[2]

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)

#
# Get the unresolved notifications in the last day
#
ok, res = sdclient.get_notifications(from_ts=int(time.time() - int(num_days_to_resolve) * 86400),
                                     to_ts=int(time.time()), resolved=False)

if not ok:
    print(res)
    sys.exit(1)

#
# Resolve them
#
notifications = res['notifications']

print(("Resolving " + str(len(notifications)) + " notifications"))
for notification in notifications:
    ok, res = sdclient.update_notification_resolution(notification, True)
    if not ok:
        print(res)
        sys.exit(1)
