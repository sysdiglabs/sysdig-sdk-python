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
    print 'You can find your token at https://app.sysdigcloud.com/#/settings/user'
    sys.exit(0)

sdc_token = sys.argv[1]

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)

cpu_metric = [
    {"id": "cpu.used.percent",
     "aggregations": {
         "time": "avg",
         "group": "avg"
     }
    }]

#
# First example: CPU by host name
# datasource_type is not necessary since it's infered from the grouping key host.hostName
#
req = [{"id": "host.hostName"}]
req.extend(cpu_metric)
res = sdclient.get_data(req, # metrics list
                        -600,    # start_ts = 600 seconds ago
                        0)       # end_ts = now

if res[0]:
    data = res[1]
else:
    print res[1]
    sys.exit(0)

print "\n\nCPU by host:"
print data

#
# Second example: CPU by container name
# datasource_type is not necessary since it's infered from the grouping key container.name
#
req = [{"id": "container.name"}]
req.extend(cpu_metric)
res = sdclient.get_data(req, # metrics list
                        -600,    # start_ts = 600 seconds ago
                        0)       # end_ts = now

if res[0]:
    data = res[1]
else:
    print res[1]
    sys.exit(0)

print "\n\nCPU by container:"
print data

#
# Third example: CPU average across all hosts
# datasource_type is set to host since no grouping keys or filters are specified (default would be host anyway)
#
res = sdclient.get_data(cpu_metric, # metrics list
                        -600,    # start_ts = 600 seconds ago
                        0,       # end_ts = now
                        datasource_type='host') # ask data from hosts      

if res[0]:
    data = res[1]
else:
    print res[1]
    sys.exit(0)

print "\n\nAverage CPU across all the hosts in the infrastructure:"
print data

#
# Third example: CPU average across all containers
# datasource_type is set to container since no grouping keys or filters are specified (ovverrides the host default)
#
res = sdclient.get_data(cpu_metric, # metrics list
                        -600,    # start_ts = 600 seconds ago
                        0,       # end_ts = now
                        datasource_type='container') # ask data from containers

if res[0]:
    data = res[1]
else:
    print res[1]
    sys.exit(0)

print "\n\nAverage CPU across all the containers in the infrastructure:"
print data
