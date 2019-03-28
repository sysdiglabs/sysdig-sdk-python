#!/usr/bin/env python
#
# This example shows how to delete a dashboard
#

import getopt
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdMonitorClient


#
# Parse arguments
#
def usage():
    print('usage: %s [-p|--pattern <name>] <sysdig-token>' % sys.argv[0])
    print('-p|--pattern: Delete all dashboards containing the provided pattern')
    print('You can find your token at https://app.sysdigcloud.com/#/settings/user')
    sys.exit(1)


try:
    opts, args = getopt.getopt(sys.argv[1:], "p:", ["pattern="])
except getopt.GetoptError:
    usage()

pattern = "API Test"
for opt, arg in opts:
    if opt in ("-p", "--pattern"):
        pattern = arg

if len(args) != 1:
    usage()

sdc_token = args[0]

#
# Instantiate the SDC client
#
sdclient = SdMonitorClient(sdc_token)

#
# List the dashboards
#
ok, res = sdclient.get_dashboards()
if not ok:
    print(res)
    sys.exit(1)

#
# Delete all the dashboards containing pattern
#
for dashboard in res['dashboards']:
    if pattern in dashboard['name']:
        print("Deleting " + dashboard['name'])
        ok, res = sdclient.delete_dashboard(dashboard)
        if not ok:
            print(res)
            sys.exit(1)
