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
def evaluate(scope, expected):
    parsed_scope = sdclient._convert_scope_string_to_expression(scope)
    print '{} is valid: {}'.format(scope, parsed_scope[0] == True)

    if parsed_scope[0] != expected:
        print('Unexpected parsing result!')
        sys.exit(1)


# simple example: tag = value
evaluate('proc.name = "cassandra"', True)

# NOTE: For now you can still leave values without quotes.
# The API will be more strict, so please make sure you adopt the new format!
evaluate('proc.name = cassandra', True)

# other operators
evaluate('proc.name != "cassandra"', True)
evaluate('proc.name starts with "cassandra"', True)
evaluate('proc.name contains "cassandra"', True)

# list operators
evaluate('proc.name in ("cassandra", "mysql")', True)

# not-ed expressions
evaluate('not proc.name starts with "cassandra"', True)
evaluate('not proc.name contains "cassandra"', True)
evaluate('not proc.name in ("cassandra", "mysql")', True)

# you can combine multiple expressions; note that only AND'd scopes are currently supported
evaluate('kubernetes.service.name = "database" and proc.name = "cassandra"', True)

# the scope can obviously be omitted in the dashboard configuration
evaluate('', True)
evaluate(None, True)

# invalid scopes will cause errors
evaluate('proc.name == "cassandra"', False) # invalid operator

# currently, one space is required around operands and operators -- improvements will come soon
evaluate('proc.name="cassandra"', False)

#
# The current grammer is unable to validate all errors -- in these cases, the API will fail!
# Improvements will come soon!
#
# Here some errors that will not be detected by the Python library, but the API will
#
evaluate('proc.name = "cassandra" or proc.name = "mysql"', True) # not AND'd expressions are supported
evaluate('proc.name in ("cassandra\', \'mysql")', True) # mismatching quotes
evaluate('proc.name in ("cassandra", "mysql"', True) # missing parenthesis
