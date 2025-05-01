# DisableJobsAndMetricsV1

Get Disabled Metrics by Job name Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_name** | **str** | The Prometheus Job for which the collection of one or more metrics is disabled.  | [optional] 
**metrics** | [**List[DisableMetricV1]**](DisableMetricV1.md) | List of metrics to be disabled.  | [optional] 

## Example

```python
from sysdig_client.models.disable_jobs_and_metrics_v1 import DisableJobsAndMetricsV1

# TODO update the JSON string below
json = "{}"
# create an instance of DisableJobsAndMetricsV1 from a JSON string
disable_jobs_and_metrics_v1_instance = DisableJobsAndMetricsV1.from_json(json)
# print the JSON string representation of the object
print(DisableJobsAndMetricsV1.to_json())

# convert the object into a dict
disable_jobs_and_metrics_v1_dict = disable_jobs_and_metrics_v1_instance.to_dict()
# create an instance of DisableJobsAndMetricsV1 from a dict
disable_jobs_and_metrics_v1_from_dict = DisableJobsAndMetricsV1.from_dict(disable_jobs_and_metrics_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


