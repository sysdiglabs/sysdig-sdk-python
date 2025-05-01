# VulnEpssScoreGte

The EPSS score that meets or exceeds the specified threshold value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**extra** | [**VulnEpssScoreGteExtra**](VulnEpssScoreGteExtra.md) |  | 

## Example

```python
from sysdig_client.models.vuln_epss_score_gte import VulnEpssScoreGte

# TODO update the JSON string below
json = "{}"
# create an instance of VulnEpssScoreGte from a JSON string
vuln_epss_score_gte_instance = VulnEpssScoreGte.from_json(json)
# print the JSON string representation of the object
print(VulnEpssScoreGte.to_json())

# convert the object into a dict
vuln_epss_score_gte_dict = vuln_epss_score_gte_instance.to_dict()
# create an instance of VulnEpssScoreGte from a dict
vuln_epss_score_gte_from_dict = VulnEpssScoreGte.from_dict(vuln_epss_score_gte_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


