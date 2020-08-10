#!/usr/bin/env python
#
# Get an image scan result given image id
#

import sys

from sdcclient import SdScanningClient


def usage():
    print(('usage: %s <sysdig-token> <image_id_sha>' % sys.argv[0]))
    print('You can find your token at https://secure.sysdig.com/#/settings/user')
    sys.exit(1)


#
# Parse arguments
#
if len(sys.argv) != 3:
    usage()

sdc_token = sys.argv[1]
image_id_sha = sys.argv[2]

#
# Instantiate the SDC client
#
sdclient = SdScanningClient(sdc_token, 'https://secure.sysdig.com')

ok, res = sdclient.get_image_info_by_id(image_id_sha)

#
# Return the result
#
if ok:
    print(("Image Info %s" % res))
else:
    print(res)
    sys.exit(1)
