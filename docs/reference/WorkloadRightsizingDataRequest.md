# WorkloadRightsizingDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_range** | [**DateRange**](DateRange.md) |  | 
**algorithm** | **str** | Aggregation algorithm used for rightsizing analysis. Currently supported values are: - AVG  - P95  - MAX This field is case-sensitive and may support more values in the future.  | 
**scope** | [**List[PromqlMatcher]**](PromqlMatcher.md) | A list of PromQL-style filters | [optional] 

## Example

```python
from sysdig_client.models.workload_rightsizing_data_request import WorkloadRightsizingDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadRightsizingDataRequest from a JSON string
workload_rightsizing_data_request_instance = WorkloadRightsizingDataRequest.from_json(json)
# print the JSON string representation of the object
print(WorkloadRightsizingDataRequest.to_json())

# convert the object into a dict
workload_rightsizing_data_request_dict = workload_rightsizing_data_request_instance.to_dict()
# create an instance of WorkloadRightsizingDataRequest from a dict
workload_rightsizing_data_request_from_dict = WorkloadRightsizingDataRequest.from_dict(workload_rightsizing_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


