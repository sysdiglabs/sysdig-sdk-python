# CustomWebhookNotificationChannelOptionsV1

The custom webhook notification channel options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_hiding_of_sensitive_info** | **bool** | Whether the notification info should be hidden when notifications are sent to this notification channel | [optional] 
**url** | **str** | The url to which the request should be sent | 
**template** | **str** | The custom template used by this webhook, currently a JSON potentially enriched by Sysdig Templating Language | 
**http_method** | **str** | The HTTP method to use when doing the request to the target url | [optional] [default to 'POST']
**is_allows_insecure_connections** | **bool** | Specifies if the channel allows insecure connections (e.g. plain http, self-signed https) | [optional] 
**additional_headers** | **Dict[str, str]** | Additional headers to send as part of the request to the target url | [optional] 

## Example

```python
from sysdig_client.models.custom_webhook_notification_channel_options_v1 import CustomWebhookNotificationChannelOptionsV1

# TODO update the JSON string below
json = "{}"
# create an instance of CustomWebhookNotificationChannelOptionsV1 from a JSON string
custom_webhook_notification_channel_options_v1_instance = CustomWebhookNotificationChannelOptionsV1.from_json(json)
# print the JSON string representation of the object
print(CustomWebhookNotificationChannelOptionsV1.to_json())

# convert the object into a dict
custom_webhook_notification_channel_options_v1_dict = custom_webhook_notification_channel_options_v1_instance.to_dict()
# create an instance of CustomWebhookNotificationChannelOptionsV1 from a dict
custom_webhook_notification_channel_options_v1_from_dict = CustomWebhookNotificationChannelOptionsV1.from_dict(custom_webhook_notification_channel_options_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


