# BaseConnectionInfoMicrosoftSentinel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | Log Analytics workspace ID | 

## Example

```python
from sysdig_client.models.base_connection_info_microsoft_sentinel import BaseConnectionInfoMicrosoftSentinel

# TODO update the JSON string below
json = "{}"
# create an instance of BaseConnectionInfoMicrosoftSentinel from a JSON string
base_connection_info_microsoft_sentinel_instance = BaseConnectionInfoMicrosoftSentinel.from_json(json)
# print the JSON string representation of the object
print(BaseConnectionInfoMicrosoftSentinel.to_json())

# convert the object into a dict
base_connection_info_microsoft_sentinel_dict = base_connection_info_microsoft_sentinel_instance.to_dict()
# create an instance of BaseConnectionInfoMicrosoftSentinel from a dict
base_connection_info_microsoft_sentinel_from_dict = BaseConnectionInfoMicrosoftSentinel.from_dict(base_connection_info_microsoft_sentinel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


