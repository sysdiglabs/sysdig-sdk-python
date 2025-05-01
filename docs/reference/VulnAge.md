# VulnAge

Predicate expressing \"the Vulnerability is older than <age> days\" 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**extra** | [**VulnAgeExtra**](VulnAgeExtra.md) |  | 

## Example

```python
from sysdig_client.models.vuln_age import VulnAge

# TODO update the JSON string below
json = "{}"
# create an instance of VulnAge from a JSON string
vuln_age_instance = VulnAge.from_json(json)
# print the JSON string representation of the object
print(VulnAge.to_json())

# convert the object into a dict
vuln_age_dict = vuln_age_instance.to_dict()
# create an instance of VulnAge from a dict
vuln_age_from_dict = VulnAge.from_dict(vuln_age_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


