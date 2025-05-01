# UpdateEmailNotificationChannelRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**EmailNotificationChannelOptionsV1**](EmailNotificationChannelOptionsV1.md) |  | 

## Example

```python
from sysdig_client.models.update_email_notification_channel_request_v1 import UpdateEmailNotificationChannelRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEmailNotificationChannelRequestV1 from a JSON string
update_email_notification_channel_request_v1_instance = UpdateEmailNotificationChannelRequestV1.from_json(json)
# print the JSON string representation of the object
print(UpdateEmailNotificationChannelRequestV1.to_json())

# convert the object into a dict
update_email_notification_channel_request_v1_dict = update_email_notification_channel_request_v1_instance.to_dict()
# create an instance of UpdateEmailNotificationChannelRequestV1 from a dict
update_email_notification_channel_request_v1_from_dict = UpdateEmailNotificationChannelRequestV1.from_dict(update_email_notification_channel_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


