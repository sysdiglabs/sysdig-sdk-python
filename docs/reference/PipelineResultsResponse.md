# PipelineResultsResponse

pipeline results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**VulnerabilityManagementPage**](VulnerabilityManagementPage.md) |  | [optional] 
**data** | [**List[PipelineResult]**](PipelineResult.md) |  | [optional] 

## Example

```python
from sysdig_client.models.pipeline_results_response import PipelineResultsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineResultsResponse from a JSON string
pipeline_results_response_instance = PipelineResultsResponse.from_json(json)
# print the JSON string representation of the object
print(PipelineResultsResponse.to_json())

# convert the object into a dict
pipeline_results_response_dict = pipeline_results_response_instance.to_dict()
# create an instance of PipelineResultsResponse from a dict
pipeline_results_response_from_dict = PipelineResultsResponse.from_dict(pipeline_results_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


