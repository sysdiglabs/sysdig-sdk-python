Usage
=====

In order to use this API you must obtain a Sysdig Monitor/Secure API token.
You can get your user’s token in the Sysdig Monitor API section of the settings
page for `monitor`_ or `secure`_.

.. _monitor: https://app.sysdigcloud.com/#/settings/user
.. _secure: https://secure.sysdig.com/#/settings/user

The library exports two classes, ``SdMonitorClient`` and ``SdSecureClient`` that are
used to connect to Sysdig Monitor/Secure and execute actions.

They can be instantiated like this:

.. code-block:: python
    :linenos:

    from sdcclient import SdMonitorClient

    api_token = "MY_API_TOKEN"

    # Instantiate the Sysdig Monitor client
    client = SdMonitorClient(api_token)
