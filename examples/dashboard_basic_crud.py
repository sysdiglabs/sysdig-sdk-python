#!/usr/bin/env python
#
# Simple example of dashboard creation, retrieval, updating, and deletion.
#

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdMonitorClient
import uuid

#
# Parse arguments
#
if len(sys.argv) != 2:
    print('usage: %s <sysdig-token>' % sys.argv[0])
    print('You can find your token at https://app.sysdigcloud.com/#/settings/user')
    sys.exit(1)

sdc_token = sys.argv[1]

#
# Instantiate the SDC client
#
sdclient = SdMonitorClient(sdc_token)

#
# Create Dashboard.
#
ok, res = sdclient.create_dashboard("Sample dashboard - " + uuid.uuid4().hex)

#
# Check for successful creation
#
if not ok:
    print(res)
    sys.exit(1)

dashboard = res['dashboard']

#
# Get Dashboard.
#
ok, res = sdclient.get_dashboard(dashboard['id'])

#
# Check for successful retrieval
#
if not ok:
    print(res)
    sys.exit(1)

dashboard = res['dashboard']

#
# Update Dashboard.
#
dashboard['widgets'] = [{
    "compareToConfig": None,
    "customDisplayOptions": {
        "histogram": {
            "numberOfBuckets": 10,
        },
        "unit": "%",
        "valueLimit": {
            "count": 10,
            "direction": "desc"
        },
        "xAxis": {
            "from": 0,
            "to": None
        },
        "yAxisLeftDomain": {
            "from": 0,
            "to": None
        },
        "yAxisRightDomain": {
            "from": 0,
            "to": None
        },
        "yAxisScale": "linear"
    },
    "gridConfiguration": {
        "col": 1,
        "row": 1,
        "size_x": 6,
        "size_y": 4
    },
    "metrics": [
        {
            "id": "timestamp",
            "propertyName": "k0"
        },
        {
            "groupAggregation": "avg",
            "id": "cpu.used.percent",
            "metricFormattingDecimals": None,
            "metricFormattingUnit": None,
            "propertyName": "v0",
            "timeAggregation": "avg"
        }
    ],
    "name": "My Panel",
    "overrideScope": False,
    "scope": None,
    "showAs": "timeSeries"
}]
ok, res = sdclient.update_dashboard(dashboard)
# NOTE: ID is optional if present in data set. Line below would also work as expected.
#       This can be leveraged to copy one dashboard to another.
# ok, res = sdclient.update_dashboard(dashboard, dashboard['id'])

#
# Check for successful update
#
if not ok:
    print(res)
    sys.exit(1)

dashboard = res['dashboard']

#
# Delete Dashboard.
#
ok, res = sdclient.delete_dashboard(dashboard)

#
# Check for successful delete
#
if not ok:
    print(res)
    sys.exit(1)

#
# Create Dashboard.
#
ok, res = sdclient.create_dashboard("Sample dashboard - " + uuid.uuid4().hex)
new_dashboard = res['dashboard']

#
# Update Dashboard with previous data.
#
dashboard['name'] = new_dashboard['name'] # dashboards belonging to the same user cannot have the same name
ok, res = sdclient.update_dashboard(dashboard, new_dashboard['id'])
new_dashboard = res['dashboard']

#
# Delete Dashboard.
#
ok, res = sdclient.delete_dashboard(new_dashboard)