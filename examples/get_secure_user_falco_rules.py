#!/usr/bin/env python
#
# Get the sysdig secure user rules file.
#

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdSecureClient

#
# Parse arguments
#
if len(sys.argv) != 2:
    print(('usage: %s <sysdig-token>' % sys.argv[0]))
    print('You can find your token at https://secure.sysdig.com/#/settings/user')
    sys.exit(1)

sdc_token = sys.argv[1]

#
# Instantiate the SDC client
#
sdclient = SdSecureClient(sdc_token, 'https://secure.sysdig.com')

#
# Get the configuration
#
ok, res = sdclient.get_user_falco_rules()

#
# Return the result
#
if ok:
    sys.stdout.write(res["userRulesFile"]["content"])
else:
    print(res)
    sys.exit(1)
