#!/usr/bin/env python
#
# This script demonstrates how to use the `get_series` function to retrieve metadata
# about time series that match a set of label matchers.
#

import sys
from sdcclient import SdcClient


def render_json_as_table(results):
    if not data or len(data) == 0:
        print("No series found for the given matchers.")
        return

    # Extract all keys from the JSON objects
    keys = list(results[0].keys())

    # Calculate the maximum width for each column
    column_widths = {key: max(len(key), max(len(str(row.get(key, ""))) for row in results)) for key in keys}

    # Create a horizontal separator
    separator = "+".join("-" * (column_widths[key] + 2) for key in keys)

    # Create the header row
    header = "|".join(f" {key.ljust(column_widths[key])} " for key in keys)

    # Create the rows for each JSON object
    rows = []
    for row in results:
        rows.append("|".join(f" {str(row.get(key, '')).ljust(column_widths[key])} " for key in keys))

    # Combine everything into a table
    print(f"+{separator}+\n|{header}|\n+{separator}+\n" + "\n".join(f"|{row}|" for row in rows) + f"\n+{separator}+")


#
# Parse arguments
#
if len(sys.argv) != 2:
    print(('usage: %s <sysdig-token>' % sys.argv[0]))
    print('You can find your token at https://app.sysdigcloud.com/#/settings/user')
    sys.exit(1)

sdc_token = sys.argv[1]
hostname = sys.argv[2]

sdclient = SdcClient(sdc_token, hostname)

#
# Matchers to filter the series. Example: `up` and `process_start_time_seconds{job="prometheus"}`
#
match = [
    'up',
    'process_start_time_seconds{job="prometheus"}'
]

#
# Optional time range
#
start = None  # Replace with a timestamp if needed
end = None    # Replace with a timestamp if needed

#
# Optional limit
#
limit = 5  # Set to None to disable the limit

#
# Fetch series
#
ok, response_json = sdclient.get_series(match, start=start, end=end, limit=limit)

#
# Show the result
#
if ok:
    #
    # Read the response. The JSON looks like this:
    #
    # {
    #     "data":   [
    #         {
    #           "__name__": "up",
    #           "_sysdig_custom_metric": "true",
    #           "_sysdig_datasource": "prometheus_remote_write",
    #           "agent_version": "thereal-test-x86_64",
    #           "instance": "default.test.svc.cluster.local:9544",
    #           "jenkins_job_build_number": "1234",
    #           "job": "default-test-20250428112951594",
    #           "remote_write": "true"
    #         }
    #     ],
    #     "status": "success"
    # }
    #
    data = response_json.get("data", {})
    render_json_as_table(data)
else:
    print("Error retrieving series:", response_json)
