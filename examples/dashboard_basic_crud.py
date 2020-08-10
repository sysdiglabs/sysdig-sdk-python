#!/usr/bin/env python
#
# Simple example of dashboard creation, retrieval, updating, and deletion.
#
import sys
import uuid

from sdcclient import SdMonitorClient

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
dashboard['name'] = "Let's change the dashboard name. " + uuid.uuid4().hex
ok, res = sdclient.update_dashboard(dashboard)

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
