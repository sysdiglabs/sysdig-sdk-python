# UpdatePagerDutyNotificationChannelRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**PagerDutyNotificationChannelOptionsV1**](PagerDutyNotificationChannelOptionsV1.md) |  | 

## Example

```python
from sysdig_client.models.update_pager_duty_notification_channel_request_v1 import UpdatePagerDutyNotificationChannelRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePagerDutyNotificationChannelRequestV1 from a JSON string
update_pager_duty_notification_channel_request_v1_instance = UpdatePagerDutyNotificationChannelRequestV1.from_json(json)
# print the JSON string representation of the object
print(UpdatePagerDutyNotificationChannelRequestV1.to_json())

# convert the object into a dict
update_pager_duty_notification_channel_request_v1_dict = update_pager_duty_notification_channel_request_v1_instance.to_dict()
# create an instance of UpdatePagerDutyNotificationChannelRequestV1 from a dict
update_pager_duty_notification_channel_request_v1_from_dict = UpdatePagerDutyNotificationChannelRequestV1.from_dict(update_pager_duty_notification_channel_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


