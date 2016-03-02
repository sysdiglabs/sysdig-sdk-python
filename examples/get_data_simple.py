#!/usr/bin/env python
#
# This script shows the basics of getting data out of Sysdig Cloud by crating a 
# very simple request that has no filter an no segmentation.
#
# The request queries for the average CPU across all of the instrumented hosts for 
# the last 10 minutes, with 1 minute data granularity
#

import sys
sys.path.insert(0, '../')
from sdcclient import SdcClient

#
# Parse arguments
#
if len(sys.argv) != 2:
    print 'usage: %s <sysdig-token>' % sys.argv[0]
    sys.exit(0)

sdc_token = sys.argv[1]

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token, 'https://app-staging2.sysdigcloud.com')

#
# Prepare the metrics list. In this case, we have just one metric: cpu.used.percent, 
# without segmentation.
# The data will be aggregated as average both in time and across the hosts.
#
metrics = [
    {"id": "cpu.used.percent",
    "aggregations": {
        "time": "avg",
        "group": "avg"
    }
}]

#
# Fire the query.
#
res = sdclient.get_data(metrics, # metrics list 
    -600,   # start_ts = 600 seconds ago
    0,      # end_ts = now
    60)     # 1 data point per minute

#
# Show the result
#
if res[0]:
	data = res[1]
else:
	print res[1]
	sys.exit(0)

print data
