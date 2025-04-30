#!/usr/bin/env python
#
# This script shows the basics of getting data out of Sysdig Monitor by creating a
# simple query that returns the total CPU usage of all containers in all pods in the
# last 10 minutes. The query is executed at a timestamp 5 minutes ago.
#

import sys
import time
from datetime import datetime

from sdcclient import SdcClient


def print_prometheus_instant_result(result):
    if not result:
        print("No data found for the instant query.")
        return

    # Determine if any result has labels
    has_labels = any(entry.get("metric") for entry in result)

    if has_labels:
        print(f"{'Timestamp':<25} | {'Metric':<40} | {'Value':>10}")
        print("-" * 80)
    else:
        print(f"{'Timestamp':<25} | {'Value':>10}")
        print("-" * 40)

    for entry in result:
        timestamp, value = entry.get("value", [None, None])
        dt = datetime.fromtimestamp(float(timestamp)).isoformat() if timestamp else "N/A"
        metric = entry.get("metric", {})

        if has_labels:
            label_str = ', '.join(f'{k}="{v}"' for k, v in sorted(metric.items()))
            print(f"{dt:<25} | {label_str:<40} | {value:>10}")
        else:
            print(f"{dt:<25} | {value:>10}")


#
# Parse arguments
#
if len(sys.argv) != 3:
    print(('usage: %s <sysdig-token> <hostname>' % sys.argv[0]))
    print('You can find your token at https://app.sysdigcloud.com/#/settings/user')
    sys.exit(1)

sdc_token = sys.argv[1]
hostname = sys.argv[2]

sdclient = SdcClient(sdc_token, hostname)

#
# A PromQL query to execute. In this example, we are querying for the total CPU usage
# of all containers in all pods in the last 10 minutes.
#
query = '''
sum (
  avg_over_time(kube_pod_container_resource_requests{resource="cpu"}[10m])
)
'''

#
# Time:
#   - the parameter is optional; if not set, the current time is used
#
time = int(time.time()) - 5 * 60  # 5 minutes ago

#
# Load data
#
ok, response_json = sdclient.get_data_promql_instant(query, time)

#
# Show the result
#
if ok:
    #
    # Read the response. The JSON looks like this:
    #
    # {
    #     "result":     [
    #         {
    #             "metric": {},
    #             "value":  [
    #                 1744272414,
    #                 "0.58"
    #             ]
    #         }
    #     ],
    #     "resultType": "vector"
    # }
    #


    #
    # Print summary (what, when)
    #
    results = response_json.get("data", {}).get("result", [])
    print_prometheus_instant_result(results)

else:
    print(response_json)
    sys.exit(1)
