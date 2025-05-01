# DenyPkgExtraPackagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Package name | 
**version** | **str** | Package version | [optional] 

## Example

```python
from sysdig_client.models.deny_pkg_extra_packages_inner import DenyPkgExtraPackagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DenyPkgExtraPackagesInner from a JSON string
deny_pkg_extra_packages_inner_instance = DenyPkgExtraPackagesInner.from_json(json)
# print the JSON string representation of the object
print(DenyPkgExtraPackagesInner.to_json())

# convert the object into a dict
deny_pkg_extra_packages_inner_dict = deny_pkg_extra_packages_inner_instance.to_dict()
# create an instance of DenyPkgExtraPackagesInner from a dict
deny_pkg_extra_packages_inner_from_dict = DenyPkgExtraPackagesInner.from_dict(deny_pkg_extra_packages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


