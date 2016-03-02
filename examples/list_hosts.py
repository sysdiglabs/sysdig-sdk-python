#!/usr/bin/env python
#
# This script shows how to leverage sysdig's data query API to obtain the list
# of the instrumented hosts that have been seen in the last 5 minutes.
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
# Prepare the query's metrics list. In this case, we have just one metric: 
# host.hostName. This is a 'key' metric, and we don't include any number metric.
# Essentially, we create an 'enumeration' of hostnames.
#
metrics = [{"id": "host.hostName"}]

#
# Fire the query.
# Note: there's no sampling time. This means that we're requesting the result to
#       come as a single sample.
#
res = sdclient.get_data(metrics, # metrics list 
    -300,   # cover the last 300 seconds...
    0)      # ... ending now

#
# Show the results!
#
if res[0]:
	data = res[1]
else:
	print res[1]
	sys.exit(0)

print data
