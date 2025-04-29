# WorkloadRuntimeDetectionContent

Policy Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**EventContentType**](EventContentType.md) |  | 
**policy_id** | **int** | ID of the policy that generated the event | 
**rule_name** | **str** | Name of the rule the event is generated after | 
**rule_type** | **int** | Rule type: - 1 - List matching - process - 2 - List matching - container - 3 - List matching - file - 4 - List matching - network - 5 - List matching - syscall - 6 - Falco - 7 - Drift detection - 8 - Malware detection - 11 - ML - Cryptominer detection - 13 - ML - AWS anomalous login - 14 - ML - Okta anomalous login  | 
**rule_sub_type** | **int** | Rule subtype: - 1 - List matching - network - inbound - 2 - List matching - network - outbound - 3 - List matching - network - listening - 4 - List matching - file - readwrite - 5 - List matching - file - read only  | 
**rule_tags** | **List[str]** | The tags attached to the rule | 
**output** | **str** | Event output, generated after the configured rule | 
**fields** | [**WorkloadRuntimeDetectionContentAllOfFields**](WorkloadRuntimeDetectionContentAllOfFields.md) |  | 
**run_book** | **str** | The runbook URL as configured in the policy. | [optional] 
**origin** | [**PolicyOrigin**](PolicyOrigin.md) |  | [optional] 

## Example

```python
from sysdig_client.models.workload_runtime_detection_content import WorkloadRuntimeDetectionContent

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadRuntimeDetectionContent from a JSON string
workload_runtime_detection_content_instance = WorkloadRuntimeDetectionContent.from_json(json)
# print the JSON string representation of the object
print(WorkloadRuntimeDetectionContent.to_json())

# convert the object into a dict
workload_runtime_detection_content_dict = workload_runtime_detection_content_instance.to_dict()
# create an instance of WorkloadRuntimeDetectionContent from a dict
workload_runtime_detection_content_from_dict = WorkloadRuntimeDetectionContent.from_dict(workload_runtime_detection_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


