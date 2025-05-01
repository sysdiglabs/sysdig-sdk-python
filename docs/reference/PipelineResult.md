# PipelineResult

pipeline result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_evaluation_result** | [**PolicyEvaluationResult**](PolicyEvaluationResult.md) |  | [optional] 
**result_id** | **str** | Identifier of the scan result | [optional] 
**pull_string** | **str** | image pull string | [optional] 
**vuln_total_by_severity** | [**VulnTotalBySeverity**](VulnTotalBySeverity.md) |  | [optional] 
**image_id** | **str** | Identifier of the image (hash). | [optional] 
**created_at** | **str** | datetime of creation | [optional] 

## Example

```python
from sysdig_client.models.pipeline_result import PipelineResult

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineResult from a JSON string
pipeline_result_instance = PipelineResult.from_json(json)
# print the JSON string representation of the object
print(PipelineResult.to_json())

# convert the object into a dict
pipeline_result_dict = pipeline_result_instance.to_dict()
# create an instance of PipelineResult from a dict
pipeline_result_from_dict = PipelineResult.from_dict(pipeline_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


