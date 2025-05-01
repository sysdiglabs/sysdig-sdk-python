# MetricErrorV1

Get Disabled Metrics by Job name Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_name** | **str** | The metric name which could not be disabled or enabled.  | [optional] 
**job_name** | **str** | Specifies the name of the job that caused the error.  | [optional] 
**message** | **str** | Describes the job and metric error.  | [optional] 

## Example

```python
from sysdig_client.models.metric_error_v1 import MetricErrorV1

# TODO update the JSON string below
json = "{}"
# create an instance of MetricErrorV1 from a JSON string
metric_error_v1_instance = MetricErrorV1.from_json(json)
# print the JSON string representation of the object
print(MetricErrorV1.to_json())

# convert the object into a dict
metric_error_v1_dict = metric_error_v1_instance.to_dict()
# create an instance of MetricErrorV1 from a dict
metric_error_v1_from_dict = MetricErrorV1.from_dict(metric_error_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


