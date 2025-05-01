# WebhookNotificationChannelResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**WebhookNotificationChannelOptionsV1**](WebhookNotificationChannelOptionsV1.md) |  | 

## Example

```python
from sysdig_client.models.webhook_notification_channel_response_v1 import WebhookNotificationChannelResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookNotificationChannelResponseV1 from a JSON string
webhook_notification_channel_response_v1_instance = WebhookNotificationChannelResponseV1.from_json(json)
# print the JSON string representation of the object
print(WebhookNotificationChannelResponseV1.to_json())

# convert the object into a dict
webhook_notification_channel_response_v1_dict = webhook_notification_channel_response_v1_instance.to_dict()
# create an instance of WebhookNotificationChannelResponseV1 from a dict
webhook_notification_channel_response_v1_from_dict = WebhookNotificationChannelResponseV1.from_dict(webhook_notification_channel_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


