# GroupMappingResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |   | [optional] 
**group_name** | **str** | The group name matching the external provider name. | [optional] 
**standard_team_role** | [**TeamRoleV1**](TeamRoleV1.md) | The standard team role assigned for the user in this team. **Mutually exclusive with customTeamRoleId**.  | [optional] 
**custom_team_role_id** | **int** | The custom team role ID assigned for the user in this team. **Mutually exclusive with standardTeamRole**.  | [optional] 
**is_admin** | **bool** | Flag that indicates if the group is an admin group. | [optional] 
**team_map** | [**TeamMapV1**](TeamMapV1.md) |  | [optional] 
**weight** | **int** | The weight of the group mapping that is used to determine the priority - a lower number has higher priority. | [optional] 
**date_created** | **datetime** | The date in which this group mapping was created in ISO 8601 format. | [optional] 
**last_updated** | **datetime** | The date in which this group mapping was last updated in ISO 8601 format. | [optional] 

## Example

```python
from sysdig_client.models.group_mapping_response_v1 import GroupMappingResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMappingResponseV1 from a JSON string
group_mapping_response_v1_instance = GroupMappingResponseV1.from_json(json)
# print the JSON string representation of the object
print(GroupMappingResponseV1.to_json())

# convert the object into a dict
group_mapping_response_v1_dict = group_mapping_response_v1_instance.to_dict()
# create an instance of GroupMappingResponseV1 from a dict
group_mapping_response_v1_from_dict = GroupMappingResponseV1.from_dict(group_mapping_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


