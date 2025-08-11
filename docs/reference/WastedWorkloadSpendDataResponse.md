# WastedWorkloadSpendDataResponse

Aggregated and grouped cost data representing Wasted Workload Spend over a specific date range.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | [**WastedWorkloadSpendDataResponseTotal**](WastedWorkloadSpendDataResponseTotal.md) |  | [optional]
**group_by_data** | [**List[WastedWorkloadSpendDataResponseGroupByDataInner]**](WastedWorkloadSpendDataResponseGroupByDataInner.md) | Grouped cost data for each combination of Prometheus label values. | [optional]

## Example

```python
from sysdig_client.models.wasted_workload_spend_data_response import WastedWorkloadSpendDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WastedWorkloadSpendDataResponse from a JSON string
wasted_workload_spend_data_response_instance = WastedWorkloadSpendDataResponse.from_json(json)
# print the JSON string representation of the object
print(WastedWorkloadSpendDataResponse.to_json())

# convert the object into a dict
wasted_workload_spend_data_response_dict = wasted_workload_spend_data_response_instance.to_dict()
# create an instance of WastedWorkloadSpendDataResponse from a dict
wasted_workload_spend_data_response_from_dict = WastedWorkloadSpendDataResponse.from_dict(wasted_workload_spend_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


