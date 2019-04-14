#!/usr/bin/env python
#
# Save/restore dashboards
#

import os
import sys
import zipfile
import json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdMonitorClient

#
# Parse arguments
#
if len(sys.argv) != 3:
    print('usage: %s <sysdig-token> <file-name>' % sys.argv[0])
    print('You can find your token at https://app.sysdigcloud.com/#/settings/user')
    sys.exit(1)

sdc_token = sys.argv[1]
dashboard_state_file = sys.argv[2]

#
# Instantiate the SDC client
#
sdclient = SdMonitorClient(sdc_token)

zipf = zipfile.ZipFile(dashboard_state_file, 'r')

for info in zipf.infolist():
    data = zipf.read(info.filename)
    try:
        j = json.loads(data)
    except ValueError:
        print('Invalid JSON file found in ZIP file ' + info.filename + ': skipping')
        continue

    #
    # Handle old files
    #
    if 'dashboard' in j:
        j = j['dashboard']

    ok, res = sdclient.create_dashboard_with_configuration(j)
    if ok:
        print('Restored Dashboard named: ' + j['name'])
    else:
        print("Dashboard creation failed for dashboard name %s with error %s" % (j['name'], res))
