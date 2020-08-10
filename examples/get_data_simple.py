#!/usr/bin/env python
#
# This script shows the basics of getting data out of Sysdig Monitor by creating a
# very simple request that has no filter and no segmentation.
#
# The request queries for the average CPU across all of the instrumented hosts for
# the last 10 minutes, with 1 minute data granularity
#

import sys

from sdcclient import SdcClient

#
# Parse arguments
#
if len(sys.argv) != 2:
    print(('usage: %s <sysdig-token>' % sys.argv[0]))
    print('You can find your token at https://app.sysdigcloud.com/#/settings/user')
    sys.exit(1)

sdc_token = sys.argv[1]

sdclient = SdcClient(sdc_token)

#
# List of metrics to export. Imagine a SQL data table, with key columns and value columns
# You just need to specify the ID for keys, and ID with aggregation for values.
#
metrics = [
    # {"id": "container.id"},
    # {"id": "agent.tag.env", "aggregations": {"time": "concat", "group": "concat"}},
    {"id": "cpu.used.percent", "aggregations": {"time": "timeAvg", "group": "avg"}}
]

#
# Data filter or None if you want to see "everything"
#
filter = None

#
# Time window:
#   - for "from A to B": start is equal to A, end is equal to B (expressed in seconds)
#   - for "last X seconds": start is equal to -X, end is equal to 0
#
start = -600
end = 0

#
# Sampling time:
#   - for time series: sampling is equal to the "width" of each data point (expressed in seconds)
#   - for aggregated data (similar to bar charts, pie charts, tables, etc.): sampling is equal to 0
#
sampling = 60

#
# Load data
#
ok, res = sdclient.get_data(metrics, start, end, sampling, filter=filter)

#
# Show the result
#
if ok:
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
    colLen = 25

    #
    # Print summary (what, when)
    #
    start = res['start']
    end = res['end']
    data = res['data']

    print(('Data for %s from %d to %d' % (filter if filter else 'everything', start, end)))
    print('')

    #
    # Print table headers
    #
    dataToPrint = ' '.join([str(x['id']).ljust(colLen) if len(str(x['id'])) < colLen else str(x['id'])[
                                                                                          :(colLen - 3)].ljust(
        colLen - 3) + '...' for x in metrics])
    print(('%s %s' % ('timestamp'.ljust(colLen), dataToPrint) if sampling > 0 else dataToPrint))
    print('')

    #
    # Print table body
    #
    for d in data:
        timestamp = d['t'] if sampling > 0 else start
        values = d['d']

        dataToPrint = ' '.join(
            [str(x).ljust(colLen) if len(str(x)) < colLen else str(x)[:(colLen - 3)].ljust(colLen - 3) + '...' for x in
             values])

        print(('%s %s' % (('<t: %d>' % (timestamp)).ljust(colLen), dataToPrint) if sampling > 0 else dataToPrint))

else:
    print(res)
    sys.exit(1)
