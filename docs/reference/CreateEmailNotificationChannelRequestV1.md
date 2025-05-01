# CreateEmailNotificationChannelRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**EmailNotificationChannelOptionsV1**](EmailNotificationChannelOptionsV1.md) |  | 

## Example

```python
from sysdig_client.models.create_email_notification_channel_request_v1 import CreateEmailNotificationChannelRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEmailNotificationChannelRequestV1 from a JSON string
create_email_notification_channel_request_v1_instance = CreateEmailNotificationChannelRequestV1.from_json(json)
# print the JSON string representation of the object
print(CreateEmailNotificationChannelRequestV1.to_json())

# convert the object into a dict
create_email_notification_channel_request_v1_dict = create_email_notification_channel_request_v1_instance.to_dict()
# create an instance of CreateEmailNotificationChannelRequestV1 from a dict
create_email_notification_channel_request_v1_from_dict = CreateEmailNotificationChannelRequestV1.from_dict(create_email_notification_channel_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


