# RuntimeResultsResponse

runtime results response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**VulnerabilityManagementPage**](VulnerabilityManagementPage.md) |  | [optional] 
**data** | [**List[RuntimeResult]**](RuntimeResult.md) |  | [optional] 

## Example

```python
from sysdig_client.models.runtime_results_response import RuntimeResultsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeResultsResponse from a JSON string
runtime_results_response_instance = RuntimeResultsResponse.from_json(json)
# print the JSON string representation of the object
print(RuntimeResultsResponse.to_json())

# convert the object into a dict
runtime_results_response_dict = runtime_results_response_instance.to_dict()
# create an instance of RuntimeResultsResponse from a dict
runtime_results_response_from_dict = RuntimeResultsResponse.from_dict(runtime_results_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


