#!/usr/bin/env python
#
# Save/restore dashboards
#

import os
import sys
import zipfile
import json
import shutil
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

def cleanup_dir(path):
    if os.path.exists(path) == False:
        return
    if os.path.isdir(path) == False:
        print('Provided path is not a directory')
        sys.exit(1)

    shutil.rmtree(path)

#
# Parse arguments
#
if len(sys.argv) != 3:
    print('usage: %s <sysdig-token> <file-name>' % sys.argv[0])
    print('You can find your token at https://app.sysdigcloud.com/#/settings/user')
    sys.exit(1)

sdc_token = sys.argv[1]
dashboard_state_file = sys.argv[2]
sysdig_dashboard_dir = 'sysdig-dashboard-dir'

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)

#
# Fire the request.
#
res = sdclient.get_dashboards()

#
# Show the list of dashboards
#
if res[0]:
    data = res[1]
else:
    print(res[1])
    sys.exit(1)

# Clean up any state in the directory
cleanup_dir(sysdig_dashboard_dir)

try:
    # Creating sysdig dashboard directory to store dashboards
    if not os.path.exists(sysdig_dashboard_dir):
        os.makedirs(sysdig_dashboard_dir)


    for db in data['dashboards']:
        file_path = os.path.join(sysdig_dashboard_dir, str(db['id']))
        with open(file_path, 'wb') as f:
            f.write(json.dumps(db))
        print("Dashboard name: %s, # Charts: %d" % (db['name'], len(db['items'])))


    zipf = zipfile.ZipFile(dashboard_state_file, 'w', zipfile.ZIP_DEFLATED, allowZip64=True)
    zipdir(sysdig_dashboard_dir, zipf)
    zipf.close()

    print("Finished writing dashboard data in zip format to %s" % dashboard_state_file)
finally:
    # Clean up any state in the directory
    cleanup_dir(sysdig_dashboard_dir)
