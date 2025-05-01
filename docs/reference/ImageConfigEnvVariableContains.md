# ImageConfigEnvVariableContains

Predicate expressing \"the container has the specified environment variable and value\". 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**extra** | [**ImageConfigEnvVariableContainsExtra**](ImageConfigEnvVariableContainsExtra.md) |  | 

## Example

```python
from sysdig_client.models.image_config_env_variable_contains import ImageConfigEnvVariableContains

# TODO update the JSON string below
json = "{}"
# create an instance of ImageConfigEnvVariableContains from a JSON string
image_config_env_variable_contains_instance = ImageConfigEnvVariableContains.from_json(json)
# print the JSON string representation of the object
print(ImageConfigEnvVariableContains.to_json())

# convert the object into a dict
image_config_env_variable_contains_dict = image_config_env_variable_contains_instance.to_dict()
# create an instance of ImageConfigEnvVariableContains from a dict
image_config_env_variable_contains_from_dict = ImageConfigEnvVariableContains.from_dict(image_config_env_variable_contains_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


