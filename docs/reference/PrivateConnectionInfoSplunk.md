# PrivateConnectionInfoSplunk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | HTTP Event Collector Token | [optional] 

## Example

```python
from sysdig_client.models.private_connection_info_splunk import PrivateConnectionInfoSplunk

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateConnectionInfoSplunk from a JSON string
private_connection_info_splunk_instance = PrivateConnectionInfoSplunk.from_json(json)
# print the JSON string representation of the object
print(PrivateConnectionInfoSplunk.to_json())

# convert the object into a dict
private_connection_info_splunk_dict = private_connection_info_splunk_instance.to_dict()
# create an instance of PrivateConnectionInfoSplunk from a dict
private_connection_info_splunk_from_dict = PrivateConnectionInfoSplunk.from_dict(private_connection_info_splunk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


