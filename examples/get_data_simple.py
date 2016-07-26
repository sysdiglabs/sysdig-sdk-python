#!/usr/bin/env python
#
# This script shows the basics of getting data out of Sysdig Cloud by crating a
# very simple request that has no filter an no segmentation.
#
# The request queries for the average CPU across all of the instrumented hosts for
# the last 10 minutes, with 1 minute data granularity
#

import os
import sys
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

sdclient = SdcClient(sdc_token)

#
# List of metrics to export. Imagine a SQL data table, with key columns and value columns
# You just need to specify the ID for keys, and ID with aggregation for values.
#
metrics =   [
                # { "id": "agent.tag.team" },
                # { "id": "kubernetes.pod.label.name" },
                # { "id": "agent.tag.env", "aggregations": { "time": "concat", "group": "concat" } },
                { "id": "cpu.used.percent", "aggregations": { "time": "timeAvg", "group": "avg" } }
            ]
filter =    None                        # or None
start =     -600                        # start timestamp, or lower than 0 for "last X seconds"
end =       0                           # end timestamp, or 0 for "last X seconds"
sampling =  60                          # sampling time in seconds for time series, or 0 for aggregated data

#
# Load data
#
res = sdclient.get_data(metrics, start, end, sampling, filter = filter)

#
# Show the result
#
if res[0]:
    #
    # Read response. The JSON looks like this:
    #
    # {
    #     start: timestamp,
    #     end: timestamp,
    #     data: [
    #         {
    #             t: timestamp,
    #             d: [ value1, value2, value3, ... ]
    #         },
    #         ...
    #     ]
    # }
    #
    response = res[1]

    colLen = 25

    #
    # Print summary (what, when)
    #
    start = response['start']
    end = response['end']
    data = response['data']

    print 'Data for %s from %d to %d' % (filter if filter else 'everything', start, end)
    print ''

    #
    # Print table headers
    #
    dataToPrint = ' '.join( [ str(x['id']).ljust(colLen) if len(str(x['id'])) < colLen else str(x['id'])[:(colLen - 3)].ljust(colLen - 3) + '...' for x in metrics  ] )
    print '%s %s' % ('timestamp'.ljust(colLen), dataToPrint) if sampling > 0 else dataToPrint
    print ''

    #
    # Print table body
    #
    for d in data:
        timestamp = d['t'] if sampling > 0 else start
        values = d['d']

        dataToPrint = ' '.join( [ str(x).ljust(colLen) if len(str(x)) < colLen else str(x)[:(colLen - 3)].ljust(colLen - 3) + '...' for x in values  ] )

        print '%s %s' % ( ('<t: %d>' % (timestamp)).ljust(colLen), dataToPrint ) if sampling > 0 else dataToPrint

else:
    print res[1]
    sys.exit(1)
