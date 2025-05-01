# ScanResultResponseMetadata

metadata of the scan result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pull_string** | **str** | image pull string | 
**image_id** | **str** | image id | 
**digest** | **str** | image digest | [optional] 
**base_os** | **str** | image base os | 
**size** | **int** | image size in bytes | 
**os** | **str** | host os | 
**architecture** | **str** | host architecture | [optional] 
**labels** | **object** | image labels | [optional] 
**author** | **str** | image author | [optional] 
**created_at** | **str** | datetime of creation | 
**host_id** | **str** | host id | 
**host_name** | **str** | host name | 

## Example

```python
from sysdig_client.models.scan_result_response_metadata import ScanResultResponseMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ScanResultResponseMetadata from a JSON string
scan_result_response_metadata_instance = ScanResultResponseMetadata.from_json(json)
# print the JSON string representation of the object
print(ScanResultResponseMetadata.to_json())

# convert the object into a dict
scan_result_response_metadata_dict = scan_result_response_metadata_instance.to_dict()
# create an instance of ScanResultResponseMetadata from a dict
scan_result_response_metadata_from_dict = ScanResultResponseMetadata.from_dict(scan_result_response_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


