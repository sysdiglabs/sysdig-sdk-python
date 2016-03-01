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
See examples in [examples](examples/)

_Note:_ in order to use this API you must obtain a Sysdig Cloud token. You can get your user's token in the _Sysdig Cloud API_ section of the [settings](https://app.sysdigcloud.com/#/settings/user) page.

Methods
-------

| Method | Description |
| ----- | ----- |
| SdcClient.**get_user_info()** | Get details about the current user. |
| SdcClient.**get_user_info()** | Get details about the current user. |
