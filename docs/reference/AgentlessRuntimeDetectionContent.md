# AgentlessRuntimeDetectionContent

Agentless CDR event content

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**EventContentType**](EventContentType.md) |  | 
**integration_id** | **str** | The unique identifier of the integration that generated the event. | 
**integration_type** | **str** | The type of integration that generated the event. | 
**rule_name** | **str** | Name of the rule the event is generated after | 
**rule_type** | **int** | Rule type: - 1 - List matching - process - 2 - List matching - container - 3 - List matching - file - 4 - List matching - network - 5 - List matching - syscall - 6 - Falco - 7 - Drift detection - 8 - Malware detection - 11 - ML - Cryptominer detection - 13 - ML - AWS anomalous login - 14 - ML - Okta anomalous login  | 
**rule_tags** | **List[str]** | The tags attached to the rule | [optional] 
**policy_id** | **int** | ID of the policy that generated the event | 
**policy_origin** | [**PolicyOrigin**](PolicyOrigin.md) |  | 
**policy_notification_channel_ids** | **List[int]** | The list of notification channels where an alert is sent after event is generated. Doesn&#39;t account for aggregations and eventual thresholds.  | [optional] 
**priority** | **str** | Rule priority | [optional] 
**output** | **str** | Event output, generated after the configured rule | [optional] 
**fields** | [**AgentlessRuntimeDetectionContentAllOfFields**](AgentlessRuntimeDetectionContentAllOfFields.md) |  | [optional] 

## Example

```python
from sysdig_client.models.agentless_runtime_detection_content import AgentlessRuntimeDetectionContent

# TODO update the JSON string below
json = "{}"
# create an instance of AgentlessRuntimeDetectionContent from a JSON string
agentless_runtime_detection_content_instance = AgentlessRuntimeDetectionContent.from_json(json)
# print the JSON string representation of the object
print(AgentlessRuntimeDetectionContent.to_json())

# convert the object into a dict
agentless_runtime_detection_content_dict = agentless_runtime_detection_content_instance.to_dict()
# create an instance of AgentlessRuntimeDetectionContent from a dict
agentless_runtime_detection_content_from_dict = AgentlessRuntimeDetectionContent.from_dict(agentless_runtime_detection_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


