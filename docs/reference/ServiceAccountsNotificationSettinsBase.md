# ServiceAccountsNotificationSettinsBase

The base schema for the service accounts notification settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | Whether the notification settings are enabled or not. | [optional] 
**notification_channel_ids** | **List[int]** | The list of notification channel IDs to which the notifications are to be sent.\\ \\ Supported types are **EMAIL** and **SLACK**.  | [optional] 
**days_before_expiry** | **List[int]** | The number of days before the expiry of the service account when the notifications are to be sent. | [optional] [default to [30,7,1]]

## Example

```python
from sysdig_client.models.service_accounts_notification_settins_base import ServiceAccountsNotificationSettinsBase

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountsNotificationSettinsBase from a JSON string
service_accounts_notification_settins_base_instance = ServiceAccountsNotificationSettinsBase.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountsNotificationSettinsBase.to_json())

# convert the object into a dict
service_accounts_notification_settins_base_dict = service_accounts_notification_settins_base_instance.to_dict()
# create an instance of ServiceAccountsNotificationSettinsBase from a dict
service_accounts_notification_settins_base_from_dict = ServiceAccountsNotificationSettinsBase.from_dict(service_accounts_notification_settins_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


