# CreateMicrosoftSentinelIntegrationRequest

Save Microsoft Sentinel Integration Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name to give to the integration | 
**is_enabled** | **bool** | If the forwarding should be enabled or not | [optional] [default to True]
**type** | [**IntegrationType**](IntegrationType.md) |  | 
**channels** | [**List[IntegrationChannel]**](IntegrationChannel.md) | Data types to forward. Must be compatible with the specified Integration type | [optional] 
**connection_info** | [**MicrosoftSentinelCreateConnectionInfo**](MicrosoftSentinelCreateConnectionInfo.md) |  | 

## Example

```python
from sysdig_client.models.create_microsoft_sentinel_integration_request import CreateMicrosoftSentinelIntegrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMicrosoftSentinelIntegrationRequest from a JSON string
create_microsoft_sentinel_integration_request_instance = CreateMicrosoftSentinelIntegrationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMicrosoftSentinelIntegrationRequest.to_json())

# convert the object into a dict
create_microsoft_sentinel_integration_request_dict = create_microsoft_sentinel_integration_request_instance.to_dict()
# create an instance of CreateMicrosoftSentinelIntegrationRequest from a dict
create_microsoft_sentinel_integration_request_from_dict = CreateMicrosoftSentinelIntegrationRequest.from_dict(create_microsoft_sentinel_integration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


