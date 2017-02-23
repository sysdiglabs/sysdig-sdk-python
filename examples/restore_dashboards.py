#!/usr/bin/env python
#
# Save/restore dashboards
#

import os
import sys
import zipfile
import json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient

#
# Parse arguments
#
if len(sys.argv) != 3:
    print 'usage: %s <sysdig-token> <file-name>' % sys.argv[0]
    print 'You can find your token at https://app.sysdigcloud.com/#/settings/user'
    sys.exit(1)

sdc_token = sys.argv[1]
dashboard_state_file = sys.argv[2]

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)

zipf = zipfile.ZipFile(dashboard_state_file, 'r')

for info in zipf.infolist():
    data = zipf.read(info.filename)
    dboard = json.loads(data)
    
    dboard['timeMode'] = {'mode' : 1}
    dboard['time'] = {'last' : 2 * 60 * 60 * 1000000, 'sampling' : 2 * 60 * 60 * 1000000}

    # Single filter support for all restored dashboards
    # TODO: add support to get filter from saved dashboard
    dashboardFilter = "proc.name = cassandra"
    res = sdclient.create_dashboard_from_template(dboard['name'] + '-restored', dboard, dashboardFilter)
    if res[0] == False:
        print "Dashboard creation failed for dashboard name %s with error %s" % (j['name'], res[1])
