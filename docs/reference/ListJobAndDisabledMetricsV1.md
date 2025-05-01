# ListJobAndDisabledMetricsV1

Get Disabled Metrics by Job name Response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_name** | **str** | The name of the Job reporting the metric.  | [optional] 
**metrics** | [**List[MetricV1]**](MetricV1.md) | List of metrics that are disabled for the Job.  | [optional] 

## Example

```python
from sysdig_client.models.list_job_and_disabled_metrics_v1 import ListJobAndDisabledMetricsV1

# TODO update the JSON string below
json = "{}"
# create an instance of ListJobAndDisabledMetricsV1 from a JSON string
list_job_and_disabled_metrics_v1_instance = ListJobAndDisabledMetricsV1.from_json(json)
# print the JSON string representation of the object
print(ListJobAndDisabledMetricsV1.to_json())

# convert the object into a dict
list_job_and_disabled_metrics_v1_dict = list_job_and_disabled_metrics_v1_instance.to_dict()
# create an instance of ListJobAndDisabledMetricsV1 from a dict
list_job_and_disabled_metrics_v1_from_dict = ListJobAndDisabledMetricsV1.from_dict(list_job_and_disabled_metrics_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


