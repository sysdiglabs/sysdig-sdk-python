# OpsgenieNotificationChannelResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**OpsgenieNotificationChannelOptionsV1**](OpsgenieNotificationChannelOptionsV1.md) |  | 

## Example

```python
from sysdig_client.models.opsgenie_notification_channel_response_v1 import OpsgenieNotificationChannelResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of OpsgenieNotificationChannelResponseV1 from a JSON string
opsgenie_notification_channel_response_v1_instance = OpsgenieNotificationChannelResponseV1.from_json(json)
# print the JSON string representation of the object
print(OpsgenieNotificationChannelResponseV1.to_json())

# convert the object into a dict
opsgenie_notification_channel_response_v1_dict = opsgenie_notification_channel_response_v1_instance.to_dict()
# create an instance of OpsgenieNotificationChannelResponseV1 from a dict
opsgenie_notification_channel_response_v1_from_dict = OpsgenieNotificationChannelResponseV1.from_dict(opsgenie_notification_channel_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


