# GetTeamsPaginatedResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**OffsetPaginatedResponsePage**](OffsetPaginatedResponsePage.md) |  | [optional] 
**data** | [**List[TeamResponseV1]**](TeamResponseV1.md) |  | [optional] 

## Example

```python
from sysdig_client.models.get_teams_paginated_response_v1 import GetTeamsPaginatedResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of GetTeamsPaginatedResponseV1 from a JSON string
get_teams_paginated_response_v1_instance = GetTeamsPaginatedResponseV1.from_json(json)
# print the JSON string representation of the object
print(GetTeamsPaginatedResponseV1.to_json())

# convert the object into a dict
get_teams_paginated_response_v1_dict = get_teams_paginated_response_v1_instance.to_dict()
# create an instance of GetTeamsPaginatedResponseV1 from a dict
get_teams_paginated_response_v1_from_dict = GetTeamsPaginatedResponseV1.from_dict(get_teams_paginated_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


