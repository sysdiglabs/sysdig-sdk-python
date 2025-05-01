# WorkloadCostTrendsDataResponseTotal

Aggregated cost values for the current and previous ranges.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **float** | The total cost for the current range. | [optional] 
**previous** | **float** | The total cost for the previous range. | [optional] 
**change** | **float** | The difference between the current and the previous cost periods expressed in percentages. | [optional] 

## Example

```python
from sysdig_client.models.workload_cost_trends_data_response_total import WorkloadCostTrendsDataResponseTotal

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadCostTrendsDataResponseTotal from a JSON string
workload_cost_trends_data_response_total_instance = WorkloadCostTrendsDataResponseTotal.from_json(json)
# print the JSON string representation of the object
print(WorkloadCostTrendsDataResponseTotal.to_json())

# convert the object into a dict
workload_cost_trends_data_response_total_dict = workload_cost_trends_data_response_total_instance.to_dict()
# create an instance of WorkloadCostTrendsDataResponseTotal from a dict
workload_cost_trends_data_response_total_from_dict = WorkloadCostTrendsDataResponseTotal.from_dict(workload_cost_trends_data_response_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


