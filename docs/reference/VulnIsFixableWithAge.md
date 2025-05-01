# VulnIsFixableWithAge

Predicate expressing \"the Vulnerability is Fixable and its fix is older than <age> days\". 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**extra** | [**VulnIsFixableWithAgeExtra**](VulnIsFixableWithAgeExtra.md) |  | 

## Example

```python
from sysdig_client.models.vuln_is_fixable_with_age import VulnIsFixableWithAge

# TODO update the JSON string below
json = "{}"
# create an instance of VulnIsFixableWithAge from a JSON string
vuln_is_fixable_with_age_instance = VulnIsFixableWithAge.from_json(json)
# print the JSON string representation of the object
print(VulnIsFixableWithAge.to_json())

# convert the object into a dict
vuln_is_fixable_with_age_dict = vuln_is_fixable_with_age_instance.to_dict()
# create an instance of VulnIsFixableWithAge from a dict
vuln_is_fixable_with_age_from_dict = VulnIsFixableWithAge.from_dict(vuln_is_fixable_with_age_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


