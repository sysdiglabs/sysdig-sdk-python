#!/usr/bin/env python
#
# This script shows how to use the create_alert() call to create the following
# Sysdig Cloud alert: 'send an email notification when the CPU of any tomcat
# process running on any of the instrumented machines goes over 80%'
#
#

import getopt
import sys

from sdcclient import SdcClient


#
# Parse arguments
#
def usage():
    print(('usage: %s [-a|--alert <name>] <sysdig-token>' % sys.argv[0]))
    print('-a|--alert: Set name of alert to create')
    print('You can find your token at https://app.sysdigcloud.com/#/settings/user')
    sys.exit(1)


try:
    opts, args = getopt.getopt(sys.argv[1:], "a:", ["alert="])
except getopt.GetoptError:
    usage()

alert_name = "tomcat cpu > 80% on any host"
for opt, arg in opts:
    if opt in ("-a", "--alert"):
        alert_name = arg

if len(args) != 1:
    usage()

sdc_token = args[0]

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)

#
# Find notification channels (you need IDs to create an alert).
#
notify_channels = [{'type': 'SLACK', 'channel': '#python-sdc-test-alert'},
                   {'type': 'EMAIL', 'emailRecipients': ['python-sdc-testing@draios.com', 'test@sysdig.com']},
                   {'type': 'SNS', 'snsTopicARNs': ['arn:aws:sns:us-east-1:273107874544:alarms-stg']}
                   ]

ok, res = sdclient.get_notification_ids(notify_channels)
if not ok:
    print(("Could not get IDs and hence not creating the alert: " + res))
    sys.exit(-1)

notification_channel_ids = res

#
# Create the alert.
#
ok, res = sdclient.create_alert(
    alert_name,  # Alert name.
    'this alert was automatically created using the python Sysdig Cloud library',  # Alert description.
    6,  # Syslog-encoded severity. 6 means 'info'.
    60,  # The alert will fire if the condition is met for at least 60 seconds.
    'avg(cpu.used.percent) > 80',  # The condition.
    ['host.mac', 'proc.name'],  # Segmentation. We want to check this metric for every process on every machine.
    'ANY',
    # in case there is more than one tomcat process, this alert will fire when a single one of them crosses the 80% threshold.
    'proc.name = "tomcat"',
    # Filter. We want to receive a notification only if the name of the process meeting the condition is 'tomcat'.
    notification_channel_ids,
    False)  # This alert will be disabled when it's created.

#
# Validate a print the results.
#
print(res)
if not ok:
    sys.exit(1)
