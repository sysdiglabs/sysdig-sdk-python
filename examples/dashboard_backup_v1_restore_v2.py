#!/usr/bin/env python
#
# Save the first user dashboard to file and then use create_dashboard_from_file()
# to apply the stored dasboard again with a different filter.
#
import os
import sys
import json
sys.path.insert(
    0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdMonitorClient
from sdcclient import SdMonitorClientV1

#
# Parse arguments
#
if len(sys.argv) != 5:
    print(
        'usage: %s <sysdig-v1-url> <sysdig-v1-token> <sysdig-v2-url> <sysdig-v2-token>'
        % sys.argv[0])
    print(
        'You can find your token at https://app.sysdigcloud.com/#/settings/user'
    )
    sys.exit(1)

sdc_v1_url = sys.argv[1]
sdc_v1_token = sys.argv[2]
sdc_v2_url = sys.argv[3]
sdc_v2_token = sys.argv[4]

#
# Instantiate the SDC client
#
sdclient_v2 = SdMonitorClient(sdc_v2_token, sdc_url=sdc_v2_url)
sdclient_v1 = SdMonitorClientV1(sdc_v1_token, sdc_url=sdc_v1_url)

#
# Serialize the first user dashboard to disk
#
ok, res = sdclient_v1.get_dashboards()

if not ok:
    print(res)
    sys.exit(1)

for dashboard in res['dashboards']:
    file_name = '{}.json'.format(dashboard['id'])
    print('Saving v1 dashboard {} to file {}...'.format(
        dashboard['name'], file_name))
    sdclient_v1.save_dashboard_to_file(dashboard, file_name)

    print('Importing dashboard to v2...')
    ok, res = sdclient_v2.create_dashboard_from_file(
        u'import of {}'.format(dashboard['name']),
        file_name,
        None,
        shared=dashboard['isShared'],
        public=dashboard['isPublic'])

    if ok:
        print('Dashboard {} imported!'.format(dashboard['name']))
        sdclient_v2.delete_dashboard(res['dashboard'])
    else:
        print('Dashboard {} import failed:'.format(dashboard['name']))
        print(res)

    print('\n')
