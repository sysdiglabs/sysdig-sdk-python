#!/usr/bin/env python
#
# Get a specific policy
#

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdScanningClient


def usage():
    print('usage: %s <sysdig-token> <image_id> <full_tag_name>' % sys.argv[0])
    print('You can find your token at https://secure.sysdig.com/#/settings/user')
    sys.exit(1)


#
# Parse arguments
#
if len(sys.argv) != 4:
    usage()

sdc_token = sys.argv[1]
image_id = sys.argv[2]
full_tag_name = sys.argv[3]

#
# Instantiate the SDC client
#
sdclient = SdScanningClient(sdc_token, 'https://secure.sysdig.com')

ok, res = sdclient.get_image_scan_result_by_id(image_id, full_tag_name)

#
# Return the result
#
if ok:
    print("Image Scan Result %s" % res)
else:
    print(res)
    sys.exit(1)
