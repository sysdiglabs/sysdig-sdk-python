# AuthenticatedConnectionInfoWebhook


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
from sysdig_client.models.authenticated_connection_info_webhook import AuthenticatedConnectionInfoWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatedConnectionInfoWebhook from a JSON string
authenticated_connection_info_webhook_instance = AuthenticatedConnectionInfoWebhook.from_json(json)
# print the JSON string representation of the object
print(AuthenticatedConnectionInfoWebhook.to_json())

# convert the object into a dict
authenticated_connection_info_webhook_dict = authenticated_connection_info_webhook_instance.to_dict()
# create an instance of AuthenticatedConnectionInfoWebhook from a dict
authenticated_connection_info_webhook_from_dict = AuthenticatedConnectionInfoWebhook.from_dict(authenticated_connection_info_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


