# ServiceAccountsNotificationSettingsResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | Whether the notification settings are enabled or not. | [optional] 
**notification_channel_ids** | **List[int]** | The list of notification channel IDs to which the notifications are to be sent.\\ \\ Supported types are **EMAIL** and **SLACK**.  | [optional] 
**days_before_expiry** | **List[int]** | The number of days before the expiry of the service account when the notifications are to be sent. | [optional] [default to [30, 7, 1]]

## Example

```python
from sysdig_client.models.service_accounts_notification_settings_response_v1 import ServiceAccountsNotificationSettingsResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountsNotificationSettingsResponseV1 from a JSON string
service_accounts_notification_settings_response_v1_instance = ServiceAccountsNotificationSettingsResponseV1.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountsNotificationSettingsResponseV1.to_json())

# convert the object into a dict
service_accounts_notification_settings_response_v1_dict = service_accounts_notification_settings_response_v1_instance.to_dict()
# create an instance of ServiceAccountsNotificationSettingsResponseV1 from a dict
service_accounts_notification_settings_response_v1_from_dict = ServiceAccountsNotificationSettingsResponseV1.from_dict(service_accounts_notification_settings_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


