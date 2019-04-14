#!/usr/bin/env python
#
# Print the list of dashboards.
#

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdMonitorClient

#
# Parse arguments
#
if len(sys.argv) != 2:
    print('usage: %s <sysdig-token>' % sys.argv[0])
    print('You can find your token at https://app.sysdigcloud.com/#/settings/user')
    sys.exit(1)

sdc_token = sys.argv[1]

#
# Instantiate the SDC client
#
sdclient = SdMonitorClient(sdc_token)

#
# Fire the request.
#
ok, res = sdclient.get_dashboards()

#
# Show the list of dashboards
#
if not ok:
    print(res)
    sys.exit(1)

for db in res['dashboards']:
    print("Name: %s, # Charts: %d" % (db['name'], len(db['widgets'] if 'widgets' in db else [])))
