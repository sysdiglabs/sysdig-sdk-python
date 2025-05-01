# DisableMetricV1

Get Disabled Metrics by Job name Response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_name** | **str** | The name of the metric to be disabled or re-enabled.  | [optional] 
**is_disabled** | **bool** | Set as &#x60;true&#x60; to disable a metric. \\ Set as &#x60;false&#x60; to re-enable a metric.  | [optional] 

## Example

```python
from sysdig_client.models.disable_metric_v1 import DisableMetricV1

# TODO update the JSON string below
json = "{}"
# create an instance of DisableMetricV1 from a JSON string
disable_metric_v1_instance = DisableMetricV1.from_json(json)
# print the JSON string representation of the object
print(DisableMetricV1.to_json())

# convert the object into a dict
disable_metric_v1_dict = disable_metric_v1_instance.to_dict()
# create an instance of DisableMetricV1 from a dict
disable_metric_v1_from_dict = DisableMetricV1.from_dict(disable_metric_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


