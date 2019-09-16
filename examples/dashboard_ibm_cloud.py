#!/usr/bin/env python

# This example uses IBM Cloud IAM authentication and makes a few calls to the
# Dashboard API as validation. Creates, edits and then deletes a dashboard.

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import IbmAuthHelper, SdMonitorClient

# Parse arguments.
def usage():
    print('usage: %s <endpoint-url> <apikey> <instance-guid>' % sys.argv[0])
    print('endpoint-url: The endpoint URL that should point to IBM Cloud')
    print('apikey: IBM Cloud IAM apikey that will be used to retrieve an access token')
    print('instance-guid: GUID of an IBM Cloud Monitoring with Sysdig instance')
    sys.exit(1)

if len(sys.argv) != 4:
    usage()

URL = sys.argv[1]
APIKEY = sys.argv[2]
GUID = sys.argv[3]
DASHBOARD_NAME = 'IBM Cloud IAM with Python Client Example'
PANEL_NAME = 'CPU Over Time'

# Instantiate the client with an IBM Cloud auth object
ibm_headers = IbmAuthHelper.get_headers(URL, APIKEY, GUID)
sdclient = SdMonitorClient(sdc_url=URL, custom_headers=ibm_headers)

# Create an empty dashboard
ok, res = sdclient.create_dashboard(DASHBOARD_NAME)

# Check the result
dashboard_configuration = None
if ok:
    print('Dashboard %d created successfully' % res['dashboard']['id'])
    dashboard_configuration = res['dashboard']
else:
    print(res)
    sys.exit(1)

# Add a time series panel
panel_type = 'timeSeries'
metrics = [
    {'id': 'proc.name'},
    {'id': 'cpu.used.percent', 'aggregations': {'time': 'avg', 'group': 'avg'}}
]
ok, res = sdclient.add_dashboard_panel(
    dashboard_configuration, PANEL_NAME, panel_type, metrics)

# Check the result
if ok:
    print('Panel added successfully')
    dashboard_configuration = res['dashboard']
else:
    print(res)
    sys.exit(1)

# Remove the time series panel
ok, res = sdclient.remove_dashboard_panel(dashboard_configuration, PANEL_NAME)

# Check the result
if ok:
    print('Panel removed successfully')
    dashboard_configuration = res['dashboard']
else:
    print(res)
    sys.exit(1)

# Delete the dashboard
ok, res = sdclient.delete_dashboard(dashboard_configuration)

# Check the result
if ok:
    print('Dashboard deleted successfully')
else:
    print(res)
    sys.exit(1)

print('IBM Cloud IAM auth worked successfully!')
