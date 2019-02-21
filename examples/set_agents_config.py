#!/usr/bin/env python
#
# Set the sysdig cloud agents configuration.
# This script takes a user token and a yaml configuration file as input, and pushes the configuration
# in the yaml config file to the user.
# Typically, you want to first read the config file using the get_agents_config.py script,
# edit it and then push it back with this script.
#

import os
import sys
import yaml
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient

#
# Parse arguments
#
if len(sys.argv) != 3:
    print('usage: %s <sysdig-token> <agent-yaml-config-file>' % sys.argv[0])
    print('You can find your token at https://app.sysdigcloud.com/#/settings/user')
    sys.exit(1)

sdc_token = sys.argv[1]

#
# Load the config file
#
with open(sys.argv[2]) as cfile:
    yaml_conf = cfile.read()
    # Verify that the content is valid yaml
    parsed_yaml_conf = yaml.load(yaml_conf)
#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token, 'https://app.sysdigcloud.com')

json = {"files": [{"filter": "*", "content": yaml_conf}]}

#
# Push the configuration
#
ok, res = sdclient.set_agents_config(json)

#
# Check if everything went well
#
if ok:
    print('configuration set successfully')
else:
    print(res)
