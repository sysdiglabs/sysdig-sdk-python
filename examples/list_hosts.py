#!/usr/bin/env python
#
# This script shows how to leverage sysdig's data query API to obtain the list
# of the instrumented hosts that have been seen in the last 5 minutes.
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

duration = 600
print_json = False
for opt, arg in opts:
    if opt in ("-d", "--duration"):
        duration = int(arg)
    elif opt in ("-j", "--json"):
        print_json = True

if len(args) != 1:
    usage()

sdc_token = args[0]

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)

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
                        -duration,   # cover the last duration seconds...
                        0,      # ... ending now...
                        duration)    # ... with just one durations sample

#
# Show the results!
#
if res[0]:
    data = res[1]
else:
    print res[1]
    sys.exit(1)

if print_json:
    print json.dumps(data)
else:
    print data
