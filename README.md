python-sdcclient
================

This is a python client API for Sysdig Cloud.

Overview
--------
This module is a light wrapper around the sysdig cloud API, which is documented [here](http://support.sysdigcloud.com/hc/en-us/articles/205233166-The-Sysdig-Cloud-API-Specification). 

In its basic form, this module can be used to call any API method and be expected to return a dict of the JSON reply.

Installation
------------
#### Automatic w/ PyPI ([virtualenv](http://virtualenv.readthedocs.org/en/latest/) is recommended.)
    pip install sdcclient

#### Manual
    git clone https://github.com/draios/python-sdc-client.git
    pip install

Usage
-----
The [examples](examples/) directory contains a number of examples that show how to use this API to perform many common tasks.

_Note:_ in order to use this API you must obtain a Sysdig Cloud token. You can get your user's token in the _Sysdig Cloud API_ section of the [settings](https://app.sysdigcloud.com/#/settings/user) page.

Return Values
-------------
Every method in the SdcClient class returns **a list with two entries**. The first one is a boolean value indicating if the call was successful. The second entry depends on the result:
- if the call was successful, it's a json object containing the generated data generated
- if the call failed, it's a string descibing the error

For an example on how to parse this output, take a look at a simple example like [get_data_simple.py](examples/get_data_simple.py) 

Methods
-------
####get_user_info(self)  
**Description**  
get details about the current user.  
**Return value**  
a json object containing information about the user, for example its email and the maximum number of agents it can install.  
**Example**  
[examples/print_user_info.py](examples/print_user_info.py).  

####get_n_connected_agents(self)  
**Description**  
return the number of agents currently connected to Sysdig Cloud for the current user.  
**Return value**  
an integer number.  
**Example**  
[examples/print_user_info.py](examples/print_user_info.py).  

####get_alerts(self)  
**Description**  
retrieve the list of alerts configured by the user.  
**Return value**  
an array of alert json objects, with the format described at [this link](https://app.sysdigcloud.com/apidocs/#!/Alerts/get_api_alerts).  
**Example**  
[examples/list_alerts.py](examples/list_alerts.py).  

#### create_alert(self, name, description, severity, for_atleast_s, condition, segmentby = [], segment_condition = 'ANY', filter = '', notify='', enabled=True, annotations={}):
**Description**  
create a threshold-based alert.  
**arguments**: 
- **name**: the alert name. This will appear in the Sysdig Cloud UI and in notification emails.
- **description**: the alert description. This will appear in the Sysdig Cloud UI and in notification emails.
- **severity**: syslog-encoded alert severity. This is a number from 0 to 7 where 0 means 'emergency' and 7 is 'debug'.
- **for_atleast_s**: the number of consecutive seconds the condition must be satisfied for the alert to fire. 
- **condition**: the alert condition, as described here https://app.sysdigcloud.com/apidocs/#!/Alerts/post_api_alerts
- **segmentby**: a list of Sysdig Cloud segmentation criteria that can be used to apply the alert to multiple entities. For example, segmenting a CPU alert by ['host.mac', 'proc.name'] allows to apply it to any process in any machine. 
- **segment_condition**: When _segmentby_ is specified (and therefore the alert will cover multiple entities) this field is used to determine when it will fire. In particular, you have two options for _segment_condition_: **ANY** (the alert will fire when at least one of the monitored entities satisfies the condition) and **ALL** (the alert will fire when all of the monitored entities satisfy the condition).
- **filter**: a boolean expression combining Sysdig Cloud segmentation criteria that makes it possible to reduce the scope of the alert. For example: _kubernetes.namespace.name='production' and container.image='nginx'_
- **notify**: the type of notification you want this alert to generate. Options are _EMAIL_, XXX.
- **enabled**: if True, the alert will be enabled when created.
- **annotations**: an optional dictionary of custom properties that you can associate to this alert for automation or management resons
**Return value**  
a json object describing the just created alert, with the format described at [this link](https://app.sysdigcloud.com/apidocs/#!/Alerts/post_api_alerts).  
**Example**  
[examples/create_alert.py](examples/create_alert.py).  
