# VulnDisclosureRangeExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | The start date (inclusive) of disclosed vulnerabilities. | [optional] 
**end_date** | **date** | The end date (inclusive) of disclosed vulnerabilities. | [optional] 

## Example

```python
from sysdig_client.models.vuln_disclosure_range_extra import VulnDisclosureRangeExtra

# TODO update the JSON string below
json = "{}"
# create an instance of VulnDisclosureRangeExtra from a JSON string
vuln_disclosure_range_extra_instance = VulnDisclosureRangeExtra.from_json(json)
# print the JSON string representation of the object
print(VulnDisclosureRangeExtra.to_json())

# convert the object into a dict
vuln_disclosure_range_extra_dict = vuln_disclosure_range_extra_instance.to_dict()
# create an instance of VulnDisclosureRangeExtra from a dict
vuln_disclosure_range_extra_from_dict = VulnDisclosureRangeExtra.from_dict(vuln_disclosure_range_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


