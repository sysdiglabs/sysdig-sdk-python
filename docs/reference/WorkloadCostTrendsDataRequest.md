# WorkloadCostTrendsDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trend_range_in_days** | **float** | Specifies the number of days used to calculate and extract cost data. Must be a positive integer.  | 
**var_date** | **date** | The reference date used to define the time window for cost trend calculation. When combined with &#x60;trendRangeInDays&#x60;, this date represents the exclusive upper bound of the time range — the trend is calculated from (&#x60;date - trendRangeInDays&#x60;) up to but not including &#x60;date&#x60;. For example, if &#x60;date&#x60; is 2025-02-12 and &#x60;trendRangeInDays&#x60; is 10, the time range used for calculation is from 2025-02-02 to 2025-02-11 (inclusive).  Must be in YYYY-MM-DD format.  | 
**scope** | [**List[PromqlMatcher]**](PromqlMatcher.md) | A list of PromQL-style filters | [optional] 
**group_by** | **List[str]** |  | [optional] 

## Example

```python
from sysdig_client.models.workload_cost_trends_data_request import WorkloadCostTrendsDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadCostTrendsDataRequest from a JSON string
workload_cost_trends_data_request_instance = WorkloadCostTrendsDataRequest.from_json(json)
# print the JSON string representation of the object
print(WorkloadCostTrendsDataRequest.to_json())

# convert the object into a dict
workload_cost_trends_data_request_dict = workload_cost_trends_data_request_instance.to_dict()
# create an instance of WorkloadCostTrendsDataRequest from a dict
workload_cost_trends_data_request_from_dict = WorkloadCostTrendsDataRequest.from_dict(workload_cost_trends_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


