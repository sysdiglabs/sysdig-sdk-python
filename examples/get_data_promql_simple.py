#!/usr/bin/env python
#
# This script shows the basics of getting data out of Sysdig Monitor by creating a
# simple query that returns the total CPU usage of all containers in all pods in the
# last 10 minutes. The query is executed over a 5-minute time window.
#

import sys
import time
from datetime import datetime

from sdcclient import SdcClient


def print_prometheus_results_as_table(results):
    if not results:
        print("No data found for the query.")
        return

    # Store time series data
    all_timestamps = set()
    label_keys = []
    time_series_by_label = {}

    for series in results:
        metric = series.get("metric", {})
        label = ",".join(f"{k}={v}" for k, v in sorted(metric.items()))
        label_keys.append(label)
        time_series_by_label[label] = {}

        for timestamp, value in series.get("values", []):
            ts = int(float(timestamp))
            all_timestamps.add(ts)
            time_series_by_label[label][ts] = value

    # Prepare header
    label_keys = sorted(set(label_keys))
    all_timestamps = sorted(all_timestamps)

    print(f"{'Timestamp':<25} | " + " | ".join(f"{label}" for label in label_keys))
    print("-" * (26 + len(label_keys) * 25))

    # Print each row, filling in missing values with "N/A"
    for ts in all_timestamps:
        dt = datetime.fromtimestamp(ts).isoformat()
        row_values = []
        for label in label_keys:
            value = time_series_by_label.get(label, {}).get(ts, "N/A")
            row_values.append(value)
        print(f"{dt:<25} | " + " | ".join(f"{val:>20}" for val in row_values))


#
# Parse arguments
#
if len(sys.argv) != 3:
    print(("usage: %s <sysdig-token> <hostname>" % sys.argv[0]))
    print("You can find your token at https://app.sysdigcloud.com/#/settings/user")
    sys.exit(1)

sdc_token = sys.argv[1]
hostname = sys.argv[2]

sdclient = SdcClient(sdc_token, hostname)

#
# A PromQL query to execute. In this example, we are querying for the total CPU usage
# of all containers in all pods in the last 10 minutes.
#
query = """
sum (
  avg_over_time(kube_pod_container_resource_requests{resource="cpu"}[10m])
)
"""

#
# Time window:
#   - end is the current time
#   - start is the current time minus 5 minutes
#
end = int(time.time())
start = end - 5 * 60  # 5 minutes ago

#
# Step:
#   - resolution step, how far should timestamp of each resulting sample be apart
#
step = 60

#
# Load data
#
ok, response_json = sdclient.get_data_promql(query, start, end, step)

#
# Show the result
#
if ok:
    #
    # Read the response. The JSON looks like this:
    #
    # {
    #     "data":   {
    #         "result":     [
    #             {
    #                 "metric": {},
    #                 "values": [
    #                     [
    #                         1744210080,
    #                         "0.58"
    #                     ],
    #                     [
    #                         1744210140,
    #                         "0.58"
    #                     ],
    #                     [
    #                         1744210200,
    #                         "0.58"
    #                     ],
    #                     [
    #                         1744210260,
    #                         "0.5799999999999998"
    #                     ],
    #                     [
    #                         1744210320,
    #                         "0.5799999999999998"
    #                     ],
    #                     [
    #                         1744210380,
    #                         "0.5799999999999998"
    #                     ]
    #                 ]
    #             }
    #         ],
    #         "resultType": "matrix"
    #     },
    #     "status": "success"
    # }
    #

    #
    # Print summary (what, when)
    #
    results = response_json.get("data", {}).get("result", [])
    print_prometheus_results_as_table(results)

else:
    print(response_json)
    sys.exit(1)
