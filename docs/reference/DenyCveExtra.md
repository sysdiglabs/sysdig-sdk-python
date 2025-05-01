# DenyCveExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vuln_ids** | **List[str]** |  | [optional] 

## Example

```python
from sysdig_client.models.deny_cve_extra import DenyCveExtra

# TODO update the JSON string below
json = "{}"
# create an instance of DenyCveExtra from a JSON string
deny_cve_extra_instance = DenyCveExtra.from_json(json)
# print the JSON string representation of the object
print(DenyCveExtra.to_json())

# convert the object into a dict
deny_cve_extra_dict = deny_cve_extra_instance.to_dict()
# create an instance of DenyCveExtra from a dict
deny_cve_extra_from_dict = DenyCveExtra.from_dict(deny_cve_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


