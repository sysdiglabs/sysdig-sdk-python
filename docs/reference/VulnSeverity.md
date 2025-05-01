# VulnSeverity

Predicate expressing \"the Vulnerability Severity is <level> or higher\". 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**extra** | [**VulnSeverityExtra**](VulnSeverityExtra.md) |  | 

## Example

```python
from sysdig_client.models.vuln_severity import VulnSeverity

# TODO update the JSON string below
json = "{}"
# create an instance of VulnSeverity from a JSON string
vuln_severity_instance = VulnSeverity.from_json(json)
# print the JSON string representation of the object
print(VulnSeverity.to_json())

# convert the object into a dict
vuln_severity_dict = vuln_severity_instance.to_dict()
# create an instance of VulnSeverity from a dict
vuln_severity_from_dict = VulnSeverity.from_dict(vuln_severity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


