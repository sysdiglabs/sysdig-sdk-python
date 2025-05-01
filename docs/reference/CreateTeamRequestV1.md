# CreateTeamRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the team. It must be unique. | 
**description** | **str** | A longer description of the team explaining what is it used for. | [optional] 
**is_default_team** | **bool** | Specifies if the team is the default team. The default team is used to automatically assign new users to a team. | [optional] 
**standard_team_role** | [**TeamRoleV1**](TeamRoleV1.md) | The standard team role assigned by default to users added to this team. **Mutually exclusive with customTeamRoleId**.\\ \\ *ROLE_TEAM_SERVICE_MANAGER is only supported in Secure.*  | [optional] 
**custom_team_role_id** | **int** | The custom team role assigned by default to users added to this team. **Mutually exclusive with standardTeamRoleId**.  | [optional] 
**product** | [**Product**](Product.md) | The product to which the team is assigned to. Teams can only be part of a single product at a time. | 
**ui_settings** | [**UiSettingsV1**](UiSettingsV1.md) |  | [optional] 
**is_all_zones** | **bool** | **True** if the users that are members of this team have access to all zones. **Mutually exclusive with zoneIds**.\\ \\ _Only supported in Secure features._  | [optional] 
**zone_ids** | **List[int]** | The list of zones that users assigned to this team will have access to. **Mutually exclusive with allZones**.\\ \\ _Only supported in Secure features._  | [optional] 
**scopes** | [**List[ScopeV1]**](ScopeV1.md) | Scopes is a list of different scope types and filter values that will be applied to resources when accessed through the team.  | [optional] 
**additional_team_permissions** | [**AdditionalTeamPermissionsV1**](AdditionalTeamPermissionsV1.md) |  | [optional] 

## Example

```python
from sysdig_client.models.create_team_request_v1 import CreateTeamRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTeamRequestV1 from a JSON string
create_team_request_v1_instance = CreateTeamRequestV1.from_json(json)
# print the JSON string representation of the object
print(CreateTeamRequestV1.to_json())

# convert the object into a dict
create_team_request_v1_dict = create_team_request_v1_instance.to_dict()
# create an instance of CreateTeamRequestV1 from a dict
create_team_request_v1_from_dict = CreateTeamRequestV1.from_dict(create_team_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


