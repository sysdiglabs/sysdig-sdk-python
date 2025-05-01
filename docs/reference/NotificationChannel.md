# NotificationChannel

Schema for a notification channel object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Notification channel Id | [optional] 
**type** | **str** | Notification channel type | [optional] 

## Example

```python
from sysdig_client.models.notification_channel import NotificationChannel

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationChannel from a JSON string
notification_channel_instance = NotificationChannel.from_json(json)
# print the JSON string representation of the object
print(NotificationChannel.to_json())

# convert the object into a dict
notification_channel_dict = notification_channel_instance.to_dict()
# create an instance of NotificationChannel from a dict
notification_channel_from_dict = NotificationChannel.from_dict(notification_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


