#!/usr/bin/env python
#
# This script shows how to leverage Sysdig data query API to obtain the list of the instrumented
# hosts that have been seen in your infrastructure.
# The output will show the container count (`container.count` metric) in addition to the
# hostnames (`host.hostName` tag) in a format like this:
#
# host-1    12
# host-2     4
#
# where the first column is the hostname and the second column is the number of containers running
# in each host.
#
import getopt
import json
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient

#
# Parse arguments
#
def usage():
    print 'usage: %s [-j|--json] [-d|--duration <secs>] [-c|--count <number>] <sysdig-token>' % sys.argv[0]
    print '-d|--duration: List hosts seen in the last <secs> seconds (default: 3600, ie. last hour)'
    print '-c|--count: Number of hosts to print (default: 100)'
    print '-j|--json: Print output as json'
    print 'You can find your token at https://app.sysdigcloud.com/#/settings/user'
    sys.exit(1)
try:
    opts, args = getopt.getopt(sys.argv[1:],"jd:c:",["json", "duration=", "count="])
except getopt.GetoptError:
    usage()

duration = 3600
count = 100
print_json = False
for opt, arg in opts:
    print opt
    print arg
    if opt in ("-d", "--duration"):
        duration = int(arg)
    elif opt in ("-c", "--count"):
        count = int(arg)
    elif opt in ("-j", "--json"):
        print_json = True
sdc_token = args[0]

# Instantiate the SDC client
sdclient = SdcClient(sdc_token)

#
# Prepare the query's metrics list.
# In this case, we have one tag (used for segmentation) and one metric:
# - host.hostName. This is a tag, to identify each item of the output
# - container.count: This is the metric
#
metrics = [
    { "id": "host.hostName" },
    { "id": "container.count", "aggregations": { "time": "avg", "group": "avg" } }
]

res = sdclient.get_data(
    metrics,  # list of metrics
    -duration,  # start time: either a unix timestamp, or a difference from "now"
    0,  # end time: either a unix timestamp, or a difference from "now" (0 means you need "last X seconds")
    duration,  # sampling time, ie. data granularity;
               # if equal to the time window span then the result will contain a single sample
    paging = {
        "from": 0,
        "to": count - 1
    })

if res[0]:
    # data fetched successfully
    if print_json:
        print json.dumps(res[1])
    else:
        data = res[1]['data']
        output = []
        for i in range(0, len(data)):
            sample = data[i]
            metrics = sample['d']
            hostName = metrics[0]
            count = metrics[1]
            output.append('%s\t%d' % (hostName, count))

        print '\n'.join(output)
else:
    # data fetch failed
    print res[1]
    sys.exit(1)
