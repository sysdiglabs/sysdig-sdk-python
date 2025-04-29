# StatefulDetectionsContent

Stateful detections event content 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**EventContentType**](EventContentType.md) |  | 
**rule_name** | **str** | Name of the rule the event is generated after | 
**rule_type** | **int** | Rule type: - 1 - List matching - process - 2 - List matching - container - 3 - List matching - file - 4 - List matching - network - 5 - List matching - syscall - 6 - Falco - 7 - Drift detection - 8 - Malware detection - 11 - ML - Cryptominer detection - 13 - ML - AWS anomalous login - 14 - ML - Okta anomalous login  | 
**rule_tags** | **List[str]** | The tags attached to the rule | 
**policy_id** | **int** | ID of the policy that generated the event | 
**policy_origin** | [**PolicyOrigin**](PolicyOrigin.md) |  | 
**policy_notification_channel_ids** | **List[int]** | The list of notification channels where an alert is sent after event is generated. Doesn&#39;t account for aggregations and eventual thresholds.  | 
**output** | **str** | Event output, generated after the configured rule | 
**stats** | [**List[StatsInner]**](StatsInner.md) | An array representing the relevant APIs and how often they were called in the time window.  | [optional] 
**sequence** | [**List[SequenceInner]**](SequenceInner.md) | The sequence of events that occurred to trigger the event. The sequence is represented as a list of events, where each event is a map of key-value pairs.  | [optional] 
**fields** | [**StatefulDetectionsContentAllOfFields**](StatefulDetectionsContentAllOfFields.md) |  | 

## Example

```python
from sysdig_client.models.stateful_detections_content import StatefulDetectionsContent

# TODO update the JSON string below
json = "{}"
# create an instance of StatefulDetectionsContent from a JSON string
stateful_detections_content_instance = StatefulDetectionsContent.from_json(json)
# print the JSON string representation of the object
print(StatefulDetectionsContent.to_json())

# convert the object into a dict
stateful_detections_content_dict = stateful_detections_content_instance.to_dict()
# create an instance of StatefulDetectionsContent from a dict
stateful_detections_content_from_dict = StatefulDetectionsContent.from_dict(stateful_detections_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


