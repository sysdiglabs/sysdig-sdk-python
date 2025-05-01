# VulnIsInUse

The vulnerable resources currently in use.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from sysdig_client.models.vuln_is_in_use import VulnIsInUse

# TODO update the JSON string below
json = "{}"
# create an instance of VulnIsInUse from a JSON string
vuln_is_in_use_instance = VulnIsInUse.from_json(json)
# print the JSON string representation of the object
print(VulnIsInUse.to_json())

# convert the object into a dict
vuln_is_in_use_dict = vuln_is_in_use_instance.to_dict()
# create an instance of VulnIsInUse from a dict
vuln_is_in_use_from_dict = VulnIsInUse.from_dict(vuln_is_in_use_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


