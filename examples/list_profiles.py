#!/usr/bin/env python
#
# List the current set of image profiles.
#

import sys

from sdcclient import SdSecureClient


def usage():
    print(('usage: %s <secure-endpoint> <sysdig-token>' % sys.argv[0]))
    sys.exit(1)


#
# Check number of parameters
#
if len(sys.argv) < 2:
    usage()

sdc_endpoint = sys.argv[1]
sdc_token = sys.argv[2]

#
# Instantiate the SDC client
#
sdclient = SdSecureClient(sdc_token, sdc_endpoint)

#
# Retrieve all the image profiles
#
ok, res = sdclient.list_image_profiles()

if not ok:
    print(res)
    sys.exit(1)

# Strip the surrounding json to only keep the list of profiles
res = res['profiles']

for profile in res:
    print(("ID: {}, Name: {}".format(profile["profileId"], profile["imageName"])))
