# UpdateSyslogIntegrationRequest

Update Syslog Integration Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name to give to the integration | 
**is_enabled** | **bool** | If the forwarding should be enabled or not | [optional] [default to True]
**type** | [**IntegrationType**](IntegrationType.md) |  | 
**channels** | [**List[IntegrationChannel]**](IntegrationChannel.md) | Data types to forward. Must be compatible with the specified Integration type | [optional] 
**connection_info** | [**BaseConnectionInfoSyslog**](BaseConnectionInfoSyslog.md) |  | 

## Example

```python
from sysdig_client.models.update_syslog_integration_request import UpdateSyslogIntegrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSyslogIntegrationRequest from a JSON string
update_syslog_integration_request_instance = UpdateSyslogIntegrationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSyslogIntegrationRequest.to_json())

# convert the object into a dict
update_syslog_integration_request_dict = update_syslog_integration_request_instance.to_dict()
# create an instance of UpdateSyslogIntegrationRequest from a dict
update_syslog_integration_request_from_dict = UpdateSyslogIntegrationRequest.from_dict(update_syslog_integration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


