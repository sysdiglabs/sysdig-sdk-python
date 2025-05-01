# ScopeV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ScopeTypeV1**](ScopeTypeV1.md) |  | 
**expression** | **str** |  | 

## Example

```python
from sysdig_client.models.scope_v1 import ScopeV1

# TODO update the JSON string below
json = "{}"
# create an instance of ScopeV1 from a JSON string
scope_v1_instance = ScopeV1.from_json(json)
# print the JSON string representation of the object
print(ScopeV1.to_json())

# convert the object into a dict
scope_v1_dict = scope_v1_instance.to_dict()
# create an instance of ScopeV1 from a dict
scope_v1_from_dict = ScopeV1.from_dict(scope_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


