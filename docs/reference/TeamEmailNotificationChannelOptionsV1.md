# TeamEmailNotificationChannelOptionsV1

The Team Email notification channel options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_hiding_of_sensitive_info** | **bool** | Whether the notification info should be hidden when notifications are sent to this notification channel | [optional] 
**team_id** | **int** | ID of team to notify | [optional] 
**is_include_admin_users** | **bool** | Whether the admin users of the team should be notified or not | [optional] 

## Example

```python
from sysdig_client.models.team_email_notification_channel_options_v1 import TeamEmailNotificationChannelOptionsV1

# TODO update the JSON string below
json = "{}"
# create an instance of TeamEmailNotificationChannelOptionsV1 from a JSON string
team_email_notification_channel_options_v1_instance = TeamEmailNotificationChannelOptionsV1.from_json(json)
# print the JSON string representation of the object
print(TeamEmailNotificationChannelOptionsV1.to_json())

# convert the object into a dict
team_email_notification_channel_options_v1_dict = team_email_notification_channel_options_v1_instance.to_dict()
# create an instance of TeamEmailNotificationChannelOptionsV1 from a dict
team_email_notification_channel_options_v1_from_dict = TeamEmailNotificationChannelOptionsV1.from_dict(team_email_notification_channel_options_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


