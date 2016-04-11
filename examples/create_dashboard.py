#!/usr/bin/env python
#
# This example shows two easy ways to create a dasboard: using a view as a
# templeate, and copying another dashboard.
# In both cases, a filter is used to define what entities the new dashboard
# will monitor.
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
sdclient = SdcClient(sdc_token)

#
# Create the new dashboard, apllying to cassandra in production
#
res = sdclient.create_dashboard_from_view("API test - cassandra in prod", # The name we're giving to the new dashboard.
	"Overview by Process", # The view we're copying.
	'kubernetes.namespace.name=prod and proc.name = cassandra') # the filter specifying what this dasboard appies to.
																# Remember that here you can use combinations of any
																# segmentation criteria that you find in the Sysdig 
																# Cloud explore page.
#
# Check the result
#
if res[0]:
	print 'Dashboard created successfully'
else:
	print res[1]
	sys.exit(0)

#
# Make a Copy the just created dasboard, this time applying it to cassandra in the dev namespace
#
res = sdclient.create_dashboard_from_dashboard("API test - cassandra in dev", # The name we're giving to the new dashboard.
	"API test - cassandra in prod", # The view we're copying.
	'kubernetes.namespace.name=dev and proc.name = cassandra') # the filter specifying what this dasboard appies to.

#
# Check the result
#
if res[0]:
	print 'Dashboard copied successfully'
else:
	print res[1]

