#!/usr/bin/env python
#
# This script demonstrates how to use the `get_labels` function to retrieve metadata
# about label names and render the output as a table.
#

import sys
from sdcclient import SdcClient


def render_labels_as_table(labels):
    if not labels:
        print("No labels found.")
        return

    # Calculate the maximum width for the label column
    max_width = max(len(label) for label in labels)

    # Create a horizontal separator
    separator = "+" + "-" * (max_width + 2) + "+"

    # Create the header row
    header = f"| {'Label'.ljust(max_width)} |"

    # Create the rows for each label
    rows = [f"| {label.ljust(max_width)} |" for label in labels]

    # Combine everything into a table
    print(f"{separator}\n{header}\n{separator}\n" + "\n".join(rows) + f"\n{separator}")


#
# Parse arguments
#
if len(sys.argv) != 2:
    print(("usage: %s <sysdig-token>" % sys.argv[0]))
    print("You can find your token at https://app.sysdigcloud.com/#/settings/user")
    sys.exit(1)

sdc_token = sys.argv[1]
hostname = sys.argv[2]

sdclient = SdcClient(sdc_token, hostname)

#
# Optional matchers to filter the labels
#
match = ["up"]  # Replace with a list of matchers if needed

#
# Optional limit
#
limit = 10  # Set to None to disable the limit

#
# Fetch labels
#
ok, response_json = sdclient.get_labels(match=match, limit=limit)

#
# Show the result
#
if ok:
    #
    # Read the response. The JSON looks like this:
    #
    # {
    #     "status":   "success",
    #     "data": [
    #         "agent_id",
    #         "k8s_app",
    #         "kube_pod_uid",
    #         "kubernetes_io_cluster_service",
    #         "container_image_tag",
    #         "cloud_provider_tag_team",
    #         "cloud_provider_tag_expirationDate",
    #         "kube_pod_label_kubernetes_azure_com_managedby",
    #     ]
    # }
    #
    labels = response_json.get("data", [])
    render_labels_as_table(labels)
else:
    print("Error retrieving labels:", response_json)
