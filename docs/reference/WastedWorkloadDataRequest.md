# WastedWorkloadDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_range** | [**DateRange**](DateRange.md) |  |
**scope** | [**List[PromqlMatcher]**](PromqlMatcher.md) | A list of PromQL-style filters | [optional]
**group_by** | **List[str]** | Specifies Prometheus labels to group the report data by. By default, the following labels will always be included:   - kube_cluster_name   - kube_namespace_name   - kube_workload_name A maximum of 7 additional custom labels can be specified.  | [optional]

## Example

```python
from sysdig_client.models.wasted_workload_data_request import WastedWorkloadDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WastedWorkloadDataRequest from a JSON string
wasted_workload_data_request_instance = WastedWorkloadDataRequest.from_json(json)
# print the JSON string representation of the object
print(WastedWorkloadDataRequest.to_json())

# convert the object into a dict
wasted_workload_data_request_dict = wasted_workload_data_request_instance.to_dict()
# create an instance of WastedWorkloadDataRequest from a dict
wasted_workload_data_request_from_dict = WastedWorkloadDataRequest.from_dict(wasted_workload_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


