# CreateVictorOpsNotificationChannelRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**VictorOpsNotificationChannelOptionsV1**](VictorOpsNotificationChannelOptionsV1.md) |  | 

## Example

```python
from sysdig_client.models.create_victor_ops_notification_channel_request_v1 import CreateVictorOpsNotificationChannelRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVictorOpsNotificationChannelRequestV1 from a JSON string
create_victor_ops_notification_channel_request_v1_instance = CreateVictorOpsNotificationChannelRequestV1.from_json(json)
# print the JSON string representation of the object
print(CreateVictorOpsNotificationChannelRequestV1.to_json())

# convert the object into a dict
create_victor_ops_notification_channel_request_v1_dict = create_victor_ops_notification_channel_request_v1_instance.to_dict()
# create an instance of CreateVictorOpsNotificationChannelRequestV1 from a dict
create_victor_ops_notification_channel_request_v1_from_dict = CreateVictorOpsNotificationChannelRequestV1.from_dict(create_victor_ops_notification_channel_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


