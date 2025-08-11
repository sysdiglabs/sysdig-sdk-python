# MonitorEvent

Monitor Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the event. Current supported values are ALERT, CUSTOM. As the list of supported event types may change in the future, clients should handle unknown event types gracefully. | [optional]

## Example

```python
from sysdig_client.models.monitor_event import MonitorEvent

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorEvent from a JSON string
monitor_event_instance = MonitorEvent.from_json(json)
# print the JSON string representation of the object
print(MonitorEvent.to_json())

# convert the object into a dict
monitor_event_dict = monitor_event_instance.to_dict()
# create an instance of MonitorEvent from a dict
monitor_event_from_dict = MonitorEvent.from_dict(monitor_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


