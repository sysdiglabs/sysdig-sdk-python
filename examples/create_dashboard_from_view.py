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
    print 'You can find your token at https://app-staging2.sysdigcloud.com/#/settings/user'
    sys.exit(0)

sdc_token = sys.argv[1]

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token, 'https://app-staging2.sysdigcloud.com')

#
# Post the event
#
res = sdclient.create_dashboard_from_view("API test dasboard", "Top Processes", [{'proc.name': 'cassandra'}])
#res = sdclient.get_views_list()


#
# Return the result
#
if res[0]:
	print 'Recipient added successfully'
else:
	print res[1]
