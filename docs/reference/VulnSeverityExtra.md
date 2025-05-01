# VulnSeverityExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** |  | [optional] 

## Example

```python
from sysdig_client.models.vuln_severity_extra import VulnSeverityExtra

# TODO update the JSON string below
json = "{}"
# create an instance of VulnSeverityExtra from a JSON string
vuln_severity_extra_instance = VulnSeverityExtra.from_json(json)
# print the JSON string representation of the object
print(VulnSeverityExtra.to_json())

# convert the object into a dict
vuln_severity_extra_dict = vuln_severity_extra_instance.to_dict()
# create an instance of VulnSeverityExtra from a dict
vuln_severity_extra_from_dict = VulnSeverityExtra.from_dict(vuln_severity_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


