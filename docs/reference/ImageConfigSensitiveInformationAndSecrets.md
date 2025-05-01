# ImageConfigSensitiveInformationAndSecrets

Predicate expressing \"the image contains sensitive information and secrets\". 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from sysdig_client.models.image_config_sensitive_information_and_secrets import ImageConfigSensitiveInformationAndSecrets

# TODO update the JSON string below
json = "{}"
# create an instance of ImageConfigSensitiveInformationAndSecrets from a JSON string
image_config_sensitive_information_and_secrets_instance = ImageConfigSensitiveInformationAndSecrets.from_json(json)
# print the JSON string representation of the object
print(ImageConfigSensitiveInformationAndSecrets.to_json())

# convert the object into a dict
image_config_sensitive_information_and_secrets_dict = image_config_sensitive_information_and_secrets_instance.to_dict()
# create an instance of ImageConfigSensitiveInformationAndSecrets from a dict
image_config_sensitive_information_and_secrets_from_dict = ImageConfigSensitiveInformationAndSecrets.from_dict(image_config_sensitive_information_and_secrets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


