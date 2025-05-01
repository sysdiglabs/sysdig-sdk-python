# CreateGroupMappingRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_name** | **str** | The group name matching the external provider name. | 
**standard_team_role** | [**TeamRoleV1**](TeamRoleV1.md) | The standard team role assigned for the user in this team. **Mutually exclusive with customTeamRoleId**.  | [optional] 
**custom_team_role_id** | **int** | The custom team role ID assigned for the user in this team. **Mutually exclusive with standardTeamRole**.  | [optional] 
**is_admin** | **bool** | Flag that indicates if the group is an admin group. | [optional] 
**team_map** | [**TeamMapV1**](TeamMapV1.md) |  | 
**weight** | **int** | The weight of the group mapping is used to determine the priority - a lower number has higher priority. | [optional] [default to 32767]

## Example

```python
from sysdig_client.models.create_group_mapping_request_v1 import CreateGroupMappingRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGroupMappingRequestV1 from a JSON string
create_group_mapping_request_v1_instance = CreateGroupMappingRequestV1.from_json(json)
# print the JSON string representation of the object
print(CreateGroupMappingRequestV1.to_json())

# convert the object into a dict
create_group_mapping_request_v1_dict = create_group_mapping_request_v1_instance.to_dict()
# create an instance of CreateGroupMappingRequestV1 from a dict
create_group_mapping_request_v1_from_dict = CreateGroupMappingRequestV1.from_dict(create_group_mapping_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


