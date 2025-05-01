# VulnSeverityEquals

Predicate expressing \"the Vulnerability Severity is exactly <level>\". 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**extra** | [**VulnSeverityExtra**](VulnSeverityExtra.md) |  | 

## Example

```python
from sysdig_client.models.vuln_severity_equals import VulnSeverityEquals

# TODO update the JSON string below
json = "{}"
# create an instance of VulnSeverityEquals from a JSON string
vuln_severity_equals_instance = VulnSeverityEquals.from_json(json)
# print the JSON string representation of the object
print(VulnSeverityEquals.to_json())

# convert the object into a dict
vuln_severity_equals_dict = vuln_severity_equals_instance.to_dict()
# create an instance of VulnSeverityEquals from a dict
vuln_severity_equals_from_dict = VulnSeverityEquals.from_dict(vuln_severity_equals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


