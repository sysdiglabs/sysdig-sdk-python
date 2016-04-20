python-sdcclient
================

[![Build Status](https://travis-ci.org/draios/python-sdc-client.png?branch=master)](https://travis-ci.org/draios/python-sdc-client)
[![Current version on PyPI](http://img.shields.io/pypi/v/sdcclient.svg)](https://pypi.python.org/pypi/sdcclient)

A python client API for Sysdig Cloud.

This module is a wrapper around the Sysdig Cloud API, which is documented [here](http://support.sysdigcloud.com/hc/en-us/articles/205233166-The-Sysdig-Cloud-API-Specification). It exposes most of the sysdig REST API functionality as an easy to use and easy to install python interface. The repository includes a rich set of examples (in the [examples](examples/) subdir) that quickly address several use cases.

Installation
------------
#### Automatic w/ PyPI ([virtualenv](http://virtualenv.readthedocs.org/en/latest/) is recommended.)
    pip install sdcclient

#### Manual
    git clone https://github.com/draios/python-sdc-client.git
    pip install

Quick start
-----------
- If you are interested in exporting metrics data from Sysdig Cloud, take a look at [examples/get_data_simple.py](examples/get_data_simple.py) and [examples/get_data_advanced.py](examples/get_data_advanced.py).
- If you want to programmatically create an alert, refer to [examples/create_alert.py](examples/create_alert.py)
- If you want to programmatically create a dashboard, refer to [examples/create_dashboard.py](examples/create_dashboard.py)

Usage
-----

_Note:_ in order to use this API you must obtain a Sysdig Cloud token. You can get your user's token in the _Sysdig Cloud API_ section of the [settings](https://app.sysdigcloud.com/#/settings/user) page.

The library exports a single class, `SdcClient`, that is used to connect to Sysdig Cloud and execute actions. It can be instantiated like this:

``` python
from sdcclient import SdcClient

sdc_token = "MY_API_TOKEN"

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)
```

Once instantiated, all the methods documented below can be called on the object.

####Return Values
Every method in the SdcClient class returns **a list with two entries**. The first one is a boolean value indicating if the call was successful. The second entry depends on the result:
- If the call was successful, it's a dictionary reflecting the json returned by the underlying REST call
- If the call failed, it's a string describing the error

For an example on how to parse this output, take a look at a simple example like [get_data_simple.py](examples/get_data_simple.py) 

Methods
-------
#### `add_dashboard_panel(self, dashboard, name, type, metrics, scope=None, layout=None, sort_by=None, paging=None)`
**Description**  
Adds a panel to the dashboard. A panel can be a time series, or a top chart (i.e. bar chart), or a number panel.

**Arguments**  
- **dashboard**: dashboard to edit
- **name**: name of the new panel
- **type**: type of the new panel. Valid values are: `timeSeries`, `top`, `number`
- **metrics**: list of metrics; Each metric must specified an `id` (e.g. `cpu.used.percent`) and if it's a value an `aggregation` dictionary with `time` and `group` to specify time aggregation and group aggregation respectively
- **scope**: filter to apply to the panel; Example: _kubernetes.namespace.name='production' and container.image='nginx'_.
- **sort_by**: Data sorting; The parameter is optional and it's a dictionary of `metric` and `mode` (it can be `desc` or `asc`)
- **paging**: Data pagination; The parameter is optional and limits the data points returned. The parameter is a dictionary of `from` and `to` with the index of the first and last point respectively
- **layout**: Size and position of the panel

**Success Return Value**  
A dictionary showing the details of the edited dashboard.

**Example**  
[examples/dashboard.py](examples/dashboard.py).

#### `add_email_notification_recipient(self, email)`
**Description**  
Add a new recipient for email alert notifications.  
**Arguments**  
- **email**: the email target to add.

**Success Return Value**  
A dictionary showing the updated user notifications configuration.  
**Example**  
[examples/add_notification_email.py](examples/add_notification_email.py).  

#### `create_alert(self, name, description, severity, for_atleast_s, condition, segmentby = [], segment_condition = 'ANY', filter = '', notify='', enabled=True, annotations={})`
**Description**  
Create a threshold-based alert.  
**Arguments**
- **name**: the alert name. This will appear in the Sysdig Cloud UI and in notification emails.
- **description**: the alert description. This will appear in the Sysdig Cloud UI and in notification emails.
- **severity**: syslog-encoded alert severity. This is a number from 0 to 7 where 0 means 'emergency' and 7 is 'debug'.
- **for_atleast_s**: the number of consecutive seconds the condition must be satisfied for the alert to fire. 
- **condition**: the alert condition, as described here https://app.sysdigcloud.com/apidocs/#!/Alerts/post_api_alerts
- **segmentby**: a list of Sysdig Cloud segmentation criteria that can be used to apply the alert to multiple entities. For example, segmenting a CPU alert by ['host.mac', 'proc.name'] allows to apply it to any process in any machine. 
- **segment_condition**: When _segmentby_ is specified (and therefore the alert will cover multiple entities) this field is used to determine when it will fire. In particular, you have two options for _segment_condition_: **ANY** (the alert will fire when at least one of the monitored entities satisfies the condition) and **ALL** (the alert will fire when all of the monitored entities satisfy the condition).
- **filter**: a boolean expression combining Sysdig Cloud segmentation criteria that makes it possible to reduce the scope of the alert. For example: _kubernetes.namespace.name='production' and container.image='nginx'_.
- **notify**: the type of notification you want this alert to generate. Options are _EMAIL_, _SNS_, _PAGER_DUTY_, _SYSDIG_DUMP_.
- **enabled**: if True, the alert will be enabled when created.
- **annotations**: an optional dictionary of custom properties that you can associate to this alert for automation or management resons

**Success Return Value**  
A dictionary describing the just created alert, with the format described at [this link](https://app.sysdigcloud.com/apidocs/#!/Alerts/post_api_alerts).  
**Example**  
[examples/create_alert.py](examples/create_alert.py).  

#### `create_dashboard(self, name)`
**Description**  
Creates an empty dashboard. You can then add panels by using `add_dashboard_panel`.

**Arguments**  
- **name**: the name of the dashboard that will be created.

**Success Return Value**  
A dictionary showing the details of the new dashboard.

**Example**  
[examples/dashboard.py](examples/dashboard.py).

#### `create_dashboard_from_dashboard(self, newdashname, templatename, filter)`
**Description**  
Create a new dasboard using one of the existing dashboards as a template. You will be able to define the scope of the new dasboard.  
**Arguments**  
- **newdashname**: the name of the dashboard that will be created.
- **viewname**: the name of the dasboard to use as the template, as it appears in the Sysdig Cloud dashboard page.
- **filter**: a boolean expression combining Sysdig Cloud segmentation criteria defines what the new dasboard will be applied to. For example: _kubernetes.namespace.name='production' and container.image='nginx'_.

**Success Return Value**  
A dictionary showing the details of the new dashboard.  
**Example**  
[examples/create_dashboard.py](examples/create_dashboard.py).  

#### `create_dashboard_from_view(self, newdashname, viewname, filter)`  
**Description**  
Create a new dasboard using one of the Sysdig Cloud views as a template. You will be able to define the scope of the new dasboard.  
**Arguments**  
- **newdashname**: the name of the dashboard that will be created.
- **viewname**: the name of the view to use as the template for the new dashboard. Thia corresponds to the name that the view has in the explore page.
- **filter**: a boolean expression combining Sysdig Cloud segmentation criteria defines what the new dasboard will be applied to. For example: _kubernetes.namespace.name='production' and container.image='nginx'_.

**Success Return Value**  
A dictionary showing the details of the new dashboard.  
**Example**  
[examples/create_dashboard.py](examples/create_dashboard.py).  

#### `create_sysdig_capture(self, hostname, capture_name, duration, capture_filter='', folder='/')`  
**Description**  
Create a new sysdig capture. The capture will be immediately started.  
**Arguments**  
- **hostname**: the hostname of the instrumented host where the capture will be taken.
- **capture_name**: the name of the capture.
- **duration**: the duration of the capture, in seconds.  
- **capture_filter**: a sysdig filter expression.  
- **folder**: directory in the S3 bucket where the capture will be saved.

**Success Return Value**  
A dictionary showing the details of the new capture.  
**Example**  
[examples/create_sysdig_capture.py](examples/create_sysdig_capture.py).  

#### `delete_alert(self, alert)`  
**Description**  
Deletes an alert.  
**Arguments**  
- **alert**: the alert object as returned by `get_alerts()`.

**Success Return Value**  
`None`.  
**Example**  
[examples/delete_alert.py](examples/delete_alert.py).  

#### `delete_dashboard(self, dashboard)`  
**Description**  
Deletes a dashboard.  
**Arguments**  
- **dashboard**: the dashboard object as returned by `get_dashboards()`.

**Success Return Value**  
`None`.  
**Example**  
[examples/delete_dashboard.py](examples/delete_dashboard.py).  

#### `delete_event(self, event)`  
**Description**  
Deletes an event.  
**Arguments**  
- **event**: the event object as returned by `get_events()`.

**Success Return Value**  
`None`.  
**Example**  
[examples/delete_event.py](examples/delete_event.py).  

#### `get_alerts(self)`  
**Description**  
Retrieve the list of alerts configured by the user.  
**Success Return Value**  
An array of alert json objects, with the format described at [this link](https://app.sysdigcloud.com/apidocs/#!/Alerts/get_api_alerts).  
**Example**  
[examples/list_alerts.py](examples/list_alerts.py).  

#### `get_data(self, metrics, start_ts, end_ts=0, sampling_s = 0, filter='', datasource_type='host')`  
**Description**  
This is the method you use to export metric data. It's flexible enough to offer both time-series and table-based data export.  
**Arguments**  
- **metrics**: a list of dictionaries, specifying the metrics and grouping keys that the query will return. A metric is any of the entries that can be found in the _Metrics_ section of the Explore page in sysdig cloud. Metric entries require an _aggregations_ section specifying how to aggregate the metric across time and containers/host. A grouping key is any of the entries that can be found in the _Show_ or _Segment By_ sections of the Explore page in sysdig cloud. These entries are used to apply single or hierarchical segmentation to the returned data and don't require the aggregations section. Refer to the examples section below for ready to use code snippets.  
- **start_ts**: the UTC time (in seconds) of the beginning of the data window. A negative value can be optionally used to indicate a relative time in the past from now. For example, -3600 means "one hour ago".
- **end_ts**: the UTC time (in seconds) of the end of the data window, or 0 to indicate "now". A negative value can also be optionally used to indicate a relative time in the past from now. For example, -3600 means "one hour ago".
- **sampling_s**: the duration of the samples that will be returned. 0 Means that the whole data will be returned as a single sample.
- **filter**: a boolean expression combining Sysdig Cloud segmentation criteria defines what the query will be applied to. For example: _kubernetes.namespace.name='production' and container.image='nginx'_.
- **datasource_type**: specify the metric source for the request, can be `container` or `host`. Most metrics, for example `cpu.used.percent` or `memory.bytes.used`, are reported by both hosts and containers. By default, host metrics are used, but if the request contains a container-specific grouping key in the metric list/filter (e.g. `container.name`), then the container source is used. In cases where grouping keys are missing or apply to both hosts and containers (e.g. `tag.Name`), datasource_type can be explicitly set to avoid any ambiguity and allow the user to select precisely what kind of data should be used for the request. [examples/get_data_datasource.py](examples/get_data_datasource.py) contains a few examples that should clarify the use of this argument.  

**Success Return Value**  
A dictionary with the requested data. Data is organized in a list of time samples, each of which includes a UTC timestamp and a list of values, whose content and order reflect what was specified in the _metrics_ argument.  
**Examples**  
[examples/get_data_simple.py](examples/get_data_simple.py), [examples/get_data_advanced.py](examples/get_data_advanced.py), [examples/list_hosts.py](examples/list_hosts.py), [examples/get_data_datasource.py](examples/get_data_datasource.py).  

#### `get_dashboards(self)`  
**Description**  
Return the list of dashboards available under the given user account. This includes the dashboards created by the user and the ones shared with her by other users.  
**Success Return Value**  
A dictionary containing the list of available sampling intervals.  
**Example**  
[examples/list_dashboards.py](examples/list_dashboards.py).  

#### `get_data_retention_info(self)`  
**Description**  
Return the list of data retention intervals, with beginning and end UTC time for each of them. Sysdig Cloud performs rollups of the data it stores. This means that data is stored at different time granularities depending on how far in time it is. This call can be used to know what precision you can expect before you make a call to `get_data()`.  
**Success Return Value**  
A dictionary containing the list of available sampling intervals.  
**Example**  
[examples/print_data_retention_info.py](examples/print_data_retention_info.py). 

#### `get_events(self, name=None, from_ts=None, to_ts=None, tags=None)` 
**Description**  
Returns the list of Sysdig Cloud events.  
**Arguments**  
- **name**: filter events by name.  
- **from_ts**: filter events by start time. Timestamp format is in UTC (seconds).
- **to_ts**: filter events by end time. Timestamp format is in UTC (seconds).
- **tags**: filter events by tags. Can be, for example `tag1 = 'value1'`.  

**Success Return Value**  
A dictionary containing the list of events.  
**Example**  
[examples/list_events.py](examples/list_events.py). 

#### `get_explore_grouping_hierarchy(self)`  
**Description**  
Return the user's current Explore gourping hierarchy.  
**Success Return Value**  
A list containing the list of the user's Explore grouping criteria.  
**Example**  
[examples/print_explore_grouping.py](examples/print_explore_grouping.py).  

#### `get_metrics(self)`  
**Description**  
Return the metric list that can be used for data requests/alerts/dashboards.  
**Success Return Value**  
A dictionary containing the list of available metrics.  
**Example**  
[examples/list_metrics.py](examples/list_metrics.py).  

#### `get_connected_agents(self)`  
**Description**  
Return the agents currently connected to Sysdig Cloud for the current user.  
**Success Return Value**  
A list of the agents with all their attributes.  

#### `get_n_connected_agents(self)`  
**Description**  
Return the number of agents currently connected to Sysdig Cloud for the current user.  
**Success Return Value**  
An integer number.  

#### `get_notifications(self, from_ts, to_ts, state=None, resolved=None)`
**Description**  
Returns the list of Sysdig Cloud alert notifications.  
**Arguments**  
- **from_ts**: filter events by start time. Timestamp format is in UTC (seconds). 
- **to_ts**: filter events by start time. Timestamp format is in UTC (seconds).
- **state**: filter events by alert state. Supported values are `OK` and `ACTIVE`.  
- **resolved**: filter events by resolution status. Supported values are `True` and `False.

**Success Return Value**  
A dictionary containing the list of notifications.  
**Example**  
[examples/list_alert_notifications.py](examples/list_alert_notifications.py). 

#### `get_sysdig_captures(self)`
**Description**  
Returns the list of sysdig captures for the user.  
**Success Return Value**  
A dictionary containing the list of captures.  
**Example**  
[examples/list_sysdig_captures.py](examples/list_sysdig_captures.py). 

#### `get_user_info(self)`  
**Description**  
Get details about the current user.  
**Success Return Value**  
A dictionary containing information about the user, for example its email and the maximum number of agents it can install.  
**Example**  
[examples/print_user_info.py](examples/print_user_info.py).  

#### `find_dashboard_by(self, name)`
**Description**  
Finds dashboards with the specified name. You can then delete the dashboard (with `delete_dashboard`) or edit panels (with `add_dashboard_panel` and `remove_dashboard_panel`)

**Arguments**  
- **name**: the name of the dashboards to find.

**Success Return Value**  
A list of dictionaries of dashboards matching the specified name.

**Example**  
[examples/dashboard.py](examples/dashboard.py).

#### `poll_sysdig_capture(self, capture)`  
**Description**  
Fetch the updated state of a sysdig capture. Can be used to poll the status of a capture that has been previously created and started with `create_sysdig_capture`.  
**Arguments**  
- **capture**: the capture object as returned by `get_sysdig_captures()` or `create_sysdig_capture()`.

**Success Return Value**  
A dictionary showing the updated details of the capture. Use the `status` field to check the progress of a capture.    
**Example**  
[examples/create_sysdig_capture.py](examples/create_sysdig_capture.py).  

#### `post_event(self, name, description=None, severity=None, event_filter=None, tags=None)`
**Description**  
You can use this method you use to send an event to Sysdig Cloud. The events you post are available in the Events tab in the Sysdig Cloud UI and can be overlied to charts.  
**Arguments**  
- **name**: the name of the new event.  
- **description**: a longer description offering detailed information about the event.
- **severity**: syslog style from 0 (high) to 7 (low).
- **event_filter**: metadata, in Sysdig Cloud format, of nodes to associate with the event, e.g. `host.hostName = 'ip-10-1-1-1' and container.name = 'foo'`.
- **tags**: a list of key-value dictionaries that can be used to tag the event. Can be used for filtering/segmenting purposes in Sysdig Cloud.

**Success Return Value**  
A dictionary describing the new event.  
**Example**  
[examples/post_event_simple.py](examples/post_event_simple.py)
[examples/post_event.py](examples/post_event.py).  

#### `remove_dashboard_panel(self, dashboard, panel_name)`
**Description**  
Removes a panel from the dashboard. The panel to remove is identified by the specified `name`.

**Arguments**  
- **name**: name of the panel to find and remove

**Success Return Value**  
A dictionary showing the details of the edited dashboard.

**Example**  
[examples/dashboard.py](examples/dashboard.py).

#### `update_notification_resolution(self, notification, resolved)`
**Description**  
Updates the resolution status of an alert notification.  
**Arguments**  
- **notification**: notification object as returned by `get_notifications()`. 
- **resolved**: new resolution status. Supported values are `True` and `False`.

**Success Return Value**  
The updated notification.  
**Example**  
[examples/resolve_alert_notifications.py](examples/resolve_alert_notifications.py). 
