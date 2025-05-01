# VictorOpsNotificationChannelOptionsV1

The VictorOps notification channel options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_hiding_of_sensitive_info** | **bool** | Whether the notification info should be hidden when notifications are sent to this notification channel | [optional] 
**api_key** | **str** | The VictorOps api key | [optional] 
**routing_key** | **str** | The VictorOps routing key | [optional] 

## Example

```python
from sysdig_client.models.victor_ops_notification_channel_options_v1 import VictorOpsNotificationChannelOptionsV1

# TODO update the JSON string below
json = "{}"
# create an instance of VictorOpsNotificationChannelOptionsV1 from a JSON string
victor_ops_notification_channel_options_v1_instance = VictorOpsNotificationChannelOptionsV1.from_json(json)
# print the JSON string representation of the object
print(VictorOpsNotificationChannelOptionsV1.to_json())

# convert the object into a dict
victor_ops_notification_channel_options_v1_dict = victor_ops_notification_channel_options_v1_instance.to_dict()
# create an instance of VictorOpsNotificationChannelOptionsV1 from a dict
victor_ops_notification_channel_options_v1_from_dict = VictorOpsNotificationChannelOptionsV1.from_dict(victor_ops_notification_channel_options_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


