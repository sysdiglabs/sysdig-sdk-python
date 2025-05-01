# GchatNotificationChannelResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**GchatNotificationChannelOptionsV1**](GchatNotificationChannelOptionsV1.md) |  | 

## Example

```python
from sysdig_client.models.gchat_notification_channel_response_v1 import GchatNotificationChannelResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of GchatNotificationChannelResponseV1 from a JSON string
gchat_notification_channel_response_v1_instance = GchatNotificationChannelResponseV1.from_json(json)
# print the JSON string representation of the object
print(GchatNotificationChannelResponseV1.to_json())

# convert the object into a dict
gchat_notification_channel_response_v1_dict = gchat_notification_channel_response_v1_instance.to_dict()
# create an instance of GchatNotificationChannelResponseV1 from a dict
gchat_notification_channel_response_v1_from_dict = GchatNotificationChannelResponseV1.from_dict(gchat_notification_channel_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


