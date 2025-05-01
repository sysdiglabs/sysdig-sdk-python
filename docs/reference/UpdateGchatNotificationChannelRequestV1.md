# UpdateGchatNotificationChannelRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**GchatNotificationChannelOptionsV1**](GchatNotificationChannelOptionsV1.md) |  | 

## Example

```python
from sysdig_client.models.update_gchat_notification_channel_request_v1 import UpdateGchatNotificationChannelRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGchatNotificationChannelRequestV1 from a JSON string
update_gchat_notification_channel_request_v1_instance = UpdateGchatNotificationChannelRequestV1.from_json(json)
# print the JSON string representation of the object
print(UpdateGchatNotificationChannelRequestV1.to_json())

# convert the object into a dict
update_gchat_notification_channel_request_v1_dict = update_gchat_notification_channel_request_v1_instance.to_dict()
# create an instance of UpdateGchatNotificationChannelRequestV1 from a dict
update_gchat_notification_channel_request_v1_from_dict = UpdateGchatNotificationChannelRequestV1.from_dict(update_gchat_notification_channel_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


