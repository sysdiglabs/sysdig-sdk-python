# ImageConfigLabelNotExists

Predicate expressing \"the image does not have the specified label\". 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**extra** | [**ImageConfigLabelNotExistsExtra**](ImageConfigLabelNotExistsExtra.md) |  | 

## Example

```python
from sysdig_client.models.image_config_label_not_exists import ImageConfigLabelNotExists

# TODO update the JSON string below
json = "{}"
# create an instance of ImageConfigLabelNotExists from a JSON string
image_config_label_not_exists_instance = ImageConfigLabelNotExists.from_json(json)
# print the JSON string representation of the object
print(ImageConfigLabelNotExists.to_json())

# convert the object into a dict
image_config_label_not_exists_dict = image_config_label_not_exists_instance.to_dict()
# create an instance of ImageConfigLabelNotExists from a dict
image_config_label_not_exists_from_dict = ImageConfigLabelNotExists.from_dict(image_config_label_not_exists_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


