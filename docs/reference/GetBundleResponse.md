# GetBundleResponse

Bundle definition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The Bundle ID | 
**name** | **str** | The human readable Bundle name | 
**identifier** | **str** | The Policy identifier generated from the name | 
**description** | **str** | The Bundle description | [optional] 
**bundle_type** | **str** | Specifies whether the Bundle was defined by the Customer or by Sysdig | 
**rules** | [**List[BundleRule]**](BundleRule.md) | The Rules defining this Bundle | 

## Example

```python
from sysdig_client.models.get_bundle_response import GetBundleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBundleResponse from a JSON string
get_bundle_response_instance = GetBundleResponse.from_json(json)
# print the JSON string representation of the object
print(GetBundleResponse.to_json())

# convert the object into a dict
get_bundle_response_dict = get_bundle_response_instance.to_dict()
# create an instance of GetBundleResponse from a dict
get_bundle_response_from_dict = GetBundleResponse.from_dict(get_bundle_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


