# VulnCvssEqualsExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | The threshold for equality comparison with the CVSS Score. | [optional] 

## Example

```python
from sysdig_client.models.vuln_cvss_equals_extra import VulnCvssEqualsExtra

# TODO update the JSON string below
json = "{}"
# create an instance of VulnCvssEqualsExtra from a JSON string
vuln_cvss_equals_extra_instance = VulnCvssEqualsExtra.from_json(json)
# print the JSON string representation of the object
print(VulnCvssEqualsExtra.to_json())

# convert the object into a dict
vuln_cvss_equals_extra_dict = vuln_cvss_equals_extra_instance.to_dict()
# create an instance of VulnCvssEqualsExtra from a dict
vuln_cvss_equals_extra_from_dict = VulnCvssEqualsExtra.from_dict(vuln_cvss_equals_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


