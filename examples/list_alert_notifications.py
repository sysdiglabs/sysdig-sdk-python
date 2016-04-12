#!/usr/bin/env python
#
# Get alert notifications from Sysdig Cloud
#

import os
import sys
import time
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
# Get the notifications in the last day
#
res = sdclient.get_notifications(from_ts=int(time.time()-86400), to_ts=int(time.time()))

print res[1]
if not res[0]:
	sys.exit(1)

#
# Get the notifications in the active state
#
res = sdclient.get_notifications(from_ts=int(time.time()-86400), to_ts=int(time.time()), state='ACTIVE')

print res[1]
if not res[0]:
	sys.exit(1)

#
# Get the notifications in the active state
#
res = sdclient.get_notifications(from_ts=int(time.time()-86400), to_ts=int(time.time()), state='OK')

print res[1]
if not res[0]:
	sys.exit(1)

#
# Get the resolved notifications
#
res = sdclient.get_notifications(from_ts=int(time.time()-86400), to_ts=int(time.time()), resolved=True)

print res[1]
if not res[0]:
	sys.exit(1)
