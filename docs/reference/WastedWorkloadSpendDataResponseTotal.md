# WastedWorkloadSpendDataResponseTotal

Aggregated cost values for the specified time range.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accrued** | **float** | Total cost accrued during the reporting period. | [optional]
**estimated** | **float** | Estimated efficient cost during the reporting period. | [optional]
**wasted** | **float** | Difference between accrued and estimated cost. | [optional]

## Example

```python
from sysdig_client.models.wasted_workload_spend_data_response_total import WastedWorkloadSpendDataResponseTotal

# TODO update the JSON string below
json = "{}"
# create an instance of WastedWorkloadSpendDataResponseTotal from a JSON string
wasted_workload_spend_data_response_total_instance = WastedWorkloadSpendDataResponseTotal.from_json(json)
# print the JSON string representation of the object
print(WastedWorkloadSpendDataResponseTotal.to_json())

# convert the object into a dict
wasted_workload_spend_data_response_total_dict = wasted_workload_spend_data_response_total_instance.to_dict()
# create an instance of WastedWorkloadSpendDataResponseTotal from a dict
wasted_workload_spend_data_response_total_from_dict = WastedWorkloadSpendDataResponseTotal.from_dict(wasted_workload_spend_data_response_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


