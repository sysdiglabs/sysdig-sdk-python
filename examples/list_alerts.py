#!/usr/bin/env python
#
# Print 'enabled' flag and name for all of the alerts created by the user
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
# Fire the request.
#
res = sdclient.get_alerts()

#
# Show the list of alerts
#
if res[0]:
    data = res[1]
else:
    print res[1]
    sys.exit(1)

for alert in data['alerts']:
    print 'enabled: %s, name: %s' % (str(alert['enabled']), alert['name'])
