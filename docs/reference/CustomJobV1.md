# CustomJobV1

Custom Prometheus job name and enablement status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Job name | [optional]
**enabled** | **bool** | Enablement status | [optional]
**enablement_by_cluster** | **Dict[str, bool]** | Enablement overrides by cluster | [optional]

## Example

```python
from sysdig_client.models.custom_job_v1 import CustomJobV1

# TODO update the JSON string below
json = "{}"
# create an instance of CustomJobV1 from a JSON string
custom_job_v1_instance = CustomJobV1.from_json(json)
# print the JSON string representation of the object
print(CustomJobV1.to_json())

# convert the object into a dict
custom_job_v1_dict = custom_job_v1_instance.to_dict()
# create an instance of CustomJobV1 from a dict
custom_job_v1_from_dict = CustomJobV1.from_dict(custom_job_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


