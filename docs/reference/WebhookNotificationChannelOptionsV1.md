# WebhookNotificationChannelOptionsV1

The Webhook notification channel options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_hiding_of_sensitive_info** | **bool** | Whether the notification info should be hidden when notifications are sent to this notification channel | [optional] 
**url** | **str** | The url to which the request should be posted | [optional] 
**is_allows_insecure_connections** | **bool** | Specifies if the channel allows insecure connections (e.g. plain http, self-signed https) | [optional] 
**additional_headers** | **Dict[str, str]** | Additional headers to send in the request to the target url | [optional] 
**custom_data** | **Dict[str, object]** | Additional data to be added to the template rendering context | [optional] 

## Example

```python
from sysdig_client.models.webhook_notification_channel_options_v1 import WebhookNotificationChannelOptionsV1

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookNotificationChannelOptionsV1 from a JSON string
webhook_notification_channel_options_v1_instance = WebhookNotificationChannelOptionsV1.from_json(json)
# print the JSON string representation of the object
print(WebhookNotificationChannelOptionsV1.to_json())

# convert the object into a dict
webhook_notification_channel_options_v1_dict = webhook_notification_channel_options_v1_instance.to_dict()
# create an instance of WebhookNotificationChannelOptionsV1 from a dict
webhook_notification_channel_options_v1_from_dict = WebhookNotificationChannelOptionsV1.from_dict(webhook_notification_channel_options_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


