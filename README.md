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
**Description**: get details about the current user.  
**Return value**: a json object containing information about the user, for example its email and the maximum number of agents it can install.  
**Example**: [examples/print_user_info.py](examples/print_user_info.py).  

####get_n_connected_agents(self)  
**Description**: return the number of agents currently connected to Sysdig Cloud for the current user.  
**Return value**: an integer number.  
**Example**: [examples/print_user_info.py](examples/print_user_info.py).  

####get_alerts(self)  
**Description**: retrieves the list of alerts configured by the user.  
**Return value**: an array of alert json objects, with the format described at [this link](https://app.sysdigcloud.com/apidocs/#!/Alerts/get_api_alerts).  
**Example**: [examples/list_alerts.py](examples/list_alerts.py).  
