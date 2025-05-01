# VulnPkgTypeExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pkg_type** | **str** | The package type, either OS or non-OS. There is no enforcement on the value for future extensibility.  | 

## Example

```python
from sysdig_client.models.vuln_pkg_type_extra import VulnPkgTypeExtra

# TODO update the JSON string below
json = "{}"
# create an instance of VulnPkgTypeExtra from a JSON string
vuln_pkg_type_extra_instance = VulnPkgTypeExtra.from_json(json)
# print the JSON string representation of the object
print(VulnPkgTypeExtra.to_json())

# convert the object into a dict
vuln_pkg_type_extra_dict = vuln_pkg_type_extra_instance.to_dict()
# create an instance of VulnPkgTypeExtra from a dict
vuln_pkg_type_extra_from_dict = VulnPkgTypeExtra.from_dict(vuln_pkg_type_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


