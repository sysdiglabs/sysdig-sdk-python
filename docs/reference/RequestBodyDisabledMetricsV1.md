# RequestBodyDisabledMetricsV1

Change Disabled Metrics per JobName

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DisableJobsAndMetricsV1]**](DisableJobsAndMetricsV1.md) |  | 

## Example

```python
from sysdig_client.models.request_body_disabled_metrics_v1 import RequestBodyDisabledMetricsV1

# TODO update the JSON string below
json = "{}"
# create an instance of RequestBodyDisabledMetricsV1 from a JSON string
request_body_disabled_metrics_v1_instance = RequestBodyDisabledMetricsV1.from_json(json)
# print the JSON string representation of the object
print(RequestBodyDisabledMetricsV1.to_json())

# convert the object into a dict
request_body_disabled_metrics_v1_dict = request_body_disabled_metrics_v1_instance.to_dict()
# create an instance of RequestBodyDisabledMetricsV1 from a dict
request_body_disabled_metrics_v1_from_dict = RequestBodyDisabledMetricsV1.from_dict(request_body_disabled_metrics_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


