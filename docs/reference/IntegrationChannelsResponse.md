# IntegrationChannelsResponse

Integration Channels Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[IntegrationChannel]**](IntegrationChannel.md) | Data types to forward. Must be compatible with the specified Integration type | 

## Example

```python
from sysdig_client.models.integration_channels_response import IntegrationChannelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationChannelsResponse from a JSON string
integration_channels_response_instance = IntegrationChannelsResponse.from_json(json)
# print the JSON string representation of the object
print(IntegrationChannelsResponse.to_json())

# convert the object into a dict
integration_channels_response_dict = integration_channels_response_instance.to_dict()
# create an instance of IntegrationChannelsResponse from a dict
integration_channels_response_from_dict = IntegrationChannelsResponse.from_dict(integration_channels_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


