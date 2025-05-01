# SlackNotificationChannelResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**SlackReadNotificationChannelOptionsV1**](SlackReadNotificationChannelOptionsV1.md) |  | 

## Example

```python
from sysdig_client.models.slack_notification_channel_response_v1 import SlackNotificationChannelResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of SlackNotificationChannelResponseV1 from a JSON string
slack_notification_channel_response_v1_instance = SlackNotificationChannelResponseV1.from_json(json)
# print the JSON string representation of the object
print(SlackNotificationChannelResponseV1.to_json())

# convert the object into a dict
slack_notification_channel_response_v1_dict = slack_notification_channel_response_v1_instance.to_dict()
# create an instance of SlackNotificationChannelResponseV1 from a dict
slack_notification_channel_response_v1_from_dict = SlackNotificationChannelResponseV1.from_dict(slack_notification_channel_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


