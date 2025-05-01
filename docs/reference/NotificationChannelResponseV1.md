# NotificationChannelResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **int** | ID of team that owns the notification channel. If null, this will be a global notification channel | [optional] 
**is_enabled** | **bool** | Indicates if the notification channel is enabled or not. | [optional] [default to False]
**name** | **str** | Name of the notification channel. It must be unique. | 
**has_test_notification_enabled** | **bool** | Indicates whether or not a test notification should be sent upon creation or update of this notification channel resource | [optional] [default to False]
**type** | **str** |  | 
**customer_id** | **int** | ID of customer that owns the notification channel. | [optional] 
**id** | **int** | Unique ID of the resource. | [optional] 
**version** | **int** | The current version of the resource. | [optional] 
**created_on** | **datetime** | Creation date. | [optional] 
**modified_on** | **datetime** | Last modification date. | [optional] 

## Example

```python
from sysdig_client.models.notification_channel_response_v1 import NotificationChannelResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationChannelResponseV1 from a JSON string
notification_channel_response_v1_instance = NotificationChannelResponseV1.from_json(json)
# print the JSON string representation of the object
print(NotificationChannelResponseV1.to_json())

# convert the object into a dict
notification_channel_response_v1_dict = notification_channel_response_v1_instance.to_dict()
# create an instance of NotificationChannelResponseV1 from a dict
notification_channel_response_v1_from_dict = NotificationChannelResponseV1.from_dict(notification_channel_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


