#!/usr/bin/env python
#
# Save/restore dashboards
#

import os
import sys
import zipfile
import json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdMonitorClient


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
        sys.exit(-1)

    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            else:
                print('Cannot clean the provided directory due to delete failure on %s' % file_path)
        except Exception as e:
            print(e)
    os.rmdir(path)


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
sdclient = SdMonitorClient(sdc_token)

#
# Fire the request.
#
ok, res = sdclient.get_dashboards()

#
# Show the list of dashboards
#
if not ok:
    print(res)
    sys.exit(1)


# Clean up any state in the tmp directory
cleanup_dir(sysdig_dashboard_dir)

# Creating sysdig dashboard directory to store dashboards
if not os.path.exists(sysdig_dashboard_dir):
    os.makedirs(sysdig_dashboard_dir)


for db in res['dashboards']:
    sdclient.save_dashboard_to_file(db, os.path.join(sysdig_dashboard_dir, str(db['id'])))

    print("Name: %s, # Charts: %d" % (db['name'], len(db['widgets'])))

zipf = zipfile.ZipFile(dashboard_state_file, 'w', zipfile.ZIP_DEFLATED)
zipdir(sysdig_dashboard_dir, zipf)
zipf.close()

# Clean up any state in the directory
cleanup_dir(sysdig_dashboard_dir)
