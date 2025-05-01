# SlackBaseNotificationChannelOptionsV1

The Slack base notification channel options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** | The name of the Slack channel the user selected as a destination for messages. | [optional] 
**url** | **str** | The Slack webhook URL | 

## Example

```python
from sysdig_client.models.slack_base_notification_channel_options_v1 import SlackBaseNotificationChannelOptionsV1

# TODO update the JSON string below
json = "{}"
# create an instance of SlackBaseNotificationChannelOptionsV1 from a JSON string
slack_base_notification_channel_options_v1_instance = SlackBaseNotificationChannelOptionsV1.from_json(json)
# print the JSON string representation of the object
print(SlackBaseNotificationChannelOptionsV1.to_json())

# convert the object into a dict
slack_base_notification_channel_options_v1_dict = slack_base_notification_channel_options_v1_instance.to_dict()
# create an instance of SlackBaseNotificationChannelOptionsV1 from a dict
slack_base_notification_channel_options_v1_from_dict = SlackBaseNotificationChannelOptionsV1.from_dict(slack_base_notification_channel_options_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


