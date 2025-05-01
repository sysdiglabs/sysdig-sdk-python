# GetTeamUsersPaginatedResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**OffsetPaginatedResponsePage**](OffsetPaginatedResponsePage.md) |  | [optional] 
**data** | [**List[TeamUserResponseV1]**](TeamUserResponseV1.md) |  | [optional] 

## Example

```python
from sysdig_client.models.get_team_users_paginated_response_v1 import GetTeamUsersPaginatedResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of GetTeamUsersPaginatedResponseV1 from a JSON string
get_team_users_paginated_response_v1_instance = GetTeamUsersPaginatedResponseV1.from_json(json)
# print the JSON string representation of the object
print(GetTeamUsersPaginatedResponseV1.to_json())

# convert the object into a dict
get_team_users_paginated_response_v1_dict = get_team_users_paginated_response_v1_instance.to_dict()
# create an instance of GetTeamUsersPaginatedResponseV1 from a dict
get_team_users_paginated_response_v1_from_dict = GetTeamUsersPaginatedResponseV1.from_dict(get_team_users_paginated_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


