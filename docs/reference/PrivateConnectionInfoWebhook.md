# PrivateConnectionInfoWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | **str** | Secret to use, according to the \&quot;auth\&quot; value. | [optional] 

## Example

```python
from sysdig_client.models.private_connection_info_webhook import PrivateConnectionInfoWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateConnectionInfoWebhook from a JSON string
private_connection_info_webhook_instance = PrivateConnectionInfoWebhook.from_json(json)
# print the JSON string representation of the object
print(PrivateConnectionInfoWebhook.to_json())

# convert the object into a dict
private_connection_info_webhook_dict = private_connection_info_webhook_instance.to_dict()
# create an instance of PrivateConnectionInfoWebhook from a dict
private_connection_info_webhook_from_dict = PrivateConnectionInfoWebhook.from_dict(private_connection_info_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


