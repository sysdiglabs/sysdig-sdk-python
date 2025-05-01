# TeamResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |   | [optional] 
**name** | **str** | The name of the team. It must be unique. | [optional] 
**description** | **str** | A description of the team explaining what is it used for. | [optional] 
**is_immutable_team** | **bool** | Specifies if the team is immutable. This is true if the team was created by the system with full access. It cannot be modified. | [optional] 
**is_default_team** | **bool** | Specifies if the team is the default team. The default team is used to automatically assign new users to a team. | [optional] 
**standard_team_role** | [**TeamRoleV1**](TeamRoleV1.md) | The standard team role assigned by default to users added to this team. Mutually exclusive with &#39;customTeamRoleId&#39;.  | [optional] 
**custom_team_role_id** | **int** | The custom team role assigned by default to users added to this team. Mutually exclusive with &#39;standardTeamRoleId&#39;.  | [optional] 
**product** | [**Product**](Product.md) | The product to which the team is assigned to. | [optional] 
**ui_settings** | [**UiSettingsV1**](UiSettingsV1.md) |  | [optional] 
**is_all_zones** | **bool** | &#39;True&#39; if the users belonging to this team have access to all zones. Mutually exclusive with &#39;zoneIds&#39;.  | [optional] 
**zone_ids** | **List[int]** | The list of zones that users assigned to this team will have access to. Mutually exclusive with &#39;allZones&#39;.  | [optional] 
**scopes** | [**List[ScopeV1]**](ScopeV1.md) | The scopes available to the users of this team. | [optional] 
**additional_team_permissions** | [**AdditionalTeamPermissionsV1**](AdditionalTeamPermissionsV1.md) |  | [optional] 
**date_created** | **datetime** | The date (in ISO 8601 format) when this team was created. | [optional] 
**last_updated** | **datetime** | The date (in ISO 8601 format) when this team was last updated. | [optional] 
**version** | **int** |   | [optional] 

## Example

```python
from sysdig_client.models.team_response_v1 import TeamResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of TeamResponseV1 from a JSON string
team_response_v1_instance = TeamResponseV1.from_json(json)
# print the JSON string representation of the object
print(TeamResponseV1.to_json())

# convert the object into a dict
team_response_v1_dict = team_response_v1_instance.to_dict()
# create an instance of TeamResponseV1 from a dict
team_response_v1_from_dict = TeamResponseV1.from_dict(team_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


