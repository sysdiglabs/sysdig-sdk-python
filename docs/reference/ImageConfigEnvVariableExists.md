# ImageConfigEnvVariableExists

Predicate expressing \"the container has the specified environment variable\". 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**extra** | [**ImageConfigEnvVariableExistsExtra**](ImageConfigEnvVariableExistsExtra.md) |  | 

## Example

```python
from sysdig_client.models.image_config_env_variable_exists import ImageConfigEnvVariableExists

# TODO update the JSON string below
json = "{}"
# create an instance of ImageConfigEnvVariableExists from a JSON string
image_config_env_variable_exists_instance = ImageConfigEnvVariableExists.from_json(json)
# print the JSON string representation of the object
print(ImageConfigEnvVariableExists.to_json())

# convert the object into a dict
image_config_env_variable_exists_dict = image_config_env_variable_exists_instance.to_dict()
# create an instance of ImageConfigEnvVariableExists from a dict
image_config_env_variable_exists_from_dict = ImageConfigEnvVariableExists.from_dict(image_config_env_variable_exists_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


