#!/usr/bin/env python
#
# Post a user event to Sysdig Cloud
#

import os
import sys
import json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient

#
# Parse arguments
#
if len(sys.argv) < 3:
    print 'usage: %s <sysdig-token> <name> [description] [severity] [scope] [tags]' % sys.argv[0]
    print ' sysdig-token: You can find your token at https://app.sysdigcloud.com/#/settings/user'
    print ' severity: syslog style (from 0 to 7)'
    print ' scope: Sysdig Cloud format metadata to associate with the event, eg: \'host.hostName = "ip-10-1-1-1" and container.name = "foo"\''
    print ' tags: dictionary of key-value pairs, eg: \'{"app":"my_app", "file":"text.py"}\''
    sys.exit(1)

sdc_token = sys.argv[1]
name = sys.argv[2]

description = ''
if len(sys.argv) > 3:
    description = sys.argv[3]
#    print description

severity = 6
if len(sys.argv) > 4:
    severity = int(sys.argv[4])
#    print severity

scope = ''
if len(sys.argv) > 5:
    scope = sys.argv[5] 
#    scope = "'host.hostName = 'ip-10-1-1-1'"
#    print scope

tags = {}
if len(sys.argv) > 6:
    tags = json.loads(sys.argv[6])
#    print json.dumps(tags)
    
#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)

#
# Post the event using post_event(self, name, description=None, severity=6, event_filter=None, tags=None)
#
res = sdclient.post_event(name, description, severity, scope, tags)

#
# Return the result
#
if res[0]:
    print 'Event Posted Successfully'
else:
    print res[1]
    sys.exit(1)
