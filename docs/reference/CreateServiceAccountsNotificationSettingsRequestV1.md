# CreateServiceAccountsNotificationSettingsRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | Whether the notification settings are enabled or not. | 
**notification_channel_ids** | **List[int]** | The list of notification channel IDs to which the notifications are to be sent.\\ \\ Supported types are **EMAIL** and **SLACK**.  | 
**days_before_expiry** | **List[int]** | The number of days before the expiry of the service account when the notifications are to be sent. | [optional] [default to [30, 7, 1]]

## Example

```python
from sysdig_client.models.create_service_accounts_notification_settings_request_v1 import CreateServiceAccountsNotificationSettingsRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of CreateServiceAccountsNotificationSettingsRequestV1 from a JSON string
create_service_accounts_notification_settings_request_v1_instance = CreateServiceAccountsNotificationSettingsRequestV1.from_json(json)
# print the JSON string representation of the object
print(CreateServiceAccountsNotificationSettingsRequestV1.to_json())

# convert the object into a dict
create_service_accounts_notification_settings_request_v1_dict = create_service_accounts_notification_settings_request_v1_instance.to_dict()
# create an instance of CreateServiceAccountsNotificationSettingsRequestV1 from a dict
create_service_accounts_notification_settings_request_v1_from_dict = CreateServiceAccountsNotificationSettingsRequestV1.from_dict(create_service_accounts_notification_settings_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


