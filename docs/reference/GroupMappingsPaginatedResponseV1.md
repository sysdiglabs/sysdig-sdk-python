# GroupMappingsPaginatedResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**OffsetPaginatedResponsePage**](OffsetPaginatedResponsePage.md) |  | [optional] 
**data** | [**List[GroupMappingResponseV1]**](GroupMappingResponseV1.md) |  | [optional] 

## Example

```python
from sysdig_client.models.group_mappings_paginated_response_v1 import GroupMappingsPaginatedResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMappingsPaginatedResponseV1 from a JSON string
group_mappings_paginated_response_v1_instance = GroupMappingsPaginatedResponseV1.from_json(json)
# print the JSON string representation of the object
print(GroupMappingsPaginatedResponseV1.to_json())

# convert the object into a dict
group_mappings_paginated_response_v1_dict = group_mappings_paginated_response_v1_instance.to_dict()
# create an instance of GroupMappingsPaginatedResponseV1 from a dict
group_mappings_paginated_response_v1_from_dict = GroupMappingsPaginatedResponseV1.from_dict(group_mappings_paginated_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


