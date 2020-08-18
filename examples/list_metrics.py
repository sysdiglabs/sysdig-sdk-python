#!/usr/bin/env python
#
# Print the list of metrics.
#

import sys

from sdcclient import SdcClient

#
# Parse arguments
#
if len(sys.argv) != 2:
    print(('usage: %s <sysdig-token>' % sys.argv[0]))
    print('You can find your token at https://app.sysdigcloud.com/#/settings/user')
    sys.exit(1)

sdc_token = sys.argv[1]

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)

#
# Fire the request.
#
ok, res = sdclient.get_metrics()

#
# Show the list of metrics
#
if not ok:
    print(res)
    sys.exit(1)

for metric_id, metric in res.items():
    print(("Metric name: " + metric_id + ", type: " + metric['type']))
