#!/bin/bash

set -euxo pipefail

SCRIPT=$(readlink -f $0)
SCRIPTDIR=$(dirname $SCRIPT)

export SDC_URL=https://app-staging.sysdigcloud.com

docker run -d -it --rm --name sysdig-agent --privileged --net host --pid host -e COLLECTOR=collector-staging.sysdigcloud.com -e ACCESS_KEY=$PYTHON_SDC_TEST_ACCESS_KEY -v /var/run/docker.sock:/host/var/run/docker.sock  -v /dev:/host/dev -v /proc:/host/proc:ro -v /boot:/host/boot:ro -v /lib/modules:/host/lib/modules:ro -v /usr:/host/usr:ro sysdig/agent

sleep 20

AGENT_HOSTNAME=$(hostname -s)
SESSION_UUID=$(head -c 32 /dev/urandom | tr -dc 'a-zA-Z0-9')
ALERT_NAME=python-test-alert-$SESSION_UUID
DASHBOARD_1_NAME=prod-dashboard-$SESSION_UUID
DASHBOARD_2_NAME=dev-dashboard-$SESSION_UUID
EVENT_NAME=event-$SESSION_UUID
CAPTURE_NAME=apicapture-$SESSION_UUID
CHANNEL_NAME=channel-$SESSION_UUID
TEAM_NAME=team-$SESSION_UUID

$SCRIPTDIR/../examples/create_alert.py -a $ALERT_NAME $PYTHON_SDC_TEST_MONITOR_API_TOKEN
$SCRIPTDIR/../examples/update_alert.py -a $ALERT_NAME $PYTHON_SDC_TEST_MONITOR_API_TOKEN
$SCRIPTDIR/../examples/delete_alert.py -a $ALERT_NAME $PYTHON_SDC_TEST_MONITOR_API_TOKEN
$SCRIPTDIR/../examples/dashboard.py -d $DASHBOARD_1_NAME $PYTHON_SDC_TEST_MONITOR_API_TOKEN
$SCRIPTDIR/../examples/create_dashboard.py -d $DASHBOARD_2_NAME $PYTHON_SDC_TEST_MONITOR_API_TOKEN
$SCRIPTDIR/../examples/delete_dashboard.py -p $SESSION_UUID $PYTHON_SDC_TEST_MONITOR_API_TOKEN
$SCRIPTDIR/../examples/get_data_advanced.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN $AGENT_HOSTNAME
$SCRIPTDIR/../examples/get_data_datasource.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN
$SCRIPTDIR/../examples/get_data_simple.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN
$SCRIPTDIR/../examples/list_alerts.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN
$SCRIPTDIR/../examples/list_alert_notifications.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN
$SCRIPTDIR/../examples/resolve_alert_notifications.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN 1
$SCRIPTDIR/../examples/list_dashboards.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN
$SCRIPTDIR/../examples/list_hosts.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN
$SCRIPTDIR/../examples/list_metrics.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN
$SCRIPTDIR/../examples/post_event.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN $EVENT_NAME -d "test event description"
$SCRIPTDIR/../examples/post_event_simple.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN $EVENT_NAME "test event description"
$SCRIPTDIR/../examples/list_events.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN
$SCRIPTDIR/../examples/delete_event.py -e $EVENT_NAME $PYTHON_SDC_TEST_MONITOR_API_TOKEN
$SCRIPTDIR/../examples/print_data_retention_info.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN
$SCRIPTDIR/../examples/print_explore_grouping.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN
$SCRIPTDIR/../examples/print_user_info.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN
$SCRIPTDIR/../examples/list_users.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN
$SCRIPTDIR/../examples/list_sysdig_captures.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN
$SCRIPTDIR/../examples/create_sysdig_capture.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN $AGENT_HOSTNAME $CAPTURE_NAME 10
$SCRIPTDIR/../examples/notification_channels.py -c $CHANNEL_NAME $PYTHON_SDC_TEST_MONITOR_API_TOKEN
$SCRIPTDIR/../examples/user_team_mgmt.py $PYTHON_SDC_TEST_MONITOR_API_TOKEN $TEAM_NAME example-user@example-domain.com

docker stop sysdig-agent

