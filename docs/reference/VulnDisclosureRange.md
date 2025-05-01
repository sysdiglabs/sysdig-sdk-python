# VulnDisclosureRange

The start and end dates (inclusive) when vulnerabilities were disclosed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**extra** | [**VulnDisclosureRangeExtra**](VulnDisclosureRangeExtra.md) |  | 

## Example

```python
from sysdig_client.models.vuln_disclosure_range import VulnDisclosureRange

# TODO update the JSON string below
json = "{}"
# create an instance of VulnDisclosureRange from a JSON string
vuln_disclosure_range_instance = VulnDisclosureRange.from_json(json)
# print the JSON string representation of the object
print(VulnDisclosureRange.to_json())

# convert the object into a dict
vuln_disclosure_range_dict = vuln_disclosure_range_instance.to_dict()
# create an instance of VulnDisclosureRange from a dict
vuln_disclosure_range_from_dict = VulnDisclosureRange.from_dict(vuln_disclosure_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


