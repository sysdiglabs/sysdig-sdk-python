# PrivateConnectionInfoMicrosoftSentinel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | **str** | Log analytics primary key | [optional] 

## Example

```python
from sysdig_client.models.private_connection_info_microsoft_sentinel import PrivateConnectionInfoMicrosoftSentinel

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateConnectionInfoMicrosoftSentinel from a JSON string
private_connection_info_microsoft_sentinel_instance = PrivateConnectionInfoMicrosoftSentinel.from_json(json)
# print the JSON string representation of the object
print(PrivateConnectionInfoMicrosoftSentinel.to_json())

# convert the object into a dict
private_connection_info_microsoft_sentinel_dict = private_connection_info_microsoft_sentinel_instance.to_dict()
# create an instance of PrivateConnectionInfoMicrosoftSentinel from a dict
private_connection_info_microsoft_sentinel_from_dict = PrivateConnectionInfoMicrosoftSentinel.from_dict(private_connection_info_microsoft_sentinel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


