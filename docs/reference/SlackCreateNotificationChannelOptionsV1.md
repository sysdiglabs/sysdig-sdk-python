# SlackCreateNotificationChannelOptionsV1

The Slack create notification channel options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_hiding_of_sensitive_info** | **bool** | Whether the notification info should be hidden when notifications are sent to this notification channel | [optional] 
**channel** | **str** | The name of the Slack channel the user selected as a destination for messages. | [optional] 
**url** | **str** | The Slack webhook URL | 
**is_private_channel** | **bool** | Whether the Slack channel is private or not | [optional] 
**private_channel_url** | **str** | The channel URL, if channel is private | [optional] 

## Example

```python
from sysdig_client.models.slack_create_notification_channel_options_v1 import SlackCreateNotificationChannelOptionsV1

# TODO update the JSON string below
json = "{}"
# create an instance of SlackCreateNotificationChannelOptionsV1 from a JSON string
slack_create_notification_channel_options_v1_instance = SlackCreateNotificationChannelOptionsV1.from_json(json)
# print the JSON string representation of the object
print(SlackCreateNotificationChannelOptionsV1.to_json())

# convert the object into a dict
slack_create_notification_channel_options_v1_dict = slack_create_notification_channel_options_v1_instance.to_dict()
# create an instance of SlackCreateNotificationChannelOptionsV1 from a dict
slack_create_notification_channel_options_v1_from_dict = SlackCreateNotificationChannelOptionsV1.from_dict(slack_create_notification_channel_options_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


