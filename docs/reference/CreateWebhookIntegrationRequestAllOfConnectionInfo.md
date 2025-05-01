# CreateWebhookIntegrationRequestAllOfConnectionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | Webhook endpoint following the schema protocol | 
**is_insecure** | **bool** | Skip TLS certificate verification | [optional] [default to False]
**headers** | [**List[KeyValueObject]**](KeyValueObject.md) | Extra headers to add to the request. Each header mapping requires 2 keys: &#39;key&#39; for the header key and &#39;value&#39; for its value | [optional] 
**output** | **str** | Payload format | [optional] [default to 'json']
**timestamp_format** | **str** | The resolution of the \&quot;timestamp\&quot; field in the payload | [optional] [default to 'nanoseconds']
**auth** | **str** | Authentication method | 
**certificate_id** | **int** | ID of a certificate stored in Sysdig&#39;s [Certificates Management tool](#tag/Certificates). Note that the RFC 5425 (TLS) protocol is required for you to see this field | [optional] 
**secret** | **str** | Secret to use, according to the \&quot;auth\&quot; value. | 

## Example

```python
from sysdig_client.models.create_webhook_integration_request_all_of_connection_info import CreateWebhookIntegrationRequestAllOfConnectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebhookIntegrationRequestAllOfConnectionInfo from a JSON string
create_webhook_integration_request_all_of_connection_info_instance = CreateWebhookIntegrationRequestAllOfConnectionInfo.from_json(json)
# print the JSON string representation of the object
print(CreateWebhookIntegrationRequestAllOfConnectionInfo.to_json())

# convert the object into a dict
create_webhook_integration_request_all_of_connection_info_dict = create_webhook_integration_request_all_of_connection_info_instance.to_dict()
# create an instance of CreateWebhookIntegrationRequestAllOfConnectionInfo from a dict
create_webhook_integration_request_all_of_connection_info_from_dict = CreateWebhookIntegrationRequestAllOfConnectionInfo.from_dict(create_webhook_integration_request_all_of_connection_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


