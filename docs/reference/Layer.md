# Layer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | layer&#39;s index | [optional] 
**digest** | **str** | sha256 digest of the layer | 
**size** | **int** | size of the layer in bytes | [optional] 
**command** | **str** | layer command | [optional] 
**base_images_ref** | **List[str]** | base images refs | [optional] 

## Example

```python
from sysdig_client.models.layer import Layer

# TODO update the JSON string below
json = "{}"
# create an instance of Layer from a JSON string
layer_instance = Layer.from_json(json)
# print the JSON string representation of the object
print(Layer.to_json())

# convert the object into a dict
layer_dict = layer_instance.to_dict()
# create an instance of Layer from a dict
layer_from_dict = Layer.from_dict(layer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


