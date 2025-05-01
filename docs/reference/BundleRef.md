# BundleRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The Bundle ID. | 
**name** | **str** | The human readable Bundle name. | [optional] 

## Example

```python
from sysdig_client.models.bundle_ref import BundleRef

# TODO update the JSON string below
json = "{}"
# create an instance of BundleRef from a JSON string
bundle_ref_instance = BundleRef.from_json(json)
# print the JSON string representation of the object
print(BundleRef.to_json())

# convert the object into a dict
bundle_ref_dict = bundle_ref_instance.to_dict()
# create an instance of BundleRef from a dict
bundle_ref_from_dict = BundleRef.from_dict(bundle_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


