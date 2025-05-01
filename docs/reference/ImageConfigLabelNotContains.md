# ImageConfigLabelNotContains

Predicate expressing \"the image has the specified label and value\". 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**extra** | [**ImageConfigLabelNotContainsExtra**](ImageConfigLabelNotContainsExtra.md) |  | 

## Example

```python
from sysdig_client.models.image_config_label_not_contains import ImageConfigLabelNotContains

# TODO update the JSON string below
json = "{}"
# create an instance of ImageConfigLabelNotContains from a JSON string
image_config_label_not_contains_instance = ImageConfigLabelNotContains.from_json(json)
# print the JSON string representation of the object
print(ImageConfigLabelNotContains.to_json())

# convert the object into a dict
image_config_label_not_contains_dict = image_config_label_not_contains_instance.to_dict()
# create an instance of ImageConfigLabelNotContains from a dict
image_config_label_not_contains_from_dict = ImageConfigLabelNotContains.from_dict(image_config_label_not_contains_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


