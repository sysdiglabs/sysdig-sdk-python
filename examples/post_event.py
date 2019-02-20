#!/usr/bin/env python
#
# Post a user event to Sysdig Cloud
#

import os
import sys
import json
import argparse
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient

#
# Parse arguments
#
# Usage: post_event.py [-h] [-d DESCRIPTION] [-s SEVERITY] [-c SCOPE] [-t TAGS] sysdig_token name
#
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--description')
parser.add_argument('-s', '--severity', help='syslog style from 0 (high) to 7 (low)')
parser.add_argument('-c', '--scope', help='metadata, in Sysdig Cloud format, of nodes to associate with the event, eg: \'host.hostName = "ip-10-1-1-1" and container.name = "foo"\'')
parser.add_argument('-t', '--tags', help='dictionary of arbitrary key-value pairs, eg: \'{"app":"my_app", "file":"text.py"}\'')
parser.add_argument('sysdig_token', help='You can find your token at https://app.sysdigcloud.com/#/settings/user')
parser.add_argument('name')
args = parser.parse_args()

tags = None
if args.tags:
    tags = json.loads(args.tags)

#
# Instantiate the SDC client
#
sdclient = SdcClient(args.sysdig_token)

#
# Post the event using post_event(self, name, description=None, severity=None, event_filter=None, tags=None)
#
ok, res = sdclient.post_event(args.name, args.description, args.severity, args.scope, tags)

#
# Return the result
#
if ok:
    print('Event Posted Successfully')
else:
    print(res)
    sys.exit(1)
