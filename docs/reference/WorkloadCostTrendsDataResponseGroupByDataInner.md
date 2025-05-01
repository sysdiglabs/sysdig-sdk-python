# WorkloadCostTrendsDataResponseGroupByDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **Dict[str, str]** | Key-value pairs representing the grouping labels. | [optional] 
**current** | **float** | The cost for the current range within this group. | [optional] 
**previous** | **float** | The cost for the previous range within this group. | [optional] 
**change** | **float** | The difference in cost between current and previous ranges for this group. | [optional] 

## Example

```python
from sysdig_client.models.workload_cost_trends_data_response_group_by_data_inner import WorkloadCostTrendsDataResponseGroupByDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadCostTrendsDataResponseGroupByDataInner from a JSON string
workload_cost_trends_data_response_group_by_data_inner_instance = WorkloadCostTrendsDataResponseGroupByDataInner.from_json(json)
# print the JSON string representation of the object
print(WorkloadCostTrendsDataResponseGroupByDataInner.to_json())

# convert the object into a dict
workload_cost_trends_data_response_group_by_data_inner_dict = workload_cost_trends_data_response_group_by_data_inner_instance.to_dict()
# create an instance of WorkloadCostTrendsDataResponseGroupByDataInner from a dict
workload_cost_trends_data_response_group_by_data_inner_from_dict = WorkloadCostTrendsDataResponseGroupByDataInner.from_dict(workload_cost_trends_data_response_group_by_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


