# CreateZoneScopeRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_type** | **str** | The target type of the Scope | 
**rules** | **str** | Scoping rules to be applied | [optional] 

## Example

```python
from sysdig_client.models.create_zone_scope_request_v1 import CreateZoneScopeRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of CreateZoneScopeRequestV1 from a JSON string
create_zone_scope_request_v1_instance = CreateZoneScopeRequestV1.from_json(json)
# print the JSON string representation of the object
print(CreateZoneScopeRequestV1.to_json())

# convert the object into a dict
create_zone_scope_request_v1_dict = create_zone_scope_request_v1_instance.to_dict()
# create an instance of CreateZoneScopeRequestV1 from a dict
create_zone_scope_request_v1_from_dict = CreateZoneScopeRequestV1.from_dict(create_zone_scope_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


