# GchatNotificationChannelOptionsV1

The Google Chat notification channel options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_hiding_of_sensitive_info** | **bool** | Whether the notification info should be hidden when notifications are sent to this notification channel | [optional] 
**url** | **str** | Google Chat Webhook URL | 

## Example

```python
from sysdig_client.models.gchat_notification_channel_options_v1 import GchatNotificationChannelOptionsV1

# TODO update the JSON string below
json = "{}"
# create an instance of GchatNotificationChannelOptionsV1 from a JSON string
gchat_notification_channel_options_v1_instance = GchatNotificationChannelOptionsV1.from_json(json)
# print the JSON string representation of the object
print(GchatNotificationChannelOptionsV1.to_json())

# convert the object into a dict
gchat_notification_channel_options_v1_dict = gchat_notification_channel_options_v1_instance.to_dict()
# create an instance of GchatNotificationChannelOptionsV1 from a dict
gchat_notification_channel_options_v1_from_dict = GchatNotificationChannelOptionsV1.from_dict(gchat_notification_channel_options_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


