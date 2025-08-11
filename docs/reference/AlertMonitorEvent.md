# AlertMonitorEvent

Monitor Alert Event

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
**alert_id** | **int** | ID of the alert that generated the event | [optional]
**ended_at** | **datetime** | Timestamp when the alert resolved | [optional]
**alert_state** | **str** | The alert state. Current supported values are TRIGGERED, RESOLVED. | [optional]
**acknowledged** | **bool** | Whether the alert has been acknowledged. | [optional]
**manually_resolved** | **bool** | Whether the alert has been manually resolved. | [optional]
**silenced** | **bool** | Whether the alert has been silenced. | [optional]

## Example

```python
from sysdig_client.models.alert_monitor_event import AlertMonitorEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AlertMonitorEvent from a JSON string
alert_monitor_event_instance = AlertMonitorEvent.from_json(json)
# print the JSON string representation of the object
print(AlertMonitorEvent.to_json())

# convert the object into a dict
alert_monitor_event_dict = alert_monitor_event_instance.to_dict()
# create an instance of AlertMonitorEvent from a dict
alert_monitor_event_from_dict = AlertMonitorEvent.from_dict(alert_monitor_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


