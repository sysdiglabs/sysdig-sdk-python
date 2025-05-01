# GetGooglePubSubIntegrationResponse

Get Google Pub/Sub Integration Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name to give to the integration | 
**is_enabled** | **bool** | If the forwarding should be enabled or not | [default to True]
**type** | [**IntegrationType**](IntegrationType.md) |  | 
**channels** | [**List[IntegrationChannel]**](IntegrationChannel.md) | Data types to forward. Must be compatible with the specified Integration type | 
**id** | **int** | The ID of the integration | 
**connection_info** | [**BaseConnectionInfoGooglePubSub**](BaseConnectionInfoGooglePubSub.md) |  | 

## Example

```python
from sysdig_client.models.get_google_pub_sub_integration_response import GetGooglePubSubIntegrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetGooglePubSubIntegrationResponse from a JSON string
get_google_pub_sub_integration_response_instance = GetGooglePubSubIntegrationResponse.from_json(json)
# print the JSON string representation of the object
print(GetGooglePubSubIntegrationResponse.to_json())

# convert the object into a dict
get_google_pub_sub_integration_response_dict = get_google_pub_sub_integration_response_instance.to_dict()
# create an instance of GetGooglePubSubIntegrationResponse from a dict
get_google_pub_sub_integration_response_from_dict = GetGooglePubSubIntegrationResponse.from_dict(get_google_pub_sub_integration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


