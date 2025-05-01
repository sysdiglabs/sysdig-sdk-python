# SaveCaptureStorageConfigurationRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | Specifies if capture storage is enabled. | 
**is_encryption_with_provided_key_enabled** | **bool** | Specifies if server-side encryption with provided encryption key (SSE-C) is enabled. | [optional] [default to False]
**encryption_key** | **str** | AES-256 encryption key to be used for server-side encryption (base64 encoded). | [optional] 
**buckets** | [**List[BucketConfigurationV1]**](BucketConfigurationV1.md) | The list of buckets where the captures are stored. Currently only one bucket is supported.  | [optional] 

## Example

```python
from sysdig_client.models.save_capture_storage_configuration_request_v1 import SaveCaptureStorageConfigurationRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of SaveCaptureStorageConfigurationRequestV1 from a JSON string
save_capture_storage_configuration_request_v1_instance = SaveCaptureStorageConfigurationRequestV1.from_json(json)
# print the JSON string representation of the object
print(SaveCaptureStorageConfigurationRequestV1.to_json())

# convert the object into a dict
save_capture_storage_configuration_request_v1_dict = save_capture_storage_configuration_request_v1_instance.to_dict()
# create an instance of SaveCaptureStorageConfigurationRequestV1 from a dict
save_capture_storage_configuration_request_v1_from_dict = SaveCaptureStorageConfigurationRequestV1.from_dict(save_capture_storage_configuration_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


