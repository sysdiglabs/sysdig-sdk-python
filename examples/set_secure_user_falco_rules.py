#!/usr/bin/env python
#
# Set the sysdig secure system rules file.
# This script takes a user token and a falco rules file (yaml) as input, and sets the
# system falco rules file for this customer to that file.
#

import sys

import yaml

from sdcclient import SdSecureClient

#
# Parse arguments
#
if len(sys.argv) != 3:
    print(("usage: %s <sysdig-token> <falco-rules-file>" % sys.argv[0]))
    print("You can find your token at https://app.sysdigcloud.com/#/settings/user")
    sys.exit(1)

sdc_token = sys.argv[1]

#
# Load the config file
#
with open(sys.argv[2]) as cfile:
    yaml_conf = cfile.read()
    # Verify that the content is valid yaml
    parsed_yaml_conf = yaml.safe_load(yaml_conf)

sdclient = SdSecureClient(sdc_token, "https://secure.sysdig.com")

#
# Push the configuration
#
ok, res = sdclient.set_user_falco_rules(yaml_conf)

#
# Check if everything went well
#
if ok:
    print("user falco rules set successfully")
else:
    print(res)
    sys.exit(1)
