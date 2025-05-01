# UpdateTeamEmailNotificationChannelRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**TeamEmailNotificationChannelOptionsV1**](TeamEmailNotificationChannelOptionsV1.md) |  | 

## Example

```python
from sysdig_client.models.update_team_email_notification_channel_request_v1 import UpdateTeamEmailNotificationChannelRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTeamEmailNotificationChannelRequestV1 from a JSON string
update_team_email_notification_channel_request_v1_instance = UpdateTeamEmailNotificationChannelRequestV1.from_json(json)
# print the JSON string representation of the object
print(UpdateTeamEmailNotificationChannelRequestV1.to_json())

# convert the object into a dict
update_team_email_notification_channel_request_v1_dict = update_team_email_notification_channel_request_v1_instance.to_dict()
# create an instance of UpdateTeamEmailNotificationChannelRequestV1 from a dict
update_team_email_notification_channel_request_v1_from_dict = UpdateTeamEmailNotificationChannelRequestV1.from_dict(update_team_email_notification_channel_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


