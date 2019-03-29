#!/usr/bin/env python
#
# This example shows some examples of scope you can use for dashboards.
#

import getopt
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient

# random token, since we're not going to use the API for real
sdc_token = "bb8754d5-025d-4b88-a815-358fba58c4be"

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)

#
# Scopes can be passed to most of dashboard-related functions, e.g. create_dashboard_from_file.
#
# NOTE: _convert_scope_string_to_expression should never be used in a user script
# We're going to use it here just to demonstrate some scope options and some constraints
#
def evaluate(scope):
    parsed_scope = sdclient._convert_scope_string_to_expression(scope)
    print '{} is valid: {}'.format(scope, parsed_scope[0] == True)

# simple example: tag = value
evaluate('proc.name = "cassandra"')

# other operators
evaluate('proc.name != "cassandra"')
evaluate('proc.name starts with "cassandra"')
evaluate('proc.name contains "cassandra"')

# list operators
evaluate('proc.name in ("cassandra", "mysql")')

# not-ed expressions
evaluate('not proc.name starts with "cassandra"')
evaluate('not proc.name contains "cassandra"')
evaluate('not proc.name in ("cassandra", "mysql")')

# you can combine multiple expressions; note that only and-ed scopes are currently supported
evaluate('kubernetes.service.name = "database" and proc.name = "cassandra"')

# the scope can obviously be omitted in the dashboard configuration
evaluate('')
evaluate(None)