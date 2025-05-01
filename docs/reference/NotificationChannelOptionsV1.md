# NotificationChannelOptionsV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_hiding_of_sensitive_info** | **bool** | Whether the notification info should be hidden when notifications are sent to this notification channel | [optional] 

## Example

```python
from sysdig_client.models.notification_channel_options_v1 import NotificationChannelOptionsV1

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationChannelOptionsV1 from a JSON string
notification_channel_options_v1_instance = NotificationChannelOptionsV1.from_json(json)
# print the JSON string representation of the object
print(NotificationChannelOptionsV1.to_json())

# convert the object into a dict
notification_channel_options_v1_dict = notification_channel_options_v1_instance.to_dict()
# create an instance of NotificationChannelOptionsV1 from a dict
notification_channel_options_v1_from_dict = NotificationChannelOptionsV1.from_dict(notification_channel_options_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


