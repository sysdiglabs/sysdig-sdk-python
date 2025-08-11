# CustomJobsEnablementV1

The enablement status of a custom Prometheus job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enablement status |
**enablement_by_cluster** | **Dict[str, bool]** | Enablement overrides by cluster | [optional]

## Example

```python
from sysdig_client.models.custom_jobs_enablement_v1 import CustomJobsEnablementV1

# TODO update the JSON string below
json = "{}"
# create an instance of CustomJobsEnablementV1 from a JSON string
custom_jobs_enablement_v1_instance = CustomJobsEnablementV1.from_json(json)
# print the JSON string representation of the object
print(CustomJobsEnablementV1.to_json())

# convert the object into a dict
custom_jobs_enablement_v1_dict = custom_jobs_enablement_v1_instance.to_dict()
# create an instance of CustomJobsEnablementV1 from a dict
custom_jobs_enablement_v1_from_dict = CustomJobsEnablementV1.from_dict(custom_jobs_enablement_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


