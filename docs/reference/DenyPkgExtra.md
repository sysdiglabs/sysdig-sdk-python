# DenyPkgExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**packages** | [**List[DenyPkgExtraPackagesInner]**](DenyPkgExtraPackagesInner.md) |  | 

## Example

```python
from sysdig_client.models.deny_pkg_extra import DenyPkgExtra

# TODO update the JSON string below
json = "{}"
# create an instance of DenyPkgExtra from a JSON string
deny_pkg_extra_instance = DenyPkgExtra.from_json(json)
# print the JSON string representation of the object
print(DenyPkgExtra.to_json())

# convert the object into a dict
deny_pkg_extra_dict = deny_pkg_extra_instance.to_dict()
# create an instance of DenyPkgExtra from a dict
deny_pkg_extra_from_dict = DenyPkgExtra.from_dict(deny_pkg_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


