# EntryPointV1

The page you see after logging into Sysdig UI. It is defined by a Module and a Selection. **The Entry Point is not supported in Sysdig Secure.** 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module** | [**EntryPointModuleV1**](EntryPointModuleV1.md) |  | [optional] 
**selection** | **str** | The selection is the specific page within the Module, usually defined by the resource ID. It is supported only supported by **Dashboards** and **DashboardTemplates** Modules.  | [optional] 

## Example

```python
from sysdig_client.models.entry_point_v1 import EntryPointV1

# TODO update the JSON string below
json = "{}"
# create an instance of EntryPointV1 from a JSON string
entry_point_v1_instance = EntryPointV1.from_json(json)
# print the JSON string representation of the object
print(EntryPointV1.to_json())

# convert the object into a dict
entry_point_v1_dict = entry_point_v1_instance.to_dict()
# create an instance of EntryPointV1 from a dict
entry_point_v1_from_dict = EntryPointV1.from_dict(entry_point_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


