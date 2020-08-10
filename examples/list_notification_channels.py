#!/usr/bin/env python
#
# Post a user event to Sysdig Cloud
#

import json
import sys

from sdcclient import SdcClient

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
# Post the event
#
ok, res = sdclient.list_notification_channels()

#
# Return the result
#
if ok:
    print((json.dumps(res['notificationChannels'], indent=4)))
else:
    print(res)
    sys.exit(1)
