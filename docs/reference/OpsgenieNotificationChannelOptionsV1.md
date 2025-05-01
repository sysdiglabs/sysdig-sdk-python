# OpsgenieNotificationChannelOptionsV1

The Opsgenie notification channel options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_hiding_of_sensitive_info** | **bool** | Whether the notification info should be hidden when notifications are sent to this notification channel | [optional] 
**region** | **str** | The Opsgenie region to use | [optional] 
**api_key** | **str** | The Opsgenie api key | 

## Example

```python
from sysdig_client.models.opsgenie_notification_channel_options_v1 import OpsgenieNotificationChannelOptionsV1

# TODO update the JSON string below
json = "{}"
# create an instance of OpsgenieNotificationChannelOptionsV1 from a JSON string
opsgenie_notification_channel_options_v1_instance = OpsgenieNotificationChannelOptionsV1.from_json(json)
# print the JSON string representation of the object
print(OpsgenieNotificationChannelOptionsV1.to_json())

# convert the object into a dict
opsgenie_notification_channel_options_v1_dict = opsgenie_notification_channel_options_v1_instance.to_dict()
# create an instance of OpsgenieNotificationChannelOptionsV1 from a dict
opsgenie_notification_channel_options_v1_from_dict = OpsgenieNotificationChannelOptionsV1.from_dict(opsgenie_notification_channel_options_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


