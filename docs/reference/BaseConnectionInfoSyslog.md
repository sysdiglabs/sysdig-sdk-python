# BaseConnectionInfoSyslog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Address of the Syslog server | 
**port** | **int** | port of the syslog server | 
**message_format** | **str** | The syslog message format. RFC_5425 is TLS only | 
**type** | **str** | protocol, tcp or udp (case insensitive) | [optional] [default to 'tcp']
**is_insecure** | **bool** | Skip TLS certificate verification | [optional] [default to False]
**formatter** | **str** | The message content format | [optional] [default to 'JSON']
**certificate_id** | **int** | ID of a certificate stored in Sysdig&#39;s [Certificates Management tool](#tag/Certificates). Note that the RFC 5425 (TLS) protocol is required for you to see this field | [optional] 

## Example

```python
from sysdig_client.models.base_connection_info_syslog import BaseConnectionInfoSyslog

# TODO update the JSON string below
json = "{}"
# create an instance of BaseConnectionInfoSyslog from a JSON string
base_connection_info_syslog_instance = BaseConnectionInfoSyslog.from_json(json)
# print the JSON string representation of the object
print(BaseConnectionInfoSyslog.to_json())

# convert the object into a dict
base_connection_info_syslog_dict = base_connection_info_syslog_instance.to_dict()
# create an instance of BaseConnectionInfoSyslog from a dict
base_connection_info_syslog_from_dict = BaseConnectionInfoSyslog.from_dict(base_connection_info_syslog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


