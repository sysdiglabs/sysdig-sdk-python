# GroupMappingSettingsV1

The request to save group mapping settings. Currently settings for conflict resolution strategies are supported. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**no_mapping_strategy** | **str** | Strategy for handling no mappings.  | 
**different_roles_same_team_strategy** | **str** | Strategy for handling different roles on the same team.  | 
**no_mappings_error_redirect_url** | **str** | Redirect URL when NO_MAPPINGS_ERROR_REDIRECT is selected.  | [optional] 

## Example

```python
from sysdig_client.models.group_mapping_settings_v1 import GroupMappingSettingsV1

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMappingSettingsV1 from a JSON string
group_mapping_settings_v1_instance = GroupMappingSettingsV1.from_json(json)
# print the JSON string representation of the object
print(GroupMappingSettingsV1.to_json())

# convert the object into a dict
group_mapping_settings_v1_dict = group_mapping_settings_v1_instance.to_dict()
# create an instance of GroupMappingSettingsV1 from a dict
group_mapping_settings_v1_from_dict = GroupMappingSettingsV1.from_dict(group_mapping_settings_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


