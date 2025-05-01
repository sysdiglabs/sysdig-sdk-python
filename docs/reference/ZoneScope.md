# ZoneScope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |   | [optional] 
**target_type** | **str** | The target type of the Scope | 
**rules** | **str** | Scoping rules to be applied | [optional] 

## Example

```python
from sysdig_client.models.zone_scope import ZoneScope

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneScope from a JSON string
zone_scope_instance = ZoneScope.from_json(json)
# print the JSON string representation of the object
print(ZoneScope.to_json())

# convert the object into a dict
zone_scope_dict = zone_scope_instance.to_dict()
# create an instance of ZoneScope from a dict
zone_scope_from_dict = ZoneScope.from_dict(zone_scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


