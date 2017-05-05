#!/usr/bin/env python
#
# This script shows how to use the update_alert() call to modify the
# details of an existing alert.
#
#

import os
import sys
import json
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

res = sdclient.get_alerts()
if not res[0]:
    print res[1]
    sys.exit(1)

alert_found = False
for alert in res[1]['alerts']:
    if alert['name'] == "tomcat cpu > 80% on any host":
        alert_found = True
        print 'Updating alert. Configuration before changing timespan, description, and notification channels:'
        print json.dumps(alert, sort_keys=True, indent=4)
        if 'notificationChannelIds' in alert:
            alert['notificationChannelIds'] = alert['notificationChannelIds'][0:-1]
        update_txt = ' (changed by update_alert)'
        if alert['description'][-len(update_txt):] != update_txt:
            alert['description'] = alert['description'] + update_txt
        alert['timespan'] = alert['timespan'] * 2   # Note: Expressed in seconds * 1000000
        res_update = sdclient.update_alert(alert)

        if not res_update[0]:
            print res_update[1]
            sys.exit(1)

        # Validate and print the results
        print '\nAlert after modification:'
        print json.dumps(res_update[1], sort_keys=True, indent=4)

if not alert_found:
    print 'Alert to be updated not found'
    sys.exit(1)
