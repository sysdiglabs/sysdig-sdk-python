# MicrosoftSentinelUpdateConnectionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | Log Analytics workspace ID | 
**secret** | **str** | Log analytics primary key | [optional] 

## Example

```python
from sysdig_client.models.microsoft_sentinel_update_connection_info import MicrosoftSentinelUpdateConnectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftSentinelUpdateConnectionInfo from a JSON string
microsoft_sentinel_update_connection_info_instance = MicrosoftSentinelUpdateConnectionInfo.from_json(json)
# print the JSON string representation of the object
print(MicrosoftSentinelUpdateConnectionInfo.to_json())

# convert the object into a dict
microsoft_sentinel_update_connection_info_dict = microsoft_sentinel_update_connection_info_instance.to_dict()
# create an instance of MicrosoftSentinelUpdateConnectionInfo from a dict
microsoft_sentinel_update_connection_info_from_dict = MicrosoftSentinelUpdateConnectionInfo.from_dict(microsoft_sentinel_update_connection_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


