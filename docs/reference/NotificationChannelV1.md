# NotificationChannelV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **int** | ID of team that owns the notification channel. If null, this will be a global notification channel | [optional] 
**is_enabled** | **bool** | Indicates if the notification channel is enabled or not. | [optional] [default to False]
**name** | **str** | Name of the notification channel. It must be unique. | 
**has_test_notification_enabled** | **bool** | Indicates whether or not a test notification should be sent upon creation or update of this notification channel resource | [optional] [default to False]

## Example

```python
from sysdig_client.models.notification_channel_v1 import NotificationChannelV1

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationChannelV1 from a JSON string
notification_channel_v1_instance = NotificationChannelV1.from_json(json)
# print the JSON string representation of the object
print(NotificationChannelV1.to_json())

# convert the object into a dict
notification_channel_v1_dict = notification_channel_v1_instance.to_dict()
# create an instance of NotificationChannelV1 from a dict
notification_channel_v1_from_dict = NotificationChannelV1.from_dict(notification_channel_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


