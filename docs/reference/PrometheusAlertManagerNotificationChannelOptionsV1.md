# PrometheusAlertManagerNotificationChannelOptionsV1

The Prometheus Alert Manager notification channel options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_hiding_of_sensitive_info** | **bool** | Whether the notification info should be hidden when notifications are sent to this notification channel | [optional] 
**url** | **str** | The prometheus alert manager url to which the request should be posted | 
**is_allows_insecure_connections** | **bool** | Specifies if the channel allows insecure connections (e.g. plain http, self-signed https) | [optional] 
**additional_headers** | **Dict[str, str]** | Additional headers to send in the request to the alert manager url | [optional] 

## Example

```python
from sysdig_client.models.prometheus_alert_manager_notification_channel_options_v1 import PrometheusAlertManagerNotificationChannelOptionsV1

# TODO update the JSON string below
json = "{}"
# create an instance of PrometheusAlertManagerNotificationChannelOptionsV1 from a JSON string
prometheus_alert_manager_notification_channel_options_v1_instance = PrometheusAlertManagerNotificationChannelOptionsV1.from_json(json)
# print the JSON string representation of the object
print(PrometheusAlertManagerNotificationChannelOptionsV1.to_json())

# convert the object into a dict
prometheus_alert_manager_notification_channel_options_v1_dict = prometheus_alert_manager_notification_channel_options_v1_instance.to_dict()
# create an instance of PrometheusAlertManagerNotificationChannelOptionsV1 from a dict
prometheus_alert_manager_notification_channel_options_v1_from_dict = PrometheusAlertManagerNotificationChannelOptionsV1.from_dict(prometheus_alert_manager_notification_channel_options_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


