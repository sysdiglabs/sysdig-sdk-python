# IntegrationResponse

Get Integration Response

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
from sysdig_client.models.integration_response import IntegrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationResponse from a JSON string
integration_response_instance = IntegrationResponse.from_json(json)
# print the JSON string representation of the object
print(IntegrationResponse.to_json())

# convert the object into a dict
integration_response_dict = integration_response_instance.to_dict()
# create an instance of IntegrationResponse from a dict
integration_response_from_dict = IntegrationResponse.from_dict(integration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


