# VulnCvssExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | The threshold for greater-than-or-equal comparison with CVSS Score. | [optional] 

## Example

```python
from sysdig_client.models.vuln_cvss_extra import VulnCvssExtra

# TODO update the JSON string below
json = "{}"
# create an instance of VulnCvssExtra from a JSON string
vuln_cvss_extra_instance = VulnCvssExtra.from_json(json)
# print the JSON string representation of the object
print(VulnCvssExtra.to_json())

# convert the object into a dict
vuln_cvss_extra_dict = vuln_cvss_extra_instance.to_dict()
# create an instance of VulnCvssExtra from a dict
vuln_cvss_extra_from_dict = VulnCvssExtra.from_dict(vuln_cvss_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


