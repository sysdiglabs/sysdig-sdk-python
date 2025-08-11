# WorkloadRightsizingDataResponseGroupByDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **Dict[str, str]** | Key-value pairs representing the logical grouping keys.  The data is grouped by the following dimensions: - cluster - namespace - workload - container  | [optional]
**suggested_cpu** | **float** | Suggested CPU allocation (in milicores). | [optional]
**suggested_memory** | **float** | Suggested memory allocation (in MiB). | [optional]
**monthly_cost** | **float** | Estimated current monthly cost in USD. | [optional]
**monthly_potential_savings** | **float** | Estimated potential monthly savings in USD. | [optional]
**workload_type** | **str** | Type of Kubernetes workload. Possible values include: - Deployment - StatefulSet - DaemonSet - Job - CronJob - ReplicaSet - ReplicationController  | [optional]
**number_of_pods** | **int** | Number of pods currently running in the workload. | [optional]
**requested_cpu** | **float** | CPU requested by the container (in milicores). | [optional]
**requested_memory** | **float** | Memory requested by the container (in MiB). | [optional]

## Example

```python
from sysdig_client.models.workload_rightsizing_data_response_group_by_data_inner import WorkloadRightsizingDataResponseGroupByDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadRightsizingDataResponseGroupByDataInner from a JSON string
workload_rightsizing_data_response_group_by_data_inner_instance = WorkloadRightsizingDataResponseGroupByDataInner.from_json(json)
# print the JSON string representation of the object
print(WorkloadRightsizingDataResponseGroupByDataInner.to_json())

# convert the object into a dict
workload_rightsizing_data_response_group_by_data_inner_dict = workload_rightsizing_data_response_group_by_data_inner_instance.to_dict()
# create an instance of WorkloadRightsizingDataResponseGroupByDataInner from a dict
workload_rightsizing_data_response_group_by_data_inner_from_dict = WorkloadRightsizingDataResponseGroupByDataInner.from_dict(workload_rightsizing_data_response_group_by_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


