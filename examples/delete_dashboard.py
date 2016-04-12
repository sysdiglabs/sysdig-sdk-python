#!/usr/bin/env python
#
# This example shows how to delete a dashboard
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
# List the dashboards
#
res = sdclient.get_dashboards()
if not res[0]:
    print res[1]
    sys.exit(1)

#
# Delete all the dashboards containing "API test"
#
for dashboard in res[1]['dashboards']:
    if 'API test' in dashboard['name']:
        print "Deleting " + dashboard['name']
        res = sdclient.delete_dashboard(dashboard)
        if not res[0]:
            print res[1]
            sys.exit(1)
