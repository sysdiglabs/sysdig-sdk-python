# RoleResponseV1

Create role response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |   | [optional] 
**description** | **str** | Describes the role | [optional] 
**monitor_permissions** | **List[str]** | Set of Monitor permissions assigned to the role.  Check GET /platform/v1/permissions to obtain the list of available values.  | [optional] 
**secure_permissions** | **List[str]** | Set of Secure permissions assigned to the role.  Check GET /platform/v1/permissions to obtain the list of available values.  | [optional] 
**name** | **str** | The display name of the role | [optional] 

## Example

```python
from sysdig_client.models.role_response_v1 import RoleResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of RoleResponseV1 from a JSON string
role_response_v1_instance = RoleResponseV1.from_json(json)
# print the JSON string representation of the object
print(RoleResponseV1.to_json())

# convert the object into a dict
role_response_v1_dict = role_response_v1_instance.to_dict()
# create an instance of RoleResponseV1 from a dict
role_response_v1_from_dict = RoleResponseV1.from_dict(role_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


