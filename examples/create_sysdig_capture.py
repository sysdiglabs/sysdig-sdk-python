#!/usr/bin/env python
#
# Creates a sysdig capture, waits for termination and prints the download URL.
#

import os
import sys
import time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient

#
# Parse arguments
#
if len(sys.argv) not in (5, 6):
    print 'usage: %s <sysdig-token> hostname capture_name duration [filter]' % sys.argv[0]
    print 'You can find your token at https://app.sysdigcloud.com/#/settings/user'
    sys.exit(1)

sdc_token = sys.argv[1]
hostname = sys.argv[2]
capture_name = sys.argv[3]
duration = sys.argv[4]
capture_filter = ''

if len(sys.argv) == 6:
    capture_filter = sys.argv[5]

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)

res = sdclient.create_sysdig_capture(hostname, capture_name, int(duration), capture_filter)

#
# Show the list of metrics
#
if res[0]:
    capture = res[1]
else:
    print res[1]
    sys.exit(1)

while True:
    res = sdclient.poll_sysdig_capture(capture)
    if res[0]:
        capture = res[1]
    else:
        print res[1]
        sys.exit(1)

    print 'Capture is in state ' + capture['status']
    if capture['status'] in ('requested', 'capturing', 'uploading'):
        pass
    elif capture['status'] in ('error', 'uploadingError'):
        sys.exit(1)
    elif capture['status'] in ('done', 'uploaded'):
        print 'Download at: ' + sdclient.url + capture['downloadURL']
        sys.exit(0)

    time.sleep(1)
