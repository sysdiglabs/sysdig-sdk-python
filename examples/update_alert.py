#!/usr/bin/env python
#
# This script shows how to use the update_alert() call to modify the
# details of an existing alert.
#
#

import getopt
import os
import sys
import json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient


#
# Parse arguments
#
def usage():
    print('usage: %s [-a|--alert <name>] <sysdig-token>' % sys.argv[0])
    print('-a|--alert: Set name of alert to update')
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

ok, res = sdclient.get_alerts()
if not ok:
    print(res)
    sys.exit(1)

alert_found = False
for alert in res['alerts']:
    if alert['name'] == alert_name:
        alert_found = True
        print('Updating alert. Configuration before changing timespan, description, and notification channels:')
        print(json.dumps(alert, sort_keys=True, indent=4))
        if 'notificationChannelIds' in alert:
            alert['notificationChannelIds'] = alert['notificationChannelIds'][0:-1]
        update_txt = ' (changed by update_alert)'
        if alert['description'][-len(update_txt):] != update_txt:
            alert['description'] = alert['description'] + update_txt
        alert['timespan'] = alert['timespan'] * 2   # Note: Expressed in seconds * 1000000
        ok, res_update = sdclient.update_alert(alert)

        if not ok:
            print(res_update)
            sys.exit(1)

        # Validate and print the results
        print('\nAlert after modification:')
        print(json.dumps(res_update, sort_keys=True, indent=4))

if not alert_found:
    print('Alert to be updated not found')
    sys.exit(1)
