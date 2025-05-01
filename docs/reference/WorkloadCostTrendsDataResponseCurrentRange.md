# WorkloadCostTrendsDataResponseCurrentRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | The beginning of the date range. | 
**end_date** | **date** | The end of the date range. | 

## Example

```python
from sysdig_client.models.workload_cost_trends_data_response_current_range import WorkloadCostTrendsDataResponseCurrentRange

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadCostTrendsDataResponseCurrentRange from a JSON string
workload_cost_trends_data_response_current_range_instance = WorkloadCostTrendsDataResponseCurrentRange.from_json(json)
# print the JSON string representation of the object
print(WorkloadCostTrendsDataResponseCurrentRange.to_json())

# convert the object into a dict
workload_cost_trends_data_response_current_range_dict = workload_cost_trends_data_response_current_range_instance.to_dict()
# create an instance of WorkloadCostTrendsDataResponseCurrentRange from a dict
workload_cost_trends_data_response_current_range_from_dict = WorkloadCostTrendsDataResponseCurrentRange.from_dict(workload_cost_trends_data_response_current_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


