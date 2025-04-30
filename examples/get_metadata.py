#!/usr/bin/env python
#
# This script demonstrates how to use the `get_metadata` function to retrieve metadata
# about metrics and render the output as a table.
#

import sys
from sdcclient import SdcClient


def render_metadata_as_table(metadata):
    if not metadata:
        print("No metadata found.")
        return

    # Extract all metric names and their metadata
    rows = []
    for metric, details in metadata.items():
        for detail in details:
            rows.append({
                "Metric": metric,
                "Type": detail.get("type", ""),
                "Unit": detail.get("unit", ""),
                "Help": detail.get("help", "")
            })

    # Extract column names
    columns = ["Metric", "Type", "Unit", "Help"]

    # Calculate the maximum width for each column
    column_widths = {col: max(len(col), max(len(str(row[col])) for row in rows)) for col in columns}

    # Create a horizontal separator
    separator = "+" + "+".join("-" * (column_widths[col] + 2) for col in columns) + "+"

    # Create the header row
    header = "|" + "|".join(f" {col.ljust(column_widths[col])} " for col in columns) + "|"

    # Create the rows for each metadata entry
    table_rows = [
        "|" + "|".join(f" {str(row[col]).ljust(column_widths[col])} " for col in columns) + "|"
        for row in rows
    ]

    # Combine everything into a table
    print(f"{separator}\n{header}\n{separator}\n" + "\n".join(table_rows) + f"\n{separator}")


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
# Optional metric name to filter metadata
#
metric_name = "up"  # Replace with a specific metric name if needed

#
# Optional limit
#
limit = 10  # Set to None to disable the limit

#
# Fetch metadata
#
ok, response_json = sdclient.get_metadata(metric_name=metric_name, limit=limit)

#
# Show the result
#
if ok:
    #
    # Read the response. The JSON looks like this:
    #
    # {
    #     "data": [
    #         "up": [
    #             {
    #                 "type": "gauge",
    #                 "unit": "number",
    #                 "help": ""
    #             }
    #         ]
    #         ...
    #     ],
    #     "status": "success"
    # }
    #
    metadata = response_json.get("data", [])
    render_metadata_as_table(metadata)
else:
    print("Error retrieving metadata:", response_json)
