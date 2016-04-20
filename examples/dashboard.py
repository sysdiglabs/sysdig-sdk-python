#!/usr/bin/env python
#
# TODO Description
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

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)


#
# Create an empty dashboard
#
dashboard_name = 'My Dashboard'
dashboard_configuration = None
res = sdclient.create_dashboard(dashboard_name)

# Check the result
if res[0]:
    print 'Dashboard %d created successfully' % res[1]['dashboard']['id']
    dashboard_configuration = res[1]['dashboard']
else:
    print res[1]
    sys.exit(1)


#
# Find a dashboard by name
#
res = sdclient.find_dashboard_by(dashboard_name)

# Check the result
if res[0] and len(res[1]) > 0:
    print 'Dashboard found'
    dashboard_configuration = res[1][0]['dashboard']
else:
    print res[1]
    sys.exit(1)


#
# Add a time series
#
panel_name = 'CPU Over Time'
panel_type = 'timeSeries'
metrics = [
  { 'id': 'kubernetes.pod.name' },
  { 'id': 'cpu.used.percent', 'aggregations': { 'time': 'avg', 'group': 'avg' } }
]
scope = 'kubernetes.namespace.name = "dev" and kubernetes.replicationController.name = "cassandra"'
res = sdclient.add_dashboard_panel(dashboard_configuration, panel_name, panel_type, metrics, scope=scope)

# Check the result
if res[0]:
    print 'Panel added successfully'
    dashboard_configuration = res[1]['dashboard']
else:
    print res[1]
    sys.exit(1)


#
# Add a top bar chart
#
panel_name = 'CPU by host'
panel_type = 'top'
metrics = [
  { 'id': 'host.hostName' },
  { 'id': 'cpu.used.percent', 'aggregations': { 'time': 'avg', 'group': 'avg' } }
]
sort_by = { 'metric': 'cpu.used.percent', 'mode': 'desc' }
paging = { 'from': 0, 'to': 10 }
res = sdclient.add_dashboard_panel(dashboard_configuration, panel_name, panel_type, metrics, sort_by=sort_by, paging=paging)

# Check the result
if res[0]:
    print 'Panel added successfully'
    dashboard_configuration = res[1]['dashboard']
else:
    print res[1]
    sys.exit(1)


#
# Add a number panel
#
panel_name = 'CPU'
panel_type = 'number'
metrics = [
  { 'id': 'cpu.used.percent', 'aggregations': { 'time': 'avg', 'group': 'avg' } }
]
layout = { 'col': 6, 'row': 1, 'size_x': 2, 'size_y': 3 }
res = sdclient.add_dashboard_panel(dashboard_configuration, panel_name, panel_type, metrics, layout=layout)

# Check the result
if res[0]:
    print 'Panel added successfully'
    dashboard_configuration = res[1]['dashboard']
else:
    print res[1]
    sys.exit(1)


#
# Remove a panel
#
res = sdclient.remove_dashboard_panel(dashboard_configuration, 'CPU')

# Check the result
if res[0]:
    print 'Panel removed successfully'
    dashboard_configuration = res[1]['dashboard']
else:
    print res[1]
    sys.exit(1)


#
# Delete the dashboard
#
res = sdclient.delete_dashboard(dashboard_configuration)

# Check the result
if res[0]:
    print 'Dashboard deleted successfully'
else:
    print res[1]
    sys.exit(1)