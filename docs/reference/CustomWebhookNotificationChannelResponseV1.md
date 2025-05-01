# CustomWebhookNotificationChannelResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**CustomWebhookNotificationChannelOptionsV1**](CustomWebhookNotificationChannelOptionsV1.md) |  | 

## Example

```python
from sysdig_client.models.custom_webhook_notification_channel_response_v1 import CustomWebhookNotificationChannelResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of CustomWebhookNotificationChannelResponseV1 from a JSON string
custom_webhook_notification_channel_response_v1_instance = CustomWebhookNotificationChannelResponseV1.from_json(json)
# print the JSON string representation of the object
print(CustomWebhookNotificationChannelResponseV1.to_json())

# convert the object into a dict
custom_webhook_notification_channel_response_v1_dict = custom_webhook_notification_channel_response_v1_instance.to_dict()
# create an instance of CustomWebhookNotificationChannelResponseV1 from a dict
custom_webhook_notification_channel_response_v1_from_dict = CustomWebhookNotificationChannelResponseV1.from_dict(custom_webhook_notification_channel_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


