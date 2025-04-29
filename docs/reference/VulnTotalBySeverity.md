# VulnTotalBySeverity

total vulnerabilities by severity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**critical** | **int** | number of critical vulnerabilities | [optional] 
**high** | **int** | number of high severity vulnerabilities | [optional] 
**medium** | **int** | number of medium severity vulnerabilities | [optional] 
**low** | **int** | number of low severity vulnerabilities | [optional] 
**negligible** | **int** | number of negligible severity vulnerabilities | [optional] 

## Example

```python
from sysdig_client.models.vuln_total_by_severity import VulnTotalBySeverity

# TODO update the JSON string below
json = "{}"
# create an instance of VulnTotalBySeverity from a JSON string
vuln_total_by_severity_instance = VulnTotalBySeverity.from_json(json)
# print the JSON string representation of the object
print(VulnTotalBySeverity.to_json())

# convert the object into a dict
vuln_total_by_severity_dict = vuln_total_by_severity_instance.to_dict()
# create an instance of VulnTotalBySeverity from a dict
vuln_total_by_severity_from_dict = VulnTotalBySeverity.from_dict(vuln_total_by_severity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


