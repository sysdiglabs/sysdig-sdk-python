#!/usr/bin/env python
#
# Restore Alerts of the format in a JSON dumpfile from the list_alerts.py example.
#

import os
import sys
import json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient

#
# Parse arguments
#
if len(sys.argv) != 3:
    print 'usage: %s <sysdig-token> <file-name>' % sys.argv[0]
    print 'You can find your token at https://app.sysdigcloud.com/#/settings/user'
    sys.exit(1)

sdc_token = sys.argv[1]
alerts_dump_file = sys.argv[2]

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)

with open(alerts_dump_file, 'r') as f:
    j = json.load(f)
    for a in j['alerts']:
        a['description'] += ' (created via restore_alerts.py)'
        res = sdclient.create_alert(alert_obj=a)
        if not res[0]:
            print res[1]
            sys.exit(1)

print 'All Alerts in ' + alerts_dump_file + ' created successfully.'
