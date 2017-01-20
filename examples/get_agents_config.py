#!/usr/bin/env python
#
# Get the sysdig cloud agents configuration as a json file and print it on the screen.
# Agents configuration settings can be managed in a centralized way through the API
# This script downloads the settings and its result can be edited and the used from
# the set_agents_config script.
#

import os
import sys
import json
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
sdclient = SdcClient(sdc_token, 'https://app-staging.sysdigcloud.com')

#
# Get the configuration
#
res = sdclient.get_agents_config()

#
# Return the result
#
if res[0]:
        print json.dumps(res[1], indent=2)
else:
    print res[1]
