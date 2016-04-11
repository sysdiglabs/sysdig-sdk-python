#!/usr/bin/env python
#
# This example shows how to delete a dashboard
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

res = sdclient.delete_dashboard("API test - cassandra in prod")
if res:
    print 'Dashboard deleted successfully'
else:
    print res[1]
    sys.exit(0)

res = sdclient.delete_dashboard("API test - cassandra in dev")
if res:
    print 'Dashboard deleted successfully'
else:
    print res[1]
    sys.exit(0)
