# UpdateCustomWebhookNotificationChannelRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**CustomWebhookNotificationChannelOptionsV1**](CustomWebhookNotificationChannelOptionsV1.md) |  | 

## Example

```python
from sysdig_client.models.update_custom_webhook_notification_channel_request_v1 import UpdateCustomWebhookNotificationChannelRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomWebhookNotificationChannelRequestV1 from a JSON string
update_custom_webhook_notification_channel_request_v1_instance = UpdateCustomWebhookNotificationChannelRequestV1.from_json(json)
# print the JSON string representation of the object
print(UpdateCustomWebhookNotificationChannelRequestV1.to_json())

# convert the object into a dict
update_custom_webhook_notification_channel_request_v1_dict = update_custom_webhook_notification_channel_request_v1_instance.to_dict()
# create an instance of UpdateCustomWebhookNotificationChannelRequestV1 from a dict
update_custom_webhook_notification_channel_request_v1_from_dict = UpdateCustomWebhookNotificationChannelRequestV1.from_dict(update_custom_webhook_notification_channel_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


