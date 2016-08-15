#!/usr/bin/env python
#
# This script shows how to use the create_alert() call to create the following
# Sysdig Cloud alert: 'send an email notification when the CPU of any tomcat
# process running on any of the instrumented machines goes over 80%'
#
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
# Find notification channels (you need IDs to create an alert).
#
notify_channels = [ {'type': 'SLACK', 'channel': '#sysdig-demo2-alerts'},
                    {'type': 'EMAIL', 'emailRecipients': ['kini@sysdig.com']},
                    {'type': 'SNS', 'snsTopicARNs': ['arn:aws:sns:us-east-1:273107874544:alarms-stg']}
                    ]
res = sdclient.get_notification_ids(notify_channels)
if not res[0]:
    print "Could not get IDs and hence not creating the alert: " + res[1]
    sys.exit(-1)

notification_channel_ids = res[1]

#
# Create the alert.
#
res = sdclient.create_alert('tomcat cpu > 80% on any host',  # Alert name.
                            'this alert was automatically created using the python Sysdig Cloud library', # Alert description.
                            6, # Syslog-encoded severity. 6 means 'info'.
                            60, # The alert will fire if the condition is met for at least 60 seconds.
                            'avg(cpu.used.percent) > 80', # The condition.
                            ['host.mac', 'proc.name'], # Segmentation. We want to check this metric for every process on every machine.
                            'ANY', # in case there is more than one tomcat process, this alert will fire when a single one of them crosses the 80% threshold.
                            'proc.name = "tomcat"', # Filter. We want to receive a notification only if the name of the process meeting the condition is 'tomcat'.
                            notification_channel_ids,
                            False) # This alert will be disabled when it's created.

#
# Validate a print the results.
#
print res[1]
if not res[0]:
    sys.exit(1)
