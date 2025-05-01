# TeamUserResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **int** |   | [optional] 
**user_id** | **int** |   | [optional] 
**standard_team_role** | [**TeamRoleV1**](TeamRoleV1.md) |  | [optional] 
**custom_team_role_id** | **int** |   | [optional] 

## Example

```python
from sysdig_client.models.team_user_response_v1 import TeamUserResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of TeamUserResponseV1 from a JSON string
team_user_response_v1_instance = TeamUserResponseV1.from_json(json)
# print the JSON string representation of the object
print(TeamUserResponseV1.to_json())

# convert the object into a dict
team_user_response_v1_dict = team_user_response_v1_instance.to_dict()
# create an instance of TeamUserResponseV1 from a dict
team_user_response_v1_from_dict = TeamUserResponseV1.from_dict(team_user_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


