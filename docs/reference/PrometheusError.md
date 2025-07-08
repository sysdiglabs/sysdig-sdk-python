# PrometheusError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Indicates an error response. | [optional] 
**error_type** | **str** | Type of error encountered. | [optional] 
**error** | **str** | Error message describing the issue. | [optional] 

## Example

```python
from sysdig_client.models.prometheus_error import PrometheusError

# TODO update the JSON string below
json = "{}"
# create an instance of PrometheusError from a JSON string
prometheus_error_instance = PrometheusError.from_json(json)
# print the JSON string representation of the object
print(PrometheusError.to_json())

# convert the object into a dict
prometheus_error_dict = prometheus_error_instance.to_dict()
# create an instance of PrometheusError from a dict
prometheus_error_from_dict = PrometheusError.from_dict(prometheus_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


