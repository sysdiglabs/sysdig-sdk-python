# DenyCve

Predicate expressing \"any of these CVEs is present\". 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**extra** | [**DenyCveExtra**](DenyCveExtra.md) |  | 

## Example

```python
from sysdig_client.models.deny_cve import DenyCve

# TODO update the JSON string below
json = "{}"
# create an instance of DenyCve from a JSON string
deny_cve_instance = DenyCve.from_json(json)
# print the JSON string representation of the object
print(DenyCve.to_json())

# convert the object into a dict
deny_cve_dict = deny_cve_instance.to_dict()
# create an instance of DenyCve from a dict
deny_cve_from_dict = DenyCve.from_dict(deny_cve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


