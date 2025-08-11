# ListMonitorEventsResponse

The list of events matching a search criteria.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**MonitorEventsPage**](MonitorEventsPage.md) |  |
**data** | [**List[MonitorEvent]**](MonitorEvent.md) | The list of events |

## Example

```python
from sysdig_client.models.list_monitor_events_response import ListMonitorEventsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListMonitorEventsResponse from a JSON string
list_monitor_events_response_instance = ListMonitorEventsResponse.from_json(json)
# print the JSON string representation of the object
print(ListMonitorEventsResponse.to_json())

# convert the object into a dict
list_monitor_events_response_dict = list_monitor_events_response_instance.to_dict()
# create an instance of ListMonitorEventsResponse from a dict
list_monitor_events_response_from_dict = ListMonitorEventsResponse.from_dict(list_monitor_events_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


