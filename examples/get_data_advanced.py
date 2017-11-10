#!/usr/bin/env python
#
# This script shows an advanced Sysdig Monitor data request that leverages
# filtering and segmentation.
#
# The request returns the last 10 minutes of CPU utilization for the 5
# busiest containers inside the given host, with 1 minute data granularity
#

import os
import sys
import json
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
    # criteria. This entry tells Sysdig Monitor that we want to see the CPU
    # utilization for each container separately.
    {"id": "container.name"},
    # The second metric we request is the CPU. We aggregate it as an average.
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
# Paging (from and to included; by default you get from=0 to=9)
# Here we'll get the top 5.
#
paging = { "from": 0, "to": 4 }

#
# Fire the query.
#
res = sdclient.get_data(metrics=metrics,               # List of metrics to query
                        start_ts=-600,                 # Start of query span is 600 seconds ago
                        end_ts=0,                      # End the query span now
                        sampling_s=60,                 # 1 data point per minute
                        filter=filter,                 # The filter specifying the target host
                        paging=paging,                 # Paging to limit to just the 5 most busy
                        datasource_type='container')   # The source for our metrics is the container

#
# Show the result!
#
print json.dumps(res[1], sort_keys=True, indent=4)
if not res[0]:
    sys.exit(1)
