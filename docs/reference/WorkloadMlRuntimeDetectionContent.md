# WorkloadMlRuntimeDetectionContent

Workload ML event content

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**EventContentType**](EventContentType.md) |  | 
**command** | **str** | The command name | 
**exe** | **str** | The command path | 
**detected_class_probability** | **float** | The detected class probability (confidence score) | 
**policy_id** | **int** | ID of the policy that generated the event | 

## Example

```python
from sysdig_client.models.workload_ml_runtime_detection_content import WorkloadMlRuntimeDetectionContent

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadMlRuntimeDetectionContent from a JSON string
workload_ml_runtime_detection_content_instance = WorkloadMlRuntimeDetectionContent.from_json(json)
# print the JSON string representation of the object
print(WorkloadMlRuntimeDetectionContent.to_json())

# convert the object into a dict
workload_ml_runtime_detection_content_dict = workload_ml_runtime_detection_content_instance.to_dict()
# create an instance of WorkloadMlRuntimeDetectionContent from a dict
workload_ml_runtime_detection_content_from_dict = WorkloadMlRuntimeDetectionContent.from_dict(workload_ml_runtime_detection_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


