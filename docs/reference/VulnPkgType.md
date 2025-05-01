# VulnPkgType

Predicate expressing \"the Vulnerability is related to a package of <type>\". 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**extra** | [**VulnPkgTypeExtra**](VulnPkgTypeExtra.md) |  | 

## Example

```python
from sysdig_client.models.vuln_pkg_type import VulnPkgType

# TODO update the JSON string below
json = "{}"
# create an instance of VulnPkgType from a JSON string
vuln_pkg_type_instance = VulnPkgType.from_json(json)
# print the JSON string representation of the object
print(VulnPkgType.to_json())

# convert the object into a dict
vuln_pkg_type_dict = vuln_pkg_type_instance.to_dict()
# create an instance of VulnPkgType from a dict
vuln_pkg_type_from_dict = VulnPkgType.from_dict(vuln_pkg_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


