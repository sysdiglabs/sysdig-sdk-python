# EmailNotificationChannelResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**EmailNotificationChannelOptionsV1**](EmailNotificationChannelOptionsV1.md) |  | 

## Example

```python
from sysdig_client.models.email_notification_channel_response_v1 import EmailNotificationChannelResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of EmailNotificationChannelResponseV1 from a JSON string
email_notification_channel_response_v1_instance = EmailNotificationChannelResponseV1.from_json(json)
# print the JSON string representation of the object
print(EmailNotificationChannelResponseV1.to_json())

# convert the object into a dict
email_notification_channel_response_v1_dict = email_notification_channel_response_v1_instance.to_dict()
# create an instance of EmailNotificationChannelResponseV1 from a dict
email_notification_channel_response_v1_from_dict = EmailNotificationChannelResponseV1.from_dict(email_notification_channel_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


