#!/bin/bash

set -euxo pipefail

SCRIPT=$(readlink -f $0)
SCRIPTDIR=$(dirname $SCRIPT)

export SDC_URL=https://app-staging.sysdigcloud.com

AGENT_HOSTNAME=$(hostname -s)
SESSION_UUID=$(head -c 32 /dev/urandom | tr -dc 'a-zA-Z0-9')
ALERT_NAME=python-test-alert-$SESSION_UUID
DASHBOARD_1_NAME=prod-dashboard-$SESSION_UUID
DASHBOARD_2_NAME=dev-dashboard-$SESSION_UUID
EVENT_NAME=event-$SESSION_UUID
CAPTURE_NAME=apicapture-$SESSION_UUID
CHANNEL_NAME=channel-$SESSION_UUID
TEAM_NAME=team-$SESSION_UUID

date; $SCRIPTDIR/../examples/create_alert.py -a $ALERT_NAME $PYTHON_SDC_TEST_MONITOR_API_TOKEN
date; $SCRIPTDIR/../examples/update_alert.py -a $ALERT_NAME $PYTHON_SDC_TEST_MONITOR_API_TOKEN
date; $SCRIPTDIR/../examples/delete_alert.py -a $ALERT_NAME $PYTHON_SDC_TEST_MONITOR_API_TOKEN
date; $SCRIPTDIR/../examples/dashboard.py -d $DASHBOARD_1_NAME $PYTHON_SDC_TEST_MONITOR_API_TOKEN
date; $SCRIPTDIR/../examples/create_dashboard.py -d $DASHBOARD_2_NAME $PYTHON_SDC_TEST_MONITOR_API_TOKEN
date; $SCRIPTDIR/../examples/delete_dashboard.py -p $SESSION_UUID $PYTHON_SDC_TEST_MONITOR_API_TOKEN
date; $SCRIPTDIR/../examples/get_data_advanced.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN $AGENT_HOSTNAME
date; $SCRIPTDIR/../examples/get_data_datasource.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN
date; $SCRIPTDIR/../examples/get_data_simple.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN
date; $SCRIPTDIR/../examples/list_alerts.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN
date; $SCRIPTDIR/../examples/list_alert_notifications.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN
date; $SCRIPTDIR/../examples/resolve_alert_notifications.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN 1
date; $SCRIPTDIR/../examples/list_dashboards.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN
date; $SCRIPTDIR/../examples/list_hosts.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN
date; $SCRIPTDIR/../examples/list_metrics.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN
date; $SCRIPTDIR/../examples/post_event.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN $EVENT_NAME -d "test event description"
date; $SCRIPTDIR/../examples/post_event_simple.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN $EVENT_NAME "test event description"
date; $SCRIPTDIR/../examples/list_events.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN
date; $SCRIPTDIR/../examples/delete_event.py -e $EVENT_NAME $PYTHON_SDC_TEST_MONITOR_API_TOKEN
date; $SCRIPTDIR/../examples/print_data_retention_info.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN
date; $SCRIPTDIR/../examples/print_explore_grouping.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN
date; $SCRIPTDIR/../examples/print_user_info.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN
date; $SCRIPTDIR/../examples/list_users.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN
date; $SCRIPTDIR/../examples/list_sysdig_captures.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN
date; $SCRIPTDIR/../examples/create_sysdig_capture.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN $AGENT_HOSTNAME $CAPTURE_NAME 10
date; $SCRIPTDIR/../examples/notification_channels.py -c $CHANNEL_NAME $PYTHON_SDC_TEST_MONITOR_API_TOKEN
date; $SCRIPTDIR/../examples/user_team_mgmt.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN $TEAM_NAME example-user@example-domain.com
date; $SCRIPTDIR/../examples/user_team_mgmt_extended.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN $TEAM_NAME example-user@example-domain.com
