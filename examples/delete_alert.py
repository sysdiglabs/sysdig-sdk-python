#!/usr/bin/env python
#
# This example shows how to delete an alert
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
    print('-a|--alert: Set name of alert to delete')
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

for alert in res['alerts']:
    if alert['name'] == alert_name:
        print("Deleting alert")
        ok, res = sdclient.delete_alert(alert)
        if not ok:
            print(res)
            sys.exit(1)
