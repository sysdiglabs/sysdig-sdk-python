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
    print ' severity: syslog style from 0 (high) to 7 (low)'
    print ' scope: metadata, in Sysdig Cloud format, of nodes to associate with the event, eg: \'host.hostName = "ip-10-1-1-1" and container.name = "foo"\''
    print ' tags: dictionary of arbitrary key-value pairs, eg: \'{"app":"my_app", "file":"text.py"}\''
    sys.exit(1)

sdc_token = sys.argv[1]
name = sys.argv[2]
kwargs = {}

if len(sys.argv) > 3:
    kwargs['description'] = sys.argv[3]

if len(sys.argv) > 4:
    kwargs['severity'] = int(sys.argv[4])

if len(sys.argv) > 5:
    kwargs['event_filter'] = sys.argv[5] 

if len(sys.argv) > 6:
    kwargs['tags'] = json.loads(sys.argv[6])
    
#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)

#
# Post the event using post_event(self, name, description=None, severity=None, event_filter=None, tags=None)
#
res = sdclient.post_event(name, **kwargs)

#
# Return the result
#
if res[0]:
    print 'Event Posted Successfully'
else:
    print res[1]
    sys.exit(1)
