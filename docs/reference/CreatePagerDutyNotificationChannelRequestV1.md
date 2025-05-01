# CreatePagerDutyNotificationChannelRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**PagerDutyNotificationChannelOptionsV1**](PagerDutyNotificationChannelOptionsV1.md) |  | 

## Example

```python
from sysdig_client.models.create_pager_duty_notification_channel_request_v1 import CreatePagerDutyNotificationChannelRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePagerDutyNotificationChannelRequestV1 from a JSON string
create_pager_duty_notification_channel_request_v1_instance = CreatePagerDutyNotificationChannelRequestV1.from_json(json)
# print the JSON string representation of the object
print(CreatePagerDutyNotificationChannelRequestV1.to_json())

# convert the object into a dict
create_pager_duty_notification_channel_request_v1_dict = create_pager_duty_notification_channel_request_v1_instance.to_dict()
# create an instance of CreatePagerDutyNotificationChannelRequestV1 from a dict
create_pager_duty_notification_channel_request_v1_from_dict = CreatePagerDutyNotificationChannelRequestV1.from_dict(create_pager_duty_notification_channel_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


