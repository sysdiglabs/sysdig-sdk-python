#!/usr/bin/env python
#
# This script shows how to use the update_alert() call to modify the
# details of an existing alert.
#
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
    print(('usage: %s [-a|--alert <name>] <sysdig-token>' % sys.argv[0]))
    print('-a|--alert: Comma seperated list of alerts')
    print('You can find your token at https://app.sysdigcloud.com/#/settings/user')
    sys.exit(1)


try:
    opts, args = getopt.getopt(sys.argv[1:], "a:", ["alert="])
except getopt.GetoptError:
    usage()

alert_list = "95% CPU"
for opt, arg in opts:
    if opt in ("-a", "--alert"):
        alert_list = arg

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
    if alert['name'] in alert_list:
        alert_found = True
        print(("Updating \'" + alert['name'] + "\'. Enabled status before change:"))
        print((alert['enabled']))
        if alert['enabled'] == True:
            alert['enabled'] = False
        else:
            alert['enabled'] = True
        ok, res_update = sdclient.update_alert(alert)

        if not ok:
            print(res_update)
            sys.exit(1)

        # Validate and print the results
        print('Alert status after modification:')
        print((alert['enabled']))
        print(' ')

if not alert_found:
    print('Alert to be updated not found')
    sys.exit(1)
