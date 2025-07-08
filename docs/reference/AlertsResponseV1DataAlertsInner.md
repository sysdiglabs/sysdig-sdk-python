# AlertsResponseV1DataAlertsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_at** | **datetime** | Timestamp when the alert became active. | 
**annotations** | **Dict[str, str]** | Additional metadata about the alert. | 
**labels** | **Dict[str, str]** | Key-value pairs identifying the alert. | 
**state** | **str** | Current state of the alert. | 
**value** | **str** | The numerical value that triggered the alert. | 

## Example

```python
from sysdig_client.models.alerts_response_v1_data_alerts_inner import AlertsResponseV1DataAlertsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AlertsResponseV1DataAlertsInner from a JSON string
alerts_response_v1_data_alerts_inner_instance = AlertsResponseV1DataAlertsInner.from_json(json)
# print the JSON string representation of the object
print(AlertsResponseV1DataAlertsInner.to_json())

# convert the object into a dict
alerts_response_v1_data_alerts_inner_dict = alerts_response_v1_data_alerts_inner_instance.to_dict()
# create an instance of AlertsResponseV1DataAlertsInner from a dict
alerts_response_v1_data_alerts_inner_from_dict = AlertsResponseV1DataAlertsInner.from_dict(alerts_response_v1_data_alerts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


