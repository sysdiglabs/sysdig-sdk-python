# ImageConfigDefaultUserIsNot

Predicate expressing \"the container user does not default to the specified user\". 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**extra** | [**ImageConfigDefaultUserIsNotExtra**](ImageConfigDefaultUserIsNotExtra.md) |  | 

## Example

```python
from sysdig_client.models.image_config_default_user_is_not import ImageConfigDefaultUserIsNot

# TODO update the JSON string below
json = "{}"
# create an instance of ImageConfigDefaultUserIsNot from a JSON string
image_config_default_user_is_not_instance = ImageConfigDefaultUserIsNot.from_json(json)
# print the JSON string representation of the object
print(ImageConfigDefaultUserIsNot.to_json())

# convert the object into a dict
image_config_default_user_is_not_dict = image_config_default_user_is_not_instance.to_dict()
# create an instance of ImageConfigDefaultUserIsNot from a dict
image_config_default_user_is_not_from_dict = ImageConfigDefaultUserIsNot.from_dict(image_config_default_user_is_not_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


