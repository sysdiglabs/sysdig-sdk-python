#!/usr/bin/env python
#
# Resolve alert notifications from Sysdig Cloud
#

import os
import sys
import time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient

import logging
import httplib
httplib.HTTPConnection.debuglevel = 1

logging.basicConfig() # you need to initialize logging, otherwise you will not see anything from requests
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

#
# Parse arguments
#
if len(sys.argv) != 3:
    print 'usage: %s <sysdig-token> <num-days-to-resolve>' % sys.argv[0]
    print 'You can find your token at https://app.sysdigcloud.com/#/settings/user'
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
res = sdclient.get_notifications(from_ts=int(time.time() - int(num_days_to_resolve) * 86400),
                                 to_ts=int(time.time()), resolved=False)

if not res[0]:
    print res[1]
    sys.exit(1)

#
# Resolve them
#
notifications = res[1]['notifications']

print "Resolving " + str(len(notifications)) + " notifications"
for notification in notifications:
    notification.pop('nonNullFilter', None)
    res = sdclient.update_notification_resolution(notification, True)
    if not res[0]:
        print res[1]
        sys.exit(1)
