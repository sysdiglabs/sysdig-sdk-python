# SaveTeamUserRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**standard_team_role** | [**TeamRoleV1**](TeamRoleV1.md) | The standard team role assigned for the user in this team. **Mutually exclusive with customTeamRoleId**.\\ \\ *ROLE_TEAM_SERVICE_MANAGER is only supported in Secure.*  | [optional] 
**custom_team_role_id** | **int** | The custom team role ID assigned for the user in this team. **Mutually exclusive with standardTeamRole**.  | [optional] 

## Example

```python
from sysdig_client.models.save_team_user_request_v1 import SaveTeamUserRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of SaveTeamUserRequestV1 from a JSON string
save_team_user_request_v1_instance = SaveTeamUserRequestV1.from_json(json)
# print the JSON string representation of the object
print(SaveTeamUserRequestV1.to_json())

# convert the object into a dict
save_team_user_request_v1_dict = save_team_user_request_v1_instance.to_dict()
# create an instance of SaveTeamUserRequestV1 from a dict
save_team_user_request_v1_from_dict = SaveTeamUserRequestV1.from_dict(save_team_user_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


