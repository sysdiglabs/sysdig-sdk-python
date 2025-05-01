# PagerDutyNotificationChannelResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**PagerDutyNotificationChannelOptionsV1**](PagerDutyNotificationChannelOptionsV1.md) |  | 

## Example

```python
from sysdig_client.models.pager_duty_notification_channel_response_v1 import PagerDutyNotificationChannelResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of PagerDutyNotificationChannelResponseV1 from a JSON string
pager_duty_notification_channel_response_v1_instance = PagerDutyNotificationChannelResponseV1.from_json(json)
# print the JSON string representation of the object
print(PagerDutyNotificationChannelResponseV1.to_json())

# convert the object into a dict
pager_duty_notification_channel_response_v1_dict = pager_duty_notification_channel_response_v1_instance.to_dict()
# create an instance of PagerDutyNotificationChannelResponseV1 from a dict
pager_duty_notification_channel_response_v1_from_dict = PagerDutyNotificationChannelResponseV1.from_dict(pager_duty_notification_channel_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


