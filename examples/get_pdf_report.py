#!/usr/bin/env python
#
# Get a specific policy
#

import sys

from sdcclient import SdScanningClient


def usage():
    print(("usage: %s <sysdig-token> <image> <output_pdf>" % sys.argv[0]))
    print("You can find your token at https://secure.sysdig.com/#/settings/user")
    sys.exit(1)


#
# Parse arguments
#
if len(sys.argv) != 4:
    usage()

sdc_token = sys.argv[1]
image = sys.argv[2]
pdf_path = sys.argv[3]

#
# Instantiate the SDC client
#
sdclient = SdScanningClient(sdc_token, "https://secure.sysdig.com")

ok, res = sdclient.get_pdf_report(image)

#
# Return the result
#
if ok:
    with open(pdf_path, "wb") as f:
        f.write(res)
    print(("PDF %s saved" % pdf_path))
else:
    print(res)
    sys.exit(1)
