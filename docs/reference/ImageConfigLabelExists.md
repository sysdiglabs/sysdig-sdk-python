# ImageConfigLabelExists

Predicate expressing \"the image has the specified label\". 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**extra** | [**ImageConfigLabelExistsExtra**](ImageConfigLabelExistsExtra.md) |  | 

## Example

```python
from sysdig_client.models.image_config_label_exists import ImageConfigLabelExists

# TODO update the JSON string below
json = "{}"
# create an instance of ImageConfigLabelExists from a JSON string
image_config_label_exists_instance = ImageConfigLabelExists.from_json(json)
# print the JSON string representation of the object
print(ImageConfigLabelExists.to_json())

# convert the object into a dict
image_config_label_exists_dict = image_config_label_exists_instance.to_dict()
# create an instance of ImageConfigLabelExists from a dict
image_config_label_exists_from_dict = ImageConfigLabelExists.from_dict(image_config_label_exists_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


