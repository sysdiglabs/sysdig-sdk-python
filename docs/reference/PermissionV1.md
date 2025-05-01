# PermissionV1

Permission to perform an action on the Sysdig platform.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Permission Authority.  | [optional] 
**description** | **str** | Permission description.  | [optional] 
**products** | **List[str]** | Specifies the Sysdig product the permission applies to (Secure &#x3D; SDS; Monitor &#x3D; SDC).  | [optional] 
**dependencies** | **List[str]** | List of permissions that this permission depends on.  | [optional] 

## Example

```python
from sysdig_client.models.permission_v1 import PermissionV1

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionV1 from a JSON string
permission_v1_instance = PermissionV1.from_json(json)
# print the JSON string representation of the object
print(PermissionV1.to_json())

# convert the object into a dict
permission_v1_dict = permission_v1_instance.to_dict()
# create an instance of PermissionV1 from a dict
permission_v1_from_dict = PermissionV1.from_dict(permission_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


