# CreateSnsNotificationChannelRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **int** | ID of team that owns the notification channel. If null, this will be a global notification channel | [optional] 
**is_enabled** | **bool** | Indicates if the notification channel is enabled or not. | [optional] [default to False]
**name** | **str** | Name of the notification channel. It must be unique. | 
**has_test_notification_enabled** | **bool** | Indicates whether or not a test notification should be sent upon creation or update of this notification channel resource | [optional] [default to False]
**options** | [**SnsNotificationChannelOptionsV1**](SnsNotificationChannelOptionsV1.md) |  | 

## Example

```python
from sysdig_client.models.create_sns_notification_channel_request_v1 import CreateSnsNotificationChannelRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSnsNotificationChannelRequestV1 from a JSON string
create_sns_notification_channel_request_v1_instance = CreateSnsNotificationChannelRequestV1.from_json(json)
# print the JSON string representation of the object
print(CreateSnsNotificationChannelRequestV1.to_json())

# convert the object into a dict
create_sns_notification_channel_request_v1_dict = create_sns_notification_channel_request_v1_instance.to_dict()
# create an instance of CreateSnsNotificationChannelRequestV1 from a dict
create_sns_notification_channel_request_v1_from_dict = CreateSnsNotificationChannelRequestV1.from_dict(create_sns_notification_channel_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


