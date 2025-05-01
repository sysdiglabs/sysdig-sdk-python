# HostName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_type** | **str** | Matcher type to apply | [optional] 
**context_value** | **str** | Value to match | [optional] 

## Example

```python
from sysdig_client.models.host_name import HostName

# TODO update the JSON string below
json = "{}"
# create an instance of HostName from a JSON string
host_name_instance = HostName.from_json(json)
# print the JSON string representation of the object
print(HostName.to_json())

# convert the object into a dict
host_name_dict = host_name_instance.to_dict()
# create an instance of HostName from a dict
host_name_from_dict = HostName.from_dict(host_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


