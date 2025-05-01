# ListAuditEventsResponse

The list of events matching a search criteria.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**AuditPage**](AuditPage.md) |  | 
**data** | [**List[AuditEvent]**](AuditEvent.md) | The list of Audit events. | 

## Example

```python
from sysdig_client.models.list_audit_events_response import ListAuditEventsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAuditEventsResponse from a JSON string
list_audit_events_response_instance = ListAuditEventsResponse.from_json(json)
# print the JSON string representation of the object
print(ListAuditEventsResponse.to_json())

# convert the object into a dict
list_audit_events_response_dict = list_audit_events_response_instance.to_dict()
# create an instance of ListAuditEventsResponse from a dict
list_audit_events_response_from_dict = ListAuditEventsResponse.from_dict(list_audit_events_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


