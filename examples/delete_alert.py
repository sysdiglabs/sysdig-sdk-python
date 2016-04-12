#!/usr/bin/env python
#
# This example shows how to delete an alert
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

res = sdclient.get_alerts()
if not res[0]:
    print res[1]
    sys.exit(1)

for alert in res[1]['alerts']:
    if alert['name'] == "tomcat cpu > 80% on any host":
        print "Deleting alert"
        res = sdclient.delete_alert(alert)
        if not res[0]:
            print res[1]
            sys.exit(1)
