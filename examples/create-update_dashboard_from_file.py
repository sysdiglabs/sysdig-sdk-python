#!/usr/bin/env python
#
# Example of dashboard update from a json file, if it doesn't exist a new dashboard is created
#

import os
import sys
import zipfile
import json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdMonitorClient

#
# Parse arguments
#
if len(sys.argv) != 3:
  print('usage: %s <sysdig-token> <file-name>' % sys.argv[0])
  print('You can find your token at https://app.sysdigcloud.com/#/settings/user')
  sys.exit(1)

sdc_token = sys.argv[1]
dashboard_state_file = sys.argv[2]

#
# Instantiate the SDC client
#
sdclient = SdMonitorClient(sdc_token)

with open(dashboard_state_file) as data_file:
  loaded_object = json.load(data_file)

if 'dashboard' not in loaded_object:
  loaded_object = {
      'version': 'v1',
      'dashboard': loaded_object
  }

dashboard = loaded_object['dashboard']

#
# Find a dashboard by id
#
ok, res = sdclient.get_dashboard(dashboard['id'])

# Check the result
if ok and len(res) > 0:
  print('Dashboard Exists, updating')

  current = res[0]['dashboard']

  # The API will validate the new dashboard configuration against the existing one. These means that the new configuration must retain some of the properties from the existing one:
  # 1. ID: The dashboard ID must be the same
  # 2. The API protects resources against unexpected overwrites: Only the client that tries to update the latest version of the resource will be allowed to do so; Clients trying to update older versions won't succeed (HTTP 409 error). Since the dashboard is being read by file, you must first make sure that the API will assume the new dashboard to update the latest version: To do so, `version` should be read from the latest dashboard configuration
  # 3. To avoid sensitive data to be exchanged with the API, remove user-related properties such as userId, username, teamId, customerId, publicToken

  for key in ['id', 'version', 'userId', 'username' 'teamId', 'customerId', 'publicToken']:
    if key in current:
      dashboard[key] = current[key]
  
  # Then, you can update the dashboard
  ok, res = sdclient.update_dashboard(dashboard)

  if ok:
    print('Updated Dashboard id: ' + dashboard['id'] + 'named: ' + dashboard['name'])
  else:
    print("Dashboard update failed for dashboard id %s with error %s" % (dashboard['id'], res))
    sys.exit(1)
else:
  print('Creating Dashboard')
  ok, res = sdclient.create_dashboard_with_configuration(dashboard)
  if ok:
    print('Restored Dashboard id: ' + dashboard['id'] + 'named: ' + dashboard['name'])
  else:
    print("Dashboard creation failed for dashboard name %s with error %s" % (dashboard['id'], res))
    sys.exit(1)
