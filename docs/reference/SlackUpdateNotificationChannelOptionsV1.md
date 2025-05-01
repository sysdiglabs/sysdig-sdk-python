# SlackUpdateNotificationChannelOptionsV1

The Slack update notification channel options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_hiding_of_sensitive_info** | **bool** | Whether the notification info should be hidden when notifications are sent to this notification channel | [optional] 
**channel** | **str** | The name of the Slack channel the user selected as a destination for messages. | [optional] 
**url** | **str** | The Slack webhook URL | 

## Example

```python
from sysdig_client.models.slack_update_notification_channel_options_v1 import SlackUpdateNotificationChannelOptionsV1

# TODO update the JSON string below
json = "{}"
# create an instance of SlackUpdateNotificationChannelOptionsV1 from a JSON string
slack_update_notification_channel_options_v1_instance = SlackUpdateNotificationChannelOptionsV1.from_json(json)
# print the JSON string representation of the object
print(SlackUpdateNotificationChannelOptionsV1.to_json())

# convert the object into a dict
slack_update_notification_channel_options_v1_dict = slack_update_notification_channel_options_v1_instance.to_dict()
# create an instance of SlackUpdateNotificationChannelOptionsV1 from a dict
slack_update_notification_channel_options_v1_from_dict = SlackUpdateNotificationChannelOptionsV1.from_dict(slack_update_notification_channel_options_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


