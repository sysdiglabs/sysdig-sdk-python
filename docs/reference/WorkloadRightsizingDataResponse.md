# WorkloadRightsizingDataResponse

Cost data representing Workload Rightsizing over a specific date range.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by_data** | [**List[WorkloadRightsizingDataResponseGroupByDataInner]**](WorkloadRightsizingDataResponseGroupByDataInner.md) | Grouped workload rightsizing data by cluster, namespace, workload, and container. | [optional]

## Example

```python
from sysdig_client.models.workload_rightsizing_data_response import WorkloadRightsizingDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadRightsizingDataResponse from a JSON string
workload_rightsizing_data_response_instance = WorkloadRightsizingDataResponse.from_json(json)
# print the JSON string representation of the object
print(WorkloadRightsizingDataResponse.to_json())

# convert the object into a dict
workload_rightsizing_data_response_dict = workload_rightsizing_data_response_instance.to_dict()
# create an instance of WorkloadRightsizingDataResponse from a dict
workload_rightsizing_data_response_from_dict = WorkloadRightsizingDataResponse.from_dict(workload_rightsizing_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


