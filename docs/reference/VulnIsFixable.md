# VulnIsFixable

Predicate expressing \"the Vulnerability is Fixable\". 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from sysdig_client.models.vuln_is_fixable import VulnIsFixable

# TODO update the JSON string below
json = "{}"
# create an instance of VulnIsFixable from a JSON string
vuln_is_fixable_instance = VulnIsFixable.from_json(json)
# print the JSON string representation of the object
print(VulnIsFixable.to_json())

# convert the object into a dict
vuln_is_fixable_dict = vuln_is_fixable_instance.to_dict()
# create an instance of VulnIsFixable from a dict
vuln_is_fixable_from_dict = VulnIsFixable.from_dict(vuln_is_fixable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


