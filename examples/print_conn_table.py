#!/usr/bin/env python
#
# The request prints N entries from the conn table for the filter specified
# mimicking the top connections table in the Sysdig Monitor UI
#

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient

#
# Parse arguments
#
if len(sys.argv) not in [2, 3]:
    print 'usage: %s <sysdig-token> <hostname>' % sys.argv[0]
    print 'You can find your token at https://app.sysdigcloud.com/#/settings/user'
    sys.exit(1)

sdc_token = sys.argv[1]

if len(sys.argv) == 3:
    hostname = sys.argv[2]
else:
    hostname = None

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)

#
# Prepare the metrics list.
#
metrics = [
    {"id": "net.local.endpoint"},
    {"id": "net.local.service"},
    {"id": "net.remote.endpoint"},
    {"id": "net.remote.service"},
    {"id": "net.connection.count.total",
     "aggregations": {
         "time": "timeAvg",
         "group": "sum"
     }
    },
    {"id": "net.bytes.in",
     "aggregations": {
         "time": "timeAvg",
         "group": "avg"
     },
    },
    {"id": "net.bytes.out",
     "aggregations": {
         "time": "timeAvg",
         "group": "avg"
     }
    },
    {"id": "net.bytes.total",
     "aggregations": {
         "time": "timeAvg",
         "group": "avg"
     }
    },
    {"id": "net.request.count.in",
     "aggregations": {
         "time": "timeAvg",
         "group": "avg"
     }
    },
    {"id": "net.request.count.out",
     "aggregations": {
         "time": "timeAvg",
         "group": "avg"
     }
    },
    {"id": "net.request.count",
     "aggregations": {
         "time": "timeAvg",
         "group": "avg"
     }
    }
]

#
# Prepare the filter
#

if hostname is not None:
    flt = "host.hostName = '%s'" % hostname
else:
    flt = ""

#
# Time window:
#   - for "last X seconds": start is equal to -X, end is equal to 0
#
start = -7200
end = 0

#
# Fire the query.
#
page_size = 500
fetch_limit = 10000

cur = 0

row_format = "{:20.20}\t{:20.20}\t{:20.20}\t{:20.20}\t{:10}\t{:10}\t{:10}\t{:10}\t{:10}\t{:10}\t{:10}"

print row_format.format("Source", "Source Process", "Destination", "Destination Process", "Count",
                        "Bytes In", "Bytes Out", "Bytes", "Req In", "Req Out", "Req")

while cur < fetch_limit:
    paging = {'from': cur, 'to': cur + page_size}
    res = sdclient.get_data(metrics,
                            start,
                            end,
                            0,
                            flt,
                            'host',
                            paging)

    if not res[0]:
        sys.exit(res[1])

    data = res[1]['data']

    if len(data) == 0:
        break

    cur += len(data)
    for line in data:
        print row_format.format(*line['d'])
