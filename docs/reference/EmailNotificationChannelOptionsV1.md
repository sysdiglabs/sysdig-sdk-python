# EmailNotificationChannelOptionsV1

The email notification channel options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_hiding_of_sensitive_info** | **bool** | Whether the notification info should be hidden when notifications are sent to this notification channel | [optional] 
**email_recipients** | **List[str]** | List of email recipients to which notifications should be sent | 

## Example

```python
from sysdig_client.models.email_notification_channel_options_v1 import EmailNotificationChannelOptionsV1

# TODO update the JSON string below
json = "{}"
# create an instance of EmailNotificationChannelOptionsV1 from a JSON string
email_notification_channel_options_v1_instance = EmailNotificationChannelOptionsV1.from_json(json)
# print the JSON string representation of the object
print(EmailNotificationChannelOptionsV1.to_json())

# convert the object into a dict
email_notification_channel_options_v1_dict = email_notification_channel_options_v1_instance.to_dict()
# create an instance of EmailNotificationChannelOptionsV1 from a dict
email_notification_channel_options_v1_from_dict = EmailNotificationChannelOptionsV1.from_dict(email_notification_channel_options_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


