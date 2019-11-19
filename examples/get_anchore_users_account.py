#!/usr/bin/env python
#
# Get a specific anchore user account
#

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdScanningClient


def usage():
    print('usage: %s <sysdig-token>' % sys.argv[0])
    print('You can find your token at https://secure.sysdig.com/#/settings/user')
    sys.exit(1)


#
# Parse arguments
#
if len(sys.argv) != 2:
    usage()

sdc_token = sys.argv[1]

#
# Instantiate the SDC client
#
sdclient = SdScanningClient(sdc_token, 'https://secure.sysdig.com')

ok, res = sdclient.get_anchore_users_account()

#
# Return the result
#
if ok:
    print("Anchore User Info %s" % res)
else:
    print(res)
    sys.exit(1)
