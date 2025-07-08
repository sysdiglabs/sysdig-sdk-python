# AlertsResponseV1Data

Response payload containing active alerts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts** | [**List[AlertsResponseV1DataAlertsInner]**](AlertsResponseV1DataAlertsInner.md) | List of currently active alerts. | [optional] 

## Example

```python
from sysdig_client.models.alerts_response_v1_data import AlertsResponseV1Data

# TODO update the JSON string below
json = "{}"
# create an instance of AlertsResponseV1Data from a JSON string
alerts_response_v1_data_instance = AlertsResponseV1Data.from_json(json)
# print the JSON string representation of the object
print(AlertsResponseV1Data.to_json())

# convert the object into a dict
alerts_response_v1_data_dict = alerts_response_v1_data_instance.to_dict()
# create an instance of AlertsResponseV1Data from a dict
alerts_response_v1_data_from_dict = AlertsResponseV1Data.from_dict(alerts_response_v1_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


