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
    print 'usage: %s <sysdig-token>' % sys.argv[0]
    print 'You can find your token at https://secure.sysdig.com/#/settings/user'
    sys.exit(1)

sdc_token = sys.argv[1]

#
# Instantiate the SDC client
#
sdclient = SdSecureClient(sdc_token, 'https://secure-staging.sysdig.com')

#
# Get the configuration
#
res = sdclient.get_user_falco_rules()

#
# Return the result
#
if res[0]:
    sys.stdout.write(res[1]["userRulesFile"]["content"])
else:
    print res[1]
    sys.exit(1)
