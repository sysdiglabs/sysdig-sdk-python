# SplunkCreateConnectionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | URL of the Splunk instance | 
**source_type** | **str** | Source type to override [Sysdig standard data type to source type mapping](https://docs.sysdig.com/en/forward-splunk#reference-data-categories-mapped-to-source-types) | [optional] 
**index** | **str** | index to send data to. If unspecified, it will be used the index specified on the HTTP Event Collector configuration on Splunk | [optional] 
**is_insecure** | **bool** | Skip TLS certificate verification | [optional] 
**certificate_id** | **int** | ID of a certificate stored in Sysdig&#39;s [Certificates Management tool](#tag/Certificates). Note that the RFC 5425 (TLS) protocol is required for you to see this field | [optional] 
**token** | **str** | HTTP Event Collector Token | 

## Example

```python
from sysdig_client.models.splunk_create_connection_info import SplunkCreateConnectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SplunkCreateConnectionInfo from a JSON string
splunk_create_connection_info_instance = SplunkCreateConnectionInfo.from_json(json)
# print the JSON string representation of the object
print(SplunkCreateConnectionInfo.to_json())

# convert the object into a dict
splunk_create_connection_info_dict = splunk_create_connection_info_instance.to_dict()
# create an instance of SplunkCreateConnectionInfo from a dict
splunk_create_connection_info_from_dict = SplunkCreateConnectionInfo.from_dict(splunk_create_connection_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


