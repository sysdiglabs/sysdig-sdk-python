# TeamEmailNotificationChannelResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**TeamEmailNotificationChannelOptionsV1**](TeamEmailNotificationChannelOptionsV1.md) |  | 

## Example

```python
from sysdig_client.models.team_email_notification_channel_response_v1 import TeamEmailNotificationChannelResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of TeamEmailNotificationChannelResponseV1 from a JSON string
team_email_notification_channel_response_v1_instance = TeamEmailNotificationChannelResponseV1.from_json(json)
# print the JSON string representation of the object
print(TeamEmailNotificationChannelResponseV1.to_json())

# convert the object into a dict
team_email_notification_channel_response_v1_dict = team_email_notification_channel_response_v1_instance.to_dict()
# create an instance of TeamEmailNotificationChannelResponseV1 from a dict
team_email_notification_channel_response_v1_from_dict = TeamEmailNotificationChannelResponseV1.from_dict(team_email_notification_channel_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


