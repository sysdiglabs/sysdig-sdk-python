# AuditSupportedFiltersResponse

The list of supported attributes for filtering Activity Audit entries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AuditSupportedFilter]**](AuditSupportedFilter.md) | The list of supported attributes for filtering Activity Audit entries. | 

## Example

```python
from sysdig_client.models.audit_supported_filters_response import AuditSupportedFiltersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuditSupportedFiltersResponse from a JSON string
audit_supported_filters_response_instance = AuditSupportedFiltersResponse.from_json(json)
# print the JSON string representation of the object
print(AuditSupportedFiltersResponse.to_json())

# convert the object into a dict
audit_supported_filters_response_dict = audit_supported_filters_response_instance.to_dict()
# create an instance of AuditSupportedFiltersResponse from a dict
audit_supported_filters_response_from_dict = AuditSupportedFiltersResponse.from_dict(audit_supported_filters_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


