# CreateSnsNotificationChannelRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**SnsNotificationChannelOptionsV1**](SnsNotificationChannelOptionsV1.md) |  | 

## Example

```python
from sysdig_client.models.create_sns_notification_channel_request_v1 import CreateSnsNotificationChannelRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSnsNotificationChannelRequestV1 from a JSON string
create_sns_notification_channel_request_v1_instance = CreateSnsNotificationChannelRequestV1.from_json(json)
# print the JSON string representation of the object
print(CreateSnsNotificationChannelRequestV1.to_json())

# convert the object into a dict
create_sns_notification_channel_request_v1_dict = create_sns_notification_channel_request_v1_instance.to_dict()
# create an instance of CreateSnsNotificationChannelRequestV1 from a dict
create_sns_notification_channel_request_v1_from_dict = CreateSnsNotificationChannelRequestV1.from_dict(create_sns_notification_channel_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


