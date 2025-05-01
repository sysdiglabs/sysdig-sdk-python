# BucketConfigurationV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the bucket. | 
**folder** | **str** | The folder in the bucket where the captures are stored. Name of the folder without any prefix slashes (\&quot;test-folder\&quot; and not \&quot;/test-folder\&quot;). | [optional] 
**description** | **str** | The description of the bucket. | [optional] 
**provider_key_id** | **str** | Id of the configured cloud provider account. Could be fetched with /api/providers endpoint. | [optional] 
**endpoint** | **str** | The endpoint of the bucket. ***Required for S3 compatible storage.*** | [optional] 
**region** | **str** | The region of the bucket. | [optional] 
**path_style_access** | **bool** | Specifies if the bucket uses path-style access. | [optional] [default to False]

## Example

```python
from sysdig_client.models.bucket_configuration_v1 import BucketConfigurationV1

# TODO update the JSON string below
json = "{}"
# create an instance of BucketConfigurationV1 from a JSON string
bucket_configuration_v1_instance = BucketConfigurationV1.from_json(json)
# print the JSON string representation of the object
print(BucketConfigurationV1.to_json())

# convert the object into a dict
bucket_configuration_v1_dict = bucket_configuration_v1_instance.to_dict()
# create an instance of BucketConfigurationV1 from a dict
bucket_configuration_v1_from_dict = BucketConfigurationV1.from_dict(bucket_configuration_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


