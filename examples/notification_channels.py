#!/usr/bin/env python
#
# This script shows how to manipulate the notification channel list for alerts
#

import getopt
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient


#
# Parse arguments
#
def usage():
    print('usage: %s [-c|--channel <name>] <sysdig-token>' % sys.argv[0])
    print('-c|--channel: Set name of channel to create')
    print('You can find your token at https://app.sysdigcloud.com/#/settings/user')
    sys.exit(1)


try:
    opts, args = getopt.getopt(sys.argv[1:], "c:", ["channel="])
except getopt.GetoptError:
    usage()

# Name for the dashboard to create
channel_name = "Api Channel"
for opt, arg in opts:
    if opt in ("-c", "--channel"):
        channel_name = arg

if len(args) != 1:
    usage()

sdc_token = args[0]

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)

#
# Create an email notification channel
#
ok, res = sdclient.create_email_notification_channel(channel_name, ['gianluca.borello@sysdig.com', 'foo@sysdig.com', 'bar@sysdig.com'])
if not ok:
    print(res)
    sys.exit(1)

#
# The notification channel will contain the id, that can be used when creating alerts
#
channel = res['notificationChannel']
print(channel)

#
# Notification channels can also be programmatically deleted
#
ok, res = sdclient.delete_notification_channel(channel)
if not ok:
    print(res)
    sys.exit(1)
