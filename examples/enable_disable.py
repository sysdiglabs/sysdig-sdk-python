#!/usr/bin/python
#This script enables and disables alerts on sysdig
#Script needs Sysdig Monitor API Token and name of the Alert(COMPONENT) as input for this script
#It runs list.py(lists all the alerts) and flip.py which changes the state of alert

import sys
import subprocess

token = sys.argv[1]
COMPONENT = sys.argv[2]


output = subprocess.check_output("python3 list.py {0} | grep -i {1}".format(token, COMPONENT), shell=True)

alerts = list(map(lambda x: ' '.join(x.split(":")[2:]).lstrip(), output.decode('ascii').split("\n")))
alerts = list(filter(None, alerts))
for each_alert in alerts:
    output = subprocess.check_output("python3 flip.py --alert '{0}' '{1}'".format(each_alert, token), shell=True)
    print(output)
