# PagerDutyNotificationChannelOptionsV1

The PagerDuty notification channel options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_hiding_of_sensitive_info** | **bool** | Whether the notification info should be hidden when notifications are sent to this notification channel | [optional] 
**account** | **str** | The PagerDuty account used for the integration | 
**service_key** | **str** | The PagerDuty service integration key | 
**service_name** | **str** | The PagerDuty service name | 

## Example

```python
from sysdig_client.models.pager_duty_notification_channel_options_v1 import PagerDutyNotificationChannelOptionsV1

# TODO update the JSON string below
json = "{}"
# create an instance of PagerDutyNotificationChannelOptionsV1 from a JSON string
pager_duty_notification_channel_options_v1_instance = PagerDutyNotificationChannelOptionsV1.from_json(json)
# print the JSON string representation of the object
print(PagerDutyNotificationChannelOptionsV1.to_json())

# convert the object into a dict
pager_duty_notification_channel_options_v1_dict = pager_duty_notification_channel_options_v1_instance.to_dict()
# create an instance of PagerDutyNotificationChannelOptionsV1 from a dict
pager_duty_notification_channel_options_v1_from_dict = PagerDutyNotificationChannelOptionsV1.from_dict(pager_duty_notification_channel_options_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


