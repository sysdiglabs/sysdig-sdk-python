# UpdateServiceAccountsNotificationSettingsRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | Whether the notification settings are enabled or not. | 
**notification_channel_ids** | **List[int]** | The list of notification channel IDs to which the notifications are to be sent.\\ \\ Supported types are **EMAIL** and **SLACK**.  | 
**days_before_expiry** | **List[int]** | The number of days before the expiry of the service account when the notifications are to be sent. | [default to [30, 7, 1]]

## Example

```python
from sysdig_client.models.update_service_accounts_notification_settings_request_v1 import UpdateServiceAccountsNotificationSettingsRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateServiceAccountsNotificationSettingsRequestV1 from a JSON string
update_service_accounts_notification_settings_request_v1_instance = UpdateServiceAccountsNotificationSettingsRequestV1.from_json(json)
# print the JSON string representation of the object
print(UpdateServiceAccountsNotificationSettingsRequestV1.to_json())

# convert the object into a dict
update_service_accounts_notification_settings_request_v1_dict = update_service_accounts_notification_settings_request_v1_instance.to_dict()
# create an instance of UpdateServiceAccountsNotificationSettingsRequestV1 from a dict
update_service_accounts_notification_settings_request_v1_from_dict = UpdateServiceAccountsNotificationSettingsRequestV1.from_dict(update_service_accounts_notification_settings_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


