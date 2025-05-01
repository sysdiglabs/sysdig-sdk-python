# GetPermissionsResponseV1

Permissions response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**List[PermissionV1]**](PermissionV1.md) | Set of permissions  | [optional] 
**total** | **int** | Total number of permissions | [optional] 

## Example

```python
from sysdig_client.models.get_permissions_response_v1 import GetPermissionsResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of GetPermissionsResponseV1 from a JSON string
get_permissions_response_v1_instance = GetPermissionsResponseV1.from_json(json)
# print the JSON string representation of the object
print(GetPermissionsResponseV1.to_json())

# convert the object into a dict
get_permissions_response_v1_dict = get_permissions_response_v1_instance.to_dict()
# create an instance of GetPermissionsResponseV1 from a dict
get_permissions_response_v1_from_dict = GetPermissionsResponseV1.from_dict(get_permissions_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


