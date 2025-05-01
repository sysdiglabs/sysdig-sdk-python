# VulnCvssEquals

Predicate expressing \"the Vulnerability CVSS Score is exactly equal to <value>\" 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**extra** | [**VulnCvssEqualsExtra**](VulnCvssEqualsExtra.md) |  | 

## Example

```python
from sysdig_client.models.vuln_cvss_equals import VulnCvssEquals

# TODO update the JSON string below
json = "{}"
# create an instance of VulnCvssEquals from a JSON string
vuln_cvss_equals_instance = VulnCvssEquals.from_json(json)
# print the JSON string representation of the object
print(VulnCvssEquals.to_json())

# convert the object into a dict
vuln_cvss_equals_dict = vuln_cvss_equals_instance.to_dict()
# create an instance of VulnCvssEquals from a dict
vuln_cvss_equals_from_dict = VulnCvssEquals.from_dict(vuln_cvss_equals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


