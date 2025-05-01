# DenyPkg

Predicate expressing \"any of these packages is present\". 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**extra** | [**DenyPkgExtra**](DenyPkgExtra.md) |  | 

## Example

```python
from sysdig_client.models.deny_pkg import DenyPkg

# TODO update the JSON string below
json = "{}"
# create an instance of DenyPkg from a JSON string
deny_pkg_instance = DenyPkg.from_json(json)
# print the JSON string representation of the object
print(DenyPkg.to_json())

# convert the object into a dict
deny_pkg_dict = deny_pkg_instance.to_dict()
# create an instance of DenyPkg from a dict
deny_pkg_from_dict = DenyPkg.from_dict(deny_pkg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


