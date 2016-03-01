#!/usr/bin/env python
import sys
sys.path.insert(0, '../')
from sdcclient import SdcClient

#
# Parse arguments
#
if len(sys.argv) < 4:
    print 'usage: %s <sysdig-token> name description [severity]' % sys.argv[1]
    sys.exit(0)

sdc_token = sys.argv[1]
name = sys.argv[2]
description = sys.argv[3]

severity = 6
if len(sys.argv) < 4:
	severity = int(sys.argv[4])

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token, 'https://app-staging2.sysdigcloud.com')

#
# Post the event
#
res = sdclient.post_event(name, description, severity)

#
# Return the result
#
if res[0]:
	print 'Event Posted Successfully'
else:
	print res[1]