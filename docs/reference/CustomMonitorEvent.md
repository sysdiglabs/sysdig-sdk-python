# CustomMonitorEvent

Monitor Custom Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The event id. |
**created_on** | **datetime** | Timestamp when the event was created in the system |
**occurred_at** | **datetime** | Event logical timestamp (when the event occurred). For alert events, this is the time when the alert was triggered. |
**name** | **str** | The event name |
**description** | **str** | Description of the event. | [optional]
**severity** | **int** | The event severity. A lower value means more severe, with 0 being the highest severity and 7 being the lowest. |
**scope_labels** | [**List[MonitorScopeLabel]**](MonitorScopeLabel.md) | List of scope labels, including those from initial scope and those coming from the enrichment process. | [optional]
**scope** | **str** | Initial event scope | [optional]
**source** | **str** | The event source. Well known sources include kubernetes, docker, containerd. User created events have a value of api for this field, unless specifically overwritten at creation time | [optional]

## Example

```python
from sysdig_client.models.custom_monitor_event import CustomMonitorEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CustomMonitorEvent from a JSON string
custom_monitor_event_instance = CustomMonitorEvent.from_json(json)
# print the JSON string representation of the object
print(CustomMonitorEvent.to_json())

# convert the object into a dict
custom_monitor_event_dict = custom_monitor_event_instance.to_dict()
# create an instance of CustomMonitorEvent from a dict
custom_monitor_event_from_dict = CustomMonitorEvent.from_dict(custom_monitor_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


