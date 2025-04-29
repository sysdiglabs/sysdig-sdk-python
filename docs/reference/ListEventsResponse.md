# ListEventsResponse

The list of events matching a search criteria.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**EventsFeedPage**](EventsFeedPage.md) |  | 
**data** | [**List[Event]**](Event.md) | The list of events | 

## Example

```python
from sysdig_client.models.list_events_response import ListEventsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListEventsResponse from a JSON string
list_events_response_instance = ListEventsResponse.from_json(json)
# print the JSON string representation of the object
print(ListEventsResponse.to_json())

# convert the object into a dict
list_events_response_dict = list_events_response_instance.to_dict()
# create an instance of ListEventsResponse from a dict
list_events_response_from_dict = ListEventsResponse.from_dict(list_events_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


