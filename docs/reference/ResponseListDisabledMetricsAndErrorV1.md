# ResponseListDisabledMetricsAndErrorV1

Get Disabled Metrics by Job name Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ListJobAndDisabledMetricsV1]**](ListJobAndDisabledMetricsV1.md) |  | 
**errors** | [**List[MetricErrorV1]**](MetricErrorV1.md) |  | 

## Example

```python
from sysdig_client.models.response_list_disabled_metrics_and_error_v1 import ResponseListDisabledMetricsAndErrorV1

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseListDisabledMetricsAndErrorV1 from a JSON string
response_list_disabled_metrics_and_error_v1_instance = ResponseListDisabledMetricsAndErrorV1.from_json(json)
# print the JSON string representation of the object
print(ResponseListDisabledMetricsAndErrorV1.to_json())

# convert the object into a dict
response_list_disabled_metrics_and_error_v1_dict = response_list_disabled_metrics_and_error_v1_instance.to_dict()
# create an instance of ResponseListDisabledMetricsAndErrorV1 from a dict
response_list_disabled_metrics_and_error_v1_from_dict = ResponseListDisabledMetricsAndErrorV1.from_dict(response_list_disabled_metrics_and_error_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


