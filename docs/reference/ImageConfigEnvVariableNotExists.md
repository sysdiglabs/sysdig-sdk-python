# ImageConfigEnvVariableNotExists

Predicate expressing \"the container does not have the specified environment variable\". 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**extra** | [**ImageConfigEnvVariableExistsExtra**](ImageConfigEnvVariableExistsExtra.md) |  | 

## Example

```python
from sysdig_client.models.image_config_env_variable_not_exists import ImageConfigEnvVariableNotExists

# TODO update the JSON string below
json = "{}"
# create an instance of ImageConfigEnvVariableNotExists from a JSON string
image_config_env_variable_not_exists_instance = ImageConfigEnvVariableNotExists.from_json(json)
# print the JSON string representation of the object
print(ImageConfigEnvVariableNotExists.to_json())

# convert the object into a dict
image_config_env_variable_not_exists_dict = image_config_env_variable_not_exists_instance.to_dict()
# create an instance of ImageConfigEnvVariableNotExists from a dict
image_config_env_variable_not_exists_from_dict = ImageConfigEnvVariableNotExists.from_dict(image_config_env_variable_not_exists_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


