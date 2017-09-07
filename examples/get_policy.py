#!/usr/bin/env python
#
# Get a specific policy
#

import os
import sys
import json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdSecureClient

def usage():
    print 'usage: %s <sysdig-token> <policy name>' % sys.argv[0]
    print 'You can find your token at https://secure.sysdig.com/#/settings/user'
    sys.exit(1)

#
# Parse arguments
#
if len(sys.argv) != 3:
    usage()

sdc_token = sys.argv[1]
name = sys.argv[2]

#
# Instantiate the SDC client
#
sdclient = SdSecureClient(sdc_token, 'https://secure.sysdig.com')

res = sdclient.get_policy(name)

#
# Return the result
#
if res[0]:
    print json.dumps(res[1], indent=2)
else:
    print res[1]
    sys.exit(1)


