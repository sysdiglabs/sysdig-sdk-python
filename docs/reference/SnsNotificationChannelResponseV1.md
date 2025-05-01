# SnsNotificationChannelResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**SnsNotificationChannelOptionsV1**](SnsNotificationChannelOptionsV1.md) |  | 

## Example

```python
from sysdig_client.models.sns_notification_channel_response_v1 import SnsNotificationChannelResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of SnsNotificationChannelResponseV1 from a JSON string
sns_notification_channel_response_v1_instance = SnsNotificationChannelResponseV1.from_json(json)
# print the JSON string representation of the object
print(SnsNotificationChannelResponseV1.to_json())

# convert the object into a dict
sns_notification_channel_response_v1_dict = sns_notification_channel_response_v1_instance.to_dict()
# create an instance of SnsNotificationChannelResponseV1 from a dict
sns_notification_channel_response_v1_from_dict = SnsNotificationChannelResponseV1.from_dict(sns_notification_channel_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


