# MetricV1

Get Disabled Metrics by Job name Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_name** | **str** | Specifies the name of the disabled metric.  | [optional] 
**modified_date** | **datetime** | The timestamp during which the metric was disabled  | [optional] 
**user_id** | **int** | The UserId responsible for disabling the metric  | [optional] 
**user_name** | **str** | User name of the person who disabled the metric  | [optional] 

## Example

```python
from sysdig_client.models.metric_v1 import MetricV1

# TODO update the JSON string below
json = "{}"
# create an instance of MetricV1 from a JSON string
metric_v1_instance = MetricV1.from_json(json)
# print the JSON string representation of the object
print(MetricV1.to_json())

# convert the object into a dict
metric_v1_dict = metric_v1_instance.to_dict()
# create an instance of MetricV1 from a dict
metric_v1_from_dict = MetricV1.from_dict(metric_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


