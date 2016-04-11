#!/usr/bin/env python
#
# This script shows an advanced Sysdig Cloud data request that leverages
# filtering and segmentation.
#
# The request returns the last 10 minutes of CPU utilization for all of the
# containers inside the given host, with 1 minute data granularity
#

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient

#
# Parse arguments
#
if len(sys.argv) != 3:
    print 'usage: %s <sysdig-token> <hostname>' % sys.argv[0]
    print 'You can find your token at https://app.sysdigcloud.com/#/settings/user'
    sys.exit(1)

sdc_token = sys.argv[1]
hostname = sys.argv[2]

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)

#
# Prepare the metrics list.
#
metrics = [
    # The first metric we request is the container name. This is a segmentation
    # metric, and you can tell by the fact that we don't specify any aggregation
    # criteria. This entry tells Sysdig Cloud that we want to see the CPU
    # utilization for each container separately.
    {"id": "container.name"},
    # The second metric we reuest is the CPU. We aggregate it as an average.
    {"id": "cpu.used.percent",
     "aggregations": {
         "time": "avg",
         "group": "avg"
     }
    }
]

#
# Prepare the filter
#
filter = "host.hostName = '%s'" % hostname

#
# Fire the query.
#
res = sdclient.get_data(metrics, # metrics list
                        -600,   # start_ts = 600 seconds ago
                        0,      # end_ts = now
                        60,     # 1 data point per minute
                        filter, # The filter
                        'container') # The source for our metrics is the container

#
# Show the result!
#
if res[0]:
    data = res[1]
else:
    print res[1]
    sys.exit(1)

print data
