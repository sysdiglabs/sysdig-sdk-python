# CaptureStorageConfigurationResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | Specifies if capture storage is enabled. | [optional] 
**is_encryption_with_provided_key_enabled** | **bool** | Specifies if server-side encryption with provided encryption key (SSE-C) is enabled. | [optional] 
**buckets** | [**List[BucketConfigurationV1]**](BucketConfigurationV1.md) | The list of buckets where the captures are stored. Currently only one bucket is supported.  | [optional] 

## Example

```python
from sysdig_client.models.capture_storage_configuration_response_v1 import CaptureStorageConfigurationResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of CaptureStorageConfigurationResponseV1 from a JSON string
capture_storage_configuration_response_v1_instance = CaptureStorageConfigurationResponseV1.from_json(json)
# print the JSON string representation of the object
print(CaptureStorageConfigurationResponseV1.to_json())

# convert the object into a dict
capture_storage_configuration_response_v1_dict = capture_storage_configuration_response_v1_instance.to_dict()
# create an instance of CaptureStorageConfigurationResponseV1 from a dict
capture_storage_configuration_response_v1_from_dict = CaptureStorageConfigurationResponseV1.from_dict(capture_storage_configuration_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


