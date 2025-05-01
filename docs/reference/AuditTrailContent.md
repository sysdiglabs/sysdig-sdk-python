# AuditTrailContent

Content object for Platform Audit Event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp_ns** | **int** | The event timestamp in nanoseconds. | [optional] 
**user_id** | **int** | ID of user that was preforming some action. | [optional] 
**username** | **str** | Username of the user that was preforming some action. | [optional] 
**team_id** | **int** | Team ID, that user who preformed some action was logged in. | [optional] 
**team_name** | **str** | Name of the team, that user who preformed action was logged in. | [optional] 
**request_method** | **str** | HTTP request method that was used to preform action. | [optional] 
**request_uri** | **str** | URI of the request that was used to preform action. | [optional] 
**user_origin_ip** | **str** | IP address of the user that was preforming action. | [optional] 
**query_string** | **str** | Query string of the request that was used to preform action. | [optional] 
**response_status_code** | **int** | HTTP response status code of the request that was used to preform action. | [optional] 
**entity_type** | **str** | Type of entity that was affected by the action. Full list of possible values can be found in the our documentation https://docs.sysdig.com/en/docs/administration/administration-settings/app-status-and-audit/sysdig-platform-audit/#sysdig-monitor-and-sysdig-platform.  | [optional] 
**entity_id** | **str** | ID of the entity that was affected by the action. | [optional] 
**entity_payload** | **str** | Payload of the entity that was affected by the action. | [optional] 
**service_account_id** | **int** | ID of the service account that was used to preform action. | [optional] 
**service_account_name** | **str** | Name of the service account that was used to preform action. | [optional] 

## Example

```python
from sysdig_client.models.audit_trail_content import AuditTrailContent

# TODO update the JSON string below
json = "{}"
# create an instance of AuditTrailContent from a JSON string
audit_trail_content_instance = AuditTrailContent.from_json(json)
# print the JSON string representation of the object
print(AuditTrailContent.to_json())

# convert the object into a dict
audit_trail_content_dict = audit_trail_content_instance.to_dict()
# create an instance of AuditTrailContent from a dict
audit_trail_content_from_dict = AuditTrailContent.from_dict(audit_trail_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


