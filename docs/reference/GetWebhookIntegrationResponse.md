# GetWebhookIntegrationResponse

Get Webhook Integration Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name to give to the integration | 
**is_enabled** | **bool** | If the forwarding should be enabled or not | [default to True]
**type** | [**IntegrationType**](IntegrationType.md) |  | 
**channels** | [**List[IntegrationChannel]**](IntegrationChannel.md) | Data types to forward. Must be compatible with the specified Integration type | 
**id** | **int** | The ID of the integration | 
**connection_info** | [**BaseConnectionInfoWebhook**](BaseConnectionInfoWebhook.md) |  | 

## Example

```python
from sysdig_client.models.get_webhook_integration_response import GetWebhookIntegrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebhookIntegrationResponse from a JSON string
get_webhook_integration_response_instance = GetWebhookIntegrationResponse.from_json(json)
# print the JSON string representation of the object
print(GetWebhookIntegrationResponse.to_json())

# convert the object into a dict
get_webhook_integration_response_dict = get_webhook_integration_response_instance.to_dict()
# create an instance of GetWebhookIntegrationResponse from a dict
get_webhook_integration_response_from_dict = GetWebhookIntegrationResponse.from_dict(get_webhook_integration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


