# UpdateGooglePubSubIntegrationRequest

Update Google Pub/Sub Integration Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name to give to the integration | 
**is_enabled** | **bool** | If the forwarding should be enabled or not | [optional] [default to True]
**type** | [**IntegrationType**](IntegrationType.md) |  | 
**channels** | [**List[IntegrationChannel]**](IntegrationChannel.md) | Data types to forward. Must be compatible with the specified Integration type | [optional] 
**connection_info** | [**GooglePubSubCreateConnectionInfo1**](GooglePubSubCreateConnectionInfo1.md) |  | 

## Example

```python
from sysdig_client.models.update_google_pub_sub_integration_request import UpdateGooglePubSubIntegrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGooglePubSubIntegrationRequest from a JSON string
update_google_pub_sub_integration_request_instance = UpdateGooglePubSubIntegrationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateGooglePubSubIntegrationRequest.to_json())

# convert the object into a dict
update_google_pub_sub_integration_request_dict = update_google_pub_sub_integration_request_instance.to_dict()
# create an instance of UpdateGooglePubSubIntegrationRequest from a dict
update_google_pub_sub_integration_request_from_dict = UpdateGooglePubSubIntegrationRequest.from_dict(update_google_pub_sub_integration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


