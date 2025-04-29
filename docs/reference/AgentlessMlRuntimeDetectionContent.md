# AgentlessMlRuntimeDetectionContent

Agentless ML event content

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**EventContentType**](EventContentType.md) |  | 
**policy_id** | **int** | ID of the policy that generated the event | [optional] 
**policy_origin** | [**PolicyOrigin**](PolicyOrigin.md) |  | 
**policy_notification_channel_ids** | **List[int]** | The list of notification channels where an alert is sent after event is generated. Doesn&#39;t account for aggregations and eventual thresholds.  | [optional] 
**rule_name** | **str** | Name of the rule the event is generated after | 
**rule_type** | **int** | Rule type: - 1 - List matching - process - 2 - List matching - container - 3 - List matching - file - 4 - List matching - network - 5 - List matching - syscall - 6 - Falco - 7 - Drift detection - 8 - Malware detection - 11 - ML - Cryptominer detection - 13 - ML - AWS anomalous login - 14 - ML - Okta anomalous login  | 
**fields** | [**AgentlessMlRuntimeDetectionContentAllOfFields**](AgentlessMlRuntimeDetectionContentAllOfFields.md) |  | 

## Example

```python
from sysdig_client.models.agentless_ml_runtime_detection_content import AgentlessMlRuntimeDetectionContent

# TODO update the JSON string below
json = "{}"
# create an instance of AgentlessMlRuntimeDetectionContent from a JSON string
agentless_ml_runtime_detection_content_instance = AgentlessMlRuntimeDetectionContent.from_json(json)
# print the JSON string representation of the object
print(AgentlessMlRuntimeDetectionContent.to_json())

# convert the object into a dict
agentless_ml_runtime_detection_content_dict = agentless_ml_runtime_detection_content_instance.to_dict()
# create an instance of AgentlessMlRuntimeDetectionContent from a dict
agentless_ml_runtime_detection_content_from_dict = AgentlessMlRuntimeDetectionContent.from_dict(agentless_ml_runtime_detection_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


