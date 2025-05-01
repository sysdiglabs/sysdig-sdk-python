# RegistryResult

Registry result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_id** | **str** | Identifier of the scan result | [optional] 
**image_id** | **str** | Identifier of the image (hash). | [optional] 
**vendor** | **str** | Identifier the vendor of the image | [optional] 
**pull_string** | **str** | Name of the scanned asset | [optional] 
**vuln_total_by_severity** | [**VulnTotalBySeverity**](VulnTotalBySeverity.md) |  | [optional] 
**created_at** | **str** | datetime of creation | [optional] 

## Example

```python
from sysdig_client.models.registry_result import RegistryResult

# TODO update the JSON string below
json = "{}"
# create an instance of RegistryResult from a JSON string
registry_result_instance = RegistryResult.from_json(json)
# print the JSON string representation of the object
print(RegistryResult.to_json())

# convert the object into a dict
registry_result_dict = registry_result_instance.to_dict()
# create an instance of RegistryResult from a dict
registry_result_from_dict = RegistryResult.from_dict(registry_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


