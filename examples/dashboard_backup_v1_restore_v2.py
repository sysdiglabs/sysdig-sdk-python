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
if len(sys.argv) != 2:
    print('usage: %s <sysdig-token>' % sys.argv[0])
    print(
        'You can find your token at https://app.sysdigcloud.com/#/settings/user'
    )
    sys.exit(1)

sdc_token = sys.argv[1]

#
# Instantiate the SDC client
#
sdclient = SdMonitorClient(sdc_token, sdc_url='https://app.sysdigcloud.com')
sdclientV1 = SdMonitorClientV1(
    sdc_token, sdc_url='https://app.sysdigcloud.com')

#
# Serialize the first user dashboard to disk
#
ok, res = sdclientV1.get_dashboards()

if not ok:
    print(res)
    sys.exit(1)

for item in res['dashboards']:
    file_name = '{}.json'.format(item['id'])
    sdclientV1.save_dashboard_to_file(item, file_name)

    ok, res = sdclient.create_dashboard_from_file(
        u'import of {}'.format(item['name']),
        file_name,
        None,
        shared=item['isShared'],
        public=item['isPublic'])

    if ok:
        sdclient.delete_dashboard(res['dashboard'])
    else:
        print('=====')
        print(res)

    print('=====')
