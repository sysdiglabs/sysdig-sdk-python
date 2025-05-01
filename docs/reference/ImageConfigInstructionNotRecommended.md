# ImageConfigInstructionNotRecommended

Predicate expressing \"the image history contains not recommended instruction (ADD, ...)\". 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from sysdig_client.models.image_config_instruction_not_recommended import ImageConfigInstructionNotRecommended

# TODO update the JSON string below
json = "{}"
# create an instance of ImageConfigInstructionNotRecommended from a JSON string
image_config_instruction_not_recommended_instance = ImageConfigInstructionNotRecommended.from_json(json)
# print the JSON string representation of the object
print(ImageConfigInstructionNotRecommended.to_json())

# convert the object into a dict
image_config_instruction_not_recommended_dict = image_config_instruction_not_recommended_instance.to_dict()
# create an instance of ImageConfigInstructionNotRecommended from a dict
image_config_instruction_not_recommended_from_dict = ImageConfigInstructionNotRecommended.from_dict(image_config_instruction_not_recommended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


