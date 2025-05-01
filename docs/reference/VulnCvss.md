# VulnCvss

Predicate expressing \"the Vulnerability CVSS Score is higher than <value>\" 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**extra** | [**VulnCvssExtra**](VulnCvssExtra.md) |  | 

## Example

```python
from sysdig_client.models.vuln_cvss import VulnCvss

# TODO update the JSON string below
json = "{}"
# create an instance of VulnCvss from a JSON string
vuln_cvss_instance = VulnCvss.from_json(json)
# print the JSON string representation of the object
print(VulnCvss.to_json())

# convert the object into a dict
vuln_cvss_dict = vuln_cvss_instance.to_dict()
# create an instance of VulnCvss from a dict
vuln_cvss_from_dict = VulnCvss.from_dict(vuln_cvss_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


