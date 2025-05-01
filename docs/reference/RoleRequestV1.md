# RoleRequestV1

Create or update role request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Describes the role | [optional] 
**monitor_permissions** | **List[str]** | Set of Monitor permissions assigned to the role.  Check GET /platform/v1/permissions to obtain the list of available values.  | [optional] 
**secure_permissions** | **List[str]** | Set of Secure permissions assigned to the role.  Check GET /platform/v1/permissions to obtain the list of available values.  | [optional] 
**name** | **str** | The display name of the role | 

## Example

```python
from sysdig_client.models.role_request_v1 import RoleRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of RoleRequestV1 from a JSON string
role_request_v1_instance = RoleRequestV1.from_json(json)
# print the JSON string representation of the object
print(RoleRequestV1.to_json())

# convert the object into a dict
role_request_v1_dict = role_request_v1_instance.to_dict()
# create an instance of RoleRequestV1 from a dict
role_request_v1_from_dict = RoleRequestV1.from_dict(role_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


