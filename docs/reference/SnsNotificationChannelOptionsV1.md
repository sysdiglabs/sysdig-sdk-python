# SnsNotificationChannelOptionsV1

The Amazon SNS notification channel options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_hiding_of_sensitive_info** | **bool** | Whether the notification info should be hidden when notifications are sent to this notification channel | [optional] 
**sns_topic_arns** | **List[str]** | List of sns topic ARNs (Amazon Resource Names) to which notifications should be sent | [optional] 

## Example

```python
from sysdig_client.models.sns_notification_channel_options_v1 import SnsNotificationChannelOptionsV1

# TODO update the JSON string below
json = "{}"
# create an instance of SnsNotificationChannelOptionsV1 from a JSON string
sns_notification_channel_options_v1_instance = SnsNotificationChannelOptionsV1.from_json(json)
# print the JSON string representation of the object
print(SnsNotificationChannelOptionsV1.to_json())

# convert the object into a dict
sns_notification_channel_options_v1_dict = sns_notification_channel_options_v1_instance.to_dict()
# create an instance of SnsNotificationChannelOptionsV1 from a dict
sns_notification_channel_options_v1_from_dict = SnsNotificationChannelOptionsV1.from_dict(sns_notification_channel_options_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


