#!/usr/bin/env python
#
# This script demonstrates how to use the `get_label_values` function to retrieve values
# for a specific label and render the output as a table.
#

import sys
from sdcclient import SdcClient


def render_label_values_as_table(label_values):
    if not label_values:
        print("No values found for the specified label.")
        return

    # Calculate the maximum width for the value column
    max_width = max(len(value) for value in label_values)

    # Create a horizontal separator
    separator = "+" + "-" * (max_width + 2) + "+"

    # Create the header row
    header = f"| {'Value'.ljust(max_width)} |"

    # Create the rows for each label value
    rows = [f"| {value.ljust(max_width)} |" for value in label_values]

    # Combine everything into a table
    print(f"{separator}\n{header}\n{separator}\n" + "\n".join(rows) + f"\n{separator}")


#
# Parse arguments
#
if len(sys.argv) != 3:
    print(('usage: %s <sysdig-token> <label-name>' % sys.argv[0]))
    print('You can find your token at https://app.sysdigcloud.com/#/settings/user')
    sys.exit(1)

sdc_token = sys.argv[1]
hostname = sys.argv[2]

sdclient = SdcClient(sdc_token, hostname)

#
# The label name to fetch values for
#
label_name = "job"

#
# Optional matchers to filter the label values
#
match = None  # Replace with a list of matchers if needed

#
# Optional limit
#
limit = 10  # Set to None to disable the limit

#
# Fetch label values
#
ok, response_json = sdclient.get_label_values(label_name, match=match, limit=limit)

#
# Show the result
#
if ok:
    #
    # Read the response. The JSON looks like this:
    #
    # {
    #     "data": [
    #         "fluentd-default",
    #         "harbor-registry-default",
    #         "k8s-cadvisor-default",
    #         "k8s-kubelet-default",
    #         "k8s-pods",
    #         "k8s-pvc-default",
    #     ],
    #     "status": "success"
    # }
    #
    label_values = response_json.get("data", [])
    render_label_values_as_table(label_values)
else:
    print("Error retrieving label values:", response_json)
