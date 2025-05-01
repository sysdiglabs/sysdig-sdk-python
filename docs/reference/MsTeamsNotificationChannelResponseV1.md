# MsTeamsNotificationChannelResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**MsTeamsNotificationChannelOptionsV1**](MsTeamsNotificationChannelOptionsV1.md) |  | 

## Example

```python
from sysdig_client.models.ms_teams_notification_channel_response_v1 import MsTeamsNotificationChannelResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of MsTeamsNotificationChannelResponseV1 from a JSON string
ms_teams_notification_channel_response_v1_instance = MsTeamsNotificationChannelResponseV1.from_json(json)
# print the JSON string representation of the object
print(MsTeamsNotificationChannelResponseV1.to_json())

# convert the object into a dict
ms_teams_notification_channel_response_v1_dict = ms_teams_notification_channel_response_v1_instance.to_dict()
# create an instance of MsTeamsNotificationChannelResponseV1 from a dict
ms_teams_notification_channel_response_v1_from_dict = MsTeamsNotificationChannelResponseV1.from_dict(ms_teams_notification_channel_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


