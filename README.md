Sysdig Cloud python client library
===

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

Function List
-------------

Please Refer to the [Python Script Library documentation page](http://python-sdc-client.readthedocs.io/en/latest/) for the list of functions available.

Transitioning from python to REST
---------------------------------

If your goal is to interact with the REST API directly, you can use this python client library to easily understand the REST interactions by logging the actions it takes.  This is useful because full documentation of the REST API has not yet been created; and also provides a complete example of known working operations.

- Use or modify an example, or write a new script against the python sdcclient module.
- Log the HTTP requests made by the script.

To log all the requests made by your script in significant detail, add to your script:

``` python
import logging
import httplib
httplib.HTTPConnection.debuglevel = 1

logging.basicConfig() # you need to initialize logging, otherwise you will not see anything from requests
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True
```

Then run as normal.
