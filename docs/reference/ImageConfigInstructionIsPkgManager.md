# ImageConfigInstructionIsPkgManager

Predicate expressing \"the image history contains a package manager command (eg. apk, npm, rpm, etc)\". 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from sysdig_client.models.image_config_instruction_is_pkg_manager import ImageConfigInstructionIsPkgManager

# TODO update the JSON string below
json = "{}"
# create an instance of ImageConfigInstructionIsPkgManager from a JSON string
image_config_instruction_is_pkg_manager_instance = ImageConfigInstructionIsPkgManager.from_json(json)
# print the JSON string representation of the object
print(ImageConfigInstructionIsPkgManager.to_json())

# convert the object into a dict
image_config_instruction_is_pkg_manager_dict = image_config_instruction_is_pkg_manager_instance.to_dict()
# create an instance of ImageConfigInstructionIsPkgManager from a dict
image_config_instruction_is_pkg_manager_from_dict = ImageConfigInstructionIsPkgManager.from_dict(image_config_instruction_is_pkg_manager_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


