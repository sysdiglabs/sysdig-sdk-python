# WorkloadCostTrendsDataResponse

Cost trends observed between two consecutive time periods in the past.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_range** | [**WorkloadCostTrendsDataResponseCurrentRange**](WorkloadCostTrendsDataResponseCurrentRange.md) |  | [optional] 
**previous_range** | [**WorkloadCostTrendsDataResponsePreviousRange**](WorkloadCostTrendsDataResponsePreviousRange.md) |  | [optional] 
**total** | [**WorkloadCostTrendsDataResponseTotal**](WorkloadCostTrendsDataResponseTotal.md) |  | [optional] 
**scope** | [**List[PromqlMatcher]**](PromqlMatcher.md) | A list of PromQL-style filters. | [optional] 
**group_by** | **List[str]** | The label keys used to group the returned cost data. | [optional] 
**group_by_data** | [**List[WorkloadCostTrendsDataResponseGroupByDataInner]**](WorkloadCostTrendsDataResponseGroupByDataInner.md) | Grouped cost data for each combination of label values. | [optional] 

## Example

```python
from sysdig_client.models.workload_cost_trends_data_response import WorkloadCostTrendsDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadCostTrendsDataResponse from a JSON string
workload_cost_trends_data_response_instance = WorkloadCostTrendsDataResponse.from_json(json)
# print the JSON string representation of the object
print(WorkloadCostTrendsDataResponse.to_json())

# convert the object into a dict
workload_cost_trends_data_response_dict = workload_cost_trends_data_response_instance.to_dict()
# create an instance of WorkloadCostTrendsDataResponse from a dict
workload_cost_trends_data_response_from_dict = WorkloadCostTrendsDataResponse.from_dict(workload_cost_trends_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


