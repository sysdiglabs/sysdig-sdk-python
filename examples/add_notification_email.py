#!/usr/bin/env python
#
# Post a user event to Sysdig Cloud
#

import sys
sys.path.insert(0, '../')
from sdcclient import SdcClient

#
# Parse arguments
#
if len(sys.argv) != 3:
    print 'usage: %s <sysdig-token> email' % sys.argv[0]
    print 'You can find your token at https://app.sysdigcloud.com/#/settings/user'
    sys.exit(0)

sdc_token = sys.argv[1]
email = sys.argv[2]

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)

#
# Post the event
#
res = sdclient.add_email_notification_recipient(email)

#
# Return the result
#
if res[0]:
    print 'Recipient added successfully'
else:
    print res[1]
