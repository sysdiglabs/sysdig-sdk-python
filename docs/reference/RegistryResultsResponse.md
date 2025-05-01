# RegistryResultsResponse

registry results response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**VulnerabilityManagementPage**](VulnerabilityManagementPage.md) |  | [optional] 
**data** | [**List[RegistryResult]**](RegistryResult.md) |  | [optional] 

## Example

```python
from sysdig_client.models.registry_results_response import RegistryResultsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegistryResultsResponse from a JSON string
registry_results_response_instance = RegistryResultsResponse.from_json(json)
# print the JSON string representation of the object
print(RegistryResultsResponse.to_json())

# convert the object into a dict
registry_results_response_dict = registry_results_response_instance.to_dict()
# create an instance of RegistryResultsResponse from a dict
registry_results_response_from_dict = RegistryResultsResponse.from_dict(registry_results_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


