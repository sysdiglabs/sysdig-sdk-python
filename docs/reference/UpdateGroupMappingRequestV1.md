# UpdateGroupMappingRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_name** | **str** | The group name matching the external provider name. | 
**standard_team_role** | [**TeamRoleV1**](TeamRoleV1.md) | The standard team role assigned for the user in this team. **Mutually exclusive with customTeamRoleId**.  | [optional] 
**custom_team_role_id** | **int** | The custom team role ID assigned for the user in this team. **Mutually exclusive with standardTeamRole**.  | [optional] 
**is_admin** | **bool** | Flag that indicates if the group is an admin group. | 
**team_map** | [**TeamMapV1**](TeamMapV1.md) |  | 
**weight** | **int** | The weight of the group mapping that is used to determine the priority - a lower number has higher priority. | [default to 32767]

## Example

```python
from sysdig_client.models.update_group_mapping_request_v1 import UpdateGroupMappingRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGroupMappingRequestV1 from a JSON string
update_group_mapping_request_v1_instance = UpdateGroupMappingRequestV1.from_json(json)
# print the JSON string representation of the object
print(UpdateGroupMappingRequestV1.to_json())

# convert the object into a dict
update_group_mapping_request_v1_dict = update_group_mapping_request_v1_instance.to_dict()
# create an instance of UpdateGroupMappingRequestV1 from a dict
update_group_mapping_request_v1_from_dict = UpdateGroupMappingRequestV1.from_dict(update_group_mapping_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


