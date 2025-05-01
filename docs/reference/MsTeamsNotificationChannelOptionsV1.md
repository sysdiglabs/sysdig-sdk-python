# MsTeamsNotificationChannelOptionsV1

The Microsoft Teams notification channel options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_hiding_of_sensitive_info** | **bool** | Whether the notification info should be hidden when notifications are sent to this notification channel | [optional] 
**url** | **str** | Microsoft Teams Webhook URL | 

## Example

```python
from sysdig_client.models.ms_teams_notification_channel_options_v1 import MsTeamsNotificationChannelOptionsV1

# TODO update the JSON string below
json = "{}"
# create an instance of MsTeamsNotificationChannelOptionsV1 from a JSON string
ms_teams_notification_channel_options_v1_instance = MsTeamsNotificationChannelOptionsV1.from_json(json)
# print the JSON string representation of the object
print(MsTeamsNotificationChannelOptionsV1.to_json())

# convert the object into a dict
ms_teams_notification_channel_options_v1_dict = ms_teams_notification_channel_options_v1_instance.to_dict()
# create an instance of MsTeamsNotificationChannelOptionsV1 from a dict
ms_teams_notification_channel_options_v1_from_dict = MsTeamsNotificationChannelOptionsV1.from_dict(ms_teams_notification_channel_options_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


