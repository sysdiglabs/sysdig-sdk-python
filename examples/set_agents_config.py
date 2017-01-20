#!/usr/bin/env python
#
# Set the sysdig cloud agents configuration.
# This script takes a user token and a json file as input, and pushes the configuration 
# in the json file to the user.
# Typically, you want to create the json file by using the get_agents_config.py script,
# edit it and then push it back with this script.
#

import os
import sys
import json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient

#
# Parse arguments
#
if len(sys.argv) != 3:
    print 'usage: %s <sysdig-token> <config-json-file>' % sys.argv[0]
    print 'You can find your token at https://app.sysdigcloud.com/#/settings/user'
    sys.exit(1)

sdc_token = sys.argv[1]

#
# Load the config file
#
with open(sys.argv[2]) as cfile:    
    conf = json.load(cfile)

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token, 'https://app-staging.sysdigcloud.com')

#
# Push the configuration
#
res = sdclient.set_agents_config(conf)

#
# Check if everything went well
#
if res[0]:
    print 'configuration set successfully'
else:
    print res[1]
