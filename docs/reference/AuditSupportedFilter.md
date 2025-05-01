# AuditSupportedFilter

A supported field for filtering Activity Audit events.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Attribute onto which filtering is supported. | 
**type** | [**SupportedFilterType**](SupportedFilterType.md) |  | 
**operands** | [**List[Operand]**](Operand.md) | The list of supported operands for filtering events. | [optional] 

## Example

```python
from sysdig_client.models.audit_supported_filter import AuditSupportedFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AuditSupportedFilter from a JSON string
audit_supported_filter_instance = AuditSupportedFilter.from_json(json)
# print the JSON string representation of the object
print(AuditSupportedFilter.to_json())

# convert the object into a dict
audit_supported_filter_dict = audit_supported_filter_instance.to_dict()
# create an instance of AuditSupportedFilter from a dict
audit_supported_filter_from_dict = AuditSupportedFilter.from_dict(audit_supported_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


