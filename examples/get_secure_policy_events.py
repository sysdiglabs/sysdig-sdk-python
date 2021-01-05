#!/usr/bin/env python
#
# Get all policy events for a given time range or in the last N seconds.
# The events are written in jsonl format to stdout.
#
# If --summarize is provided, summarize the policy events by sanitized
# (removing container ids when present) description and print the
# descriptions by decreasing frequency.  This allows you to see which policy
# events are occurring most often.
#
# Progress information is written to standard error.
#

import getopt
import sys

from sdcclient import SdSecureClient


def usage():
    print(('usage: %s [-s|--summarize] [-l|--limit <limit>] <sysdig-token> [<duration sec>|<from sec> <to sec>]' %
           sys.argv[0]))
    print('-s|--summarize: group policy events by sanitized output and print by frequency')
    print('-l|--limit: with -s, only print the first <limit> outputs')
    print('You can find your token at https://secure.sysdig.com/#/settings/user')
    sys.exit(1)


try:
    opts, args = getopt.getopt(sys.argv[1:], "sl:", ["summarize", "limit="])
except getopt.GetoptError:
    usage()

summarize = False
limit = 0
for opt, arg in opts:
    if opt in ("-s", "--summarize"):
        summarize = True
    elif opt in ("-l", "--limit"):
        limit = int(arg)
#
# Parse arguments
#
if len(args) < 2:
    usage()

sdc_token = args[0]

duration = None
from_sec = None
to_sec = None

if len(args) == 2:
    duration = args[1]
elif len(args) == 3:
    from_sec = args[1]
    to_sec = args[2]
else:
    usage()

#
# Instantiate the SDC client
#
sdclient = SdSecureClient(sdc_token, 'https://secure.sysdig.com')

if duration is not None:
    ok, res = sdclient.get_policy_events_duration(duration)
else:
    ok, res = sdclient.get_policy_events_range(from_sec, to_sec)

all_outputs = dict()

if not ok:
    print(res)
    sys.exit(1)

print(res["data"])
