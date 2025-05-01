# VulnEpssPercentileGte

The EPSS percentile score that is greater than or equal to the specified value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**extra** | [**VulnEpssPercentileGteExtra**](VulnEpssPercentileGteExtra.md) |  | 

## Example

```python
from sysdig_client.models.vuln_epss_percentile_gte import VulnEpssPercentileGte

# TODO update the JSON string below
json = "{}"
# create an instance of VulnEpssPercentileGte from a JSON string
vuln_epss_percentile_gte_instance = VulnEpssPercentileGte.from_json(json)
# print the JSON string representation of the object
print(VulnEpssPercentileGte.to_json())

# convert the object into a dict
vuln_epss_percentile_gte_dict = vuln_epss_percentile_gte_instance.to_dict()
# create an instance of VulnEpssPercentileGte from a dict
vuln_epss_percentile_gte_from_dict = VulnEpssPercentileGte.from_dict(vuln_epss_percentile_gte_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


