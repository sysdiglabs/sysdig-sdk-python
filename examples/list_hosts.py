#!/usr/bin/env python
#
# This script shows how to leverage sysdig's data query API to obtain the list
# of the instrumented hosts that have been seen in the last 5 minutes.
# Updated 1/24/2019 - Dale J. Rodriguez
# This script will also show the container count in addition to the hostnames in a from like this: host.name 12
# Where 12 is the container count and host.name is the host
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
    print 'usage: %s [-j|--json] [-d|--duration <secs>] <sysdig-token>' % sys.argv[0]
    print '-d|--duration: List hosts seen in the last <secs> seconds'
    print '-j|--json: Print output as json'
    print 'You can find your token at https://app.sysdigcloud.com/#/settings/user'
    sys.exit(1)
try:
    opts, args = getopt.getopt(sys.argv[1:],"jd:",["json", "duration="])
except getopt.GetoptError:
    usage()
duration = 3600
print_json = False
for opt, arg in opts:
    if opt in ("-d", "--duration"):
        duration = int(arg)
    elif opt in ("-j", "--json"):
        print_json = True
sdc_token = args[0]
#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)
metrics = [{"id": "host.hostName"}, {"id": "container.count","aggregations":{"time":"avg","group":"avg"}}]
res = sdclient.get_data(
    metrics, -duration, 0, duration, paging={
        "from": 0,
        "to": 999
    })
if res[0]:
    output = []
    data = res[1]['data']
    for i in range(0, len(data)):
        sample = data[i]
        metrics = sample['d']
        hostName = metrics[0]
        count = metrics[1]
        output.append('%s\t%d' % (hostName, count))
    print '\n'.join(output)
else:
    print res[1]
    sys.exit(1)
