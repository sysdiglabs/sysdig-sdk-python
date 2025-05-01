# HostNameContains


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_type** | **str** | Matcher type to apply | [optional] 
**context_value** | **str** | Value to match | [optional] 

## Example

```python
from sysdig_client.models.host_name_contains import HostNameContains

# TODO update the JSON string below
json = "{}"
# create an instance of HostNameContains from a JSON string
host_name_contains_instance = HostNameContains.from_json(json)
# print the JSON string representation of the object
print(HostNameContains.to_json())

# convert the object into a dict
host_name_contains_dict = host_name_contains_instance.to_dict()
# create an instance of HostNameContains from a dict
host_name_contains_from_dict = HostNameContains.from_dict(host_name_contains_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


