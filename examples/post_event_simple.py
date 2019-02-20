#!/usr/bin/env python
#
# Post a user event to Sysdig Cloud
#

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient

#
# Parse arguments
#
if len(sys.argv) < 4:
    print('usage: %s <sysdig-token> name description [severity]' % sys.argv[0])
    print('You can find your token at https://app.sysdigcloud.com/#/settings/user')
    sys.exit(1)

sdc_token = sys.argv[1]
name = sys.argv[2]
description = sys.argv[3]

scope = 'host.hostName = "foo" and container.name = "bar"'
tags = {"tag1": "value1"}

severity = 6
if len(sys.argv) < 4:
    severity = int(sys.argv[4])

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)

#
# Post the event
#
ok, res = sdclient.post_event(name, description, severity, scope, tags)

#
# Return the result
#
if ok:
    print('Event Posted Successfully')
else:
    print(res)
    sys.exit(1)
