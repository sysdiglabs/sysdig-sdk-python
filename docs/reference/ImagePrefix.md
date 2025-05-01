# ImagePrefix


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_type** | **str** | Matcher type to apply | [optional] 
**context_value** | **str** | Value to match | [optional] 

## Example

```python
from sysdig_client.models.image_prefix import ImagePrefix

# TODO update the JSON string below
json = "{}"
# create an instance of ImagePrefix from a JSON string
image_prefix_instance = ImagePrefix.from_json(json)
# print the JSON string representation of the object
print(ImagePrefix.to_json())

# convert the object into a dict
image_prefix_dict = image_prefix_instance.to_dict()
# create an instance of ImagePrefix from a dict
image_prefix_from_dict = ImagePrefix.from_dict(image_prefix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


