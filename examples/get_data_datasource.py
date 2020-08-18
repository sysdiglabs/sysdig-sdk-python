#!/usr/bin/env python
#
# This script shows the use of the datasource_type argument in the get_data request,
# by providing a few clarifying examples
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
ok, res = sdclient.get_data(req,  # metrics list
                            -600,  # start_ts = 600 seconds ago
                            0)  # end_ts = now

if ok:
    data = res
else:
    print(res)
    sys.exit(1)

print("\n\nCPU by host:")
print(data)

#
# Second example: CPU by container name
# datasource_type is not necessary since it's infered from the grouping key container.name
#
req = [{"id": "container.name"}]
req.extend(cpu_metric)
ok, res = sdclient.get_data(req,  # metrics list
                            -600,  # start_ts = 600 seconds ago
                            0)  # end_ts = now

if ok:
    data = res
else:
    print(res)
    sys.exit(1)

print("\n\nCPU by container:")
print(data)

#
# Third example: CPU average across all hosts
# datasource_type is set to host since no grouping keys or filters are specified (default would be host anyway)
#
ok, res = sdclient.get_data(cpu_metric,  # metrics list
                            -600,  # start_ts = 600 seconds ago
                            0,  # end_ts = now
                            datasource_type='host')  # ask data from hosts

if ok:
    data = res
else:
    print(res)
    sys.exit(1)

print("\n\nAverage CPU across all the hosts in the infrastructure:")
print(data)

#
# Third example: CPU average across all containers
# datasource_type is set to container since no grouping keys or filters are specified (ovverrides the host default)
#
ok, res = sdclient.get_data(cpu_metric,  # metrics list
                            -600,  # start_ts = 600 seconds ago
                            0,  # end_ts = now
                            datasource_type='container')  # ask data from containers

if ok:
    data = res
else:
    print(res)
    sys.exit(1)

print("\n\nAverage CPU across all the containers in the infrastructure:")
print(data)
