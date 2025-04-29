# EventContent

Event data. It contains fields from the original event and attributes generated at the engine level. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**EventContentType**](EventContentType.md) |  | 
**namespace** | **str** | Kubernetes namespace | [optional] 
**cluster_name** | **str** | Kubernetes cluster name | [optional] 
**resource_name** | **str** | Kubernetes resource name | [optional] 
**resource_kind** | **str** | Kubernetes resource kind | [optional] 
**zones** | [**List[Zone]**](Zone.md) | List of zones that match the scope of the resource. | [optional] 
**scan_result** | [**K8sAdmissionReviewContentAllOfScanResult**](K8sAdmissionReviewContentAllOfScanResult.md) |  | 
**integration_id** | **str** | The unique identifier of the integration that generated the event. | 
**integration_type** | **str** | The type of integration that generated the event. | 
**rule_name** | **str** | Name of the rule the event is generated after | 
**rule_type** | **int** | Rule type: - 1 - List matching - process - 2 - List matching - container - 3 - List matching - file - 4 - List matching - network - 5 - List matching - syscall - 6 - Falco - 7 - Drift detection - 8 - Malware detection - 11 - ML - Cryptominer detection - 13 - ML - AWS anomalous login - 14 - ML - Okta anomalous login  | 
**rule_tags** | **List[str]** | The tags attached to the rule | 
**policy_id** | **int** | ID of the policy that generated the event | 
**policy_origin** | [**PolicyOrigin**](PolicyOrigin.md) |  | 
**policy_notification_channel_ids** | **List[int]** | The list of notification channels where an alert is sent after event is generated. Doesn&#39;t account for aggregations and eventual thresholds.  | 
**priority** | **str** | Rule priority | [optional] 
**output** | **str** | Event output, generated after the configured rule | 
**fields** | [**StatefulDetectionsContentAllOfFields**](StatefulDetectionsContentAllOfFields.md) |  | 
**rule_sub_type** | **int** | Rule subtype: - 1 - List matching - network - inbound - 2 - List matching - network - outbound - 3 - List matching - network - listening - 4 - List matching - file - readwrite - 5 - List matching - file - read only  | 
**run_book** | **str** | The runbook URL as configured in the policy. | [optional] 
**origin** | [**PolicyOrigin**](PolicyOrigin.md) |  | [optional] 
**command** | **str** | The command name | 
**exe** | **str** | The command path | 
**detected_class_probability** | **float** | The detected class probability (confidence score) | 
**stats** | [**List[StatsInner]**](StatsInner.md) | An array representing the relevant APIs and how often they were called in the time window.  | [optional] 
**sequence** | [**List[SequenceInner]**](SequenceInner.md) | The sequence of events that occurred to trigger the event. The sequence is represented as a list of events, where each event is a map of key-value pairs.  | [optional] 

## Example

```python
from sysdig_client.models.event_content import EventContent

# TODO update the JSON string below
json = "{}"
# create an instance of EventContent from a JSON string
event_content_instance = EventContent.from_json(json)
# print the JSON string representation of the object
print(EventContent.to_json())

# convert the object into a dict
event_content_dict = event_content_instance.to_dict()
# create an instance of EventContent from a dict
event_content_from_dict = EventContent.from_dict(event_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


