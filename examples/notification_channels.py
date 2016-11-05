#!/usr/bin/env python
#
# This script shows how to manipulate the notification channel list for alerts
#

import os
import sys
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
# Create an email notification channel
#
res = sdclient.create_email_notification_channel('Api Channel', ['gianluca.borello@sysdig.com', 'foo@sysdig.com', 'bar@sysdig.com'])
if not res[0]:
    print res[1]
    sys.exit(1)

#
# The notification channel will contain the id, that can be used when creating alerts
#
channel = res[1]['notificationChannel']
print channel

#
# Notification channels can also be programmatically deleted
#
res = sdclient.delete_notification_channel(channel)
if not res[0]:
    print res[1]
    sys.exit(1)
