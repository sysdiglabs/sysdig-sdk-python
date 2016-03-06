#!/usr/bin/env python
#
# Post a user event to Sysdig Cloud
#

import sys
sys.path.insert(0, '../')
from sdcclient import SdcClient

#
# Parse arguments
#
if len(sys.argv) != 2:
    print 'usage: %s <sysdig-token>' % sys.argv[0]
    print 'You can find your token at https://app.sysdigcloud.com/#/settings/user'
    sys.exit(0)

sdc_token = sys.argv[1]

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token, 'https://app.sysdigcloud.com')

#
# Post the event
#
res = sdclient.create_dashboard_from_view("API test dasboard 1", 
	"Overview by Process", 
#	[{'kubernetes.namespace.name': 'prod'}, {'proc.name': 'cassandra'}])
	'kubernetes.namespace.name=prod and proc.name = cassandra')

#
# Check the result
#
print res
sys.exit(0)
if res[0]:
	print 'Dashboard created successfully'
else:
	print res[1]
