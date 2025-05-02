#!/usr/bin/env python
#
# Get the sysdig cloud agents configuration as yaml and print it on the screen.
# Agents configuration settings can be managed in a centralized way through the API
# This script downloads the settings and its result can be edited and the used from
# the set_agents_config script.
#

import sys

from sdcclient import SdcClient

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
sdclient = SdcClient(sdc_token, 'https://app.sysdigcloud.com')

#
# Get the configuration
#
ok, res = sdclient.get_agents_config()

#
# Return the result
#
if ok:
    if "files" not in res or len(res["files"]) == 0:
        print("No current auto configuration")
    else:
        print("Current contents of config file:")
        print("--------------------------------")
        print((res["files"][0]["content"]))
        print("--------------------------------")
else:
    print(res)
