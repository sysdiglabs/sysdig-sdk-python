#!/usr/bin/env python
#
# This script shows how to use the create_alert() call to create the following
# Sysdig Cloud alert: 'send an email notification when the CPU of any tomcat
# process running on any of the instrumented machines goes over 80%'
#
#

import sys
sys.path.insert(0, '../')
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
                            ['EMAIL'], # Notification target. We want an email to be sent. Alerts email recipients can be defined here: https://app.sysdigcloud.com/#/settings/notifications
                            False) # This alert will be disabled when it's created.

#
# Validate a print the results.
#
if res[0]:
    data = res[1]
else:
    print res[1]
    sys.exit(1)

print res
