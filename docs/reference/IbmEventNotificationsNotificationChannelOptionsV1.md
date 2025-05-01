# IbmEventNotificationsNotificationChannelOptionsV1

The IBM Event Notifications notification channel options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_hiding_of_sensitive_info** | **bool** | Whether the notification info should be hidden when notifications are sent to this notification channel | [optional] 
**instance_id** | **str** | The IBM Event Notification Service Instance Id | 

## Example

```python
from sysdig_client.models.ibm_event_notifications_notification_channel_options_v1 import IbmEventNotificationsNotificationChannelOptionsV1

# TODO update the JSON string below
json = "{}"
# create an instance of IbmEventNotificationsNotificationChannelOptionsV1 from a JSON string
ibm_event_notifications_notification_channel_options_v1_instance = IbmEventNotificationsNotificationChannelOptionsV1.from_json(json)
# print the JSON string representation of the object
print(IbmEventNotificationsNotificationChannelOptionsV1.to_json())

# convert the object into a dict
ibm_event_notifications_notification_channel_options_v1_dict = ibm_event_notifications_notification_channel_options_v1_instance.to_dict()
# create an instance of IbmEventNotificationsNotificationChannelOptionsV1 from a dict
ibm_event_notifications_notification_channel_options_v1_from_dict = IbmEventNotificationsNotificationChannelOptionsV1.from_dict(ibm_event_notifications_notification_channel_options_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


