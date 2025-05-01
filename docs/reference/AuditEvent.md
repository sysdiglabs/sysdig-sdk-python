# AuditEvent

Platform Audit Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The event id. | [optional] 
**cursor** | **str** | The cursor that can be used to fetch a set of events surrounding this same event. By providing this value as &#x60;cursor&#x60; in a GET request, you will get the set of events surrounding this current event.  | [optional] 
**timestamp** | **int** | The event timestamp in nanoseconds. | [optional] 
**content** | [**AuditTrailContent**](AuditTrailContent.md) |  | [optional] 
**labels** | **Dict[str, str]** | Key value pairs of values, represents entityType where the Audit Event was generated.  | [optional] 

## Example

```python
from sysdig_client.models.audit_event import AuditEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AuditEvent from a JSON string
audit_event_instance = AuditEvent.from_json(json)
# print the JSON string representation of the object
print(AuditEvent.to_json())

# convert the object into a dict
audit_event_dict = audit_event_instance.to_dict()
# create an instance of AuditEvent from a dict
audit_event_from_dict = AuditEvent.from_dict(audit_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


