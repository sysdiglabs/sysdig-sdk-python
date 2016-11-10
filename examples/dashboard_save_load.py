#!/usr/bin/env python
#
# Save the first user dashboard to file and then use create_dashboard_from_file()
# to apply the stored dasboard again with a different filter.
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

#
# Serialize the first user dashboard to disk
#
res = sdclient.get_dashboards()

if not res[0]:
    print res[1]
    sys.exit(1)

if len(res[1][u'dashboards']) > 0:
    with open('dashboard.json', 'w') as outf:
        json.dump(res[1][u'dashboards'][0], outf)
else:
    print 'the user has no dashboards. Exiting.'
    sys.exit(0)

#
# Now create the dashboard from the file. We use a filter for the Cassandra process
# as an example.
#

dashboardFilter = "proc.name = cassandra"

res = sdclient.create_dashboard_from_file('test dasboard from file', 'dashboard.json', dashboardFilter)

if res[0]:
    print 'Dashboard created successfully'
else:
    print res[1]
    sys.exit(1)
