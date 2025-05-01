# ImageConfigDefaultUserList

Configuration to set the default user for the specified image.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**extra** | [**ImageConfigDefaultUserListExtra**](ImageConfigDefaultUserListExtra.md) |  | 

## Example

```python
from sysdig_client.models.image_config_default_user_list import ImageConfigDefaultUserList

# TODO update the JSON string below
json = "{}"
# create an instance of ImageConfigDefaultUserList from a JSON string
image_config_default_user_list_instance = ImageConfigDefaultUserList.from_json(json)
# print the JSON string representation of the object
print(ImageConfigDefaultUserList.to_json())

# convert the object into a dict
image_config_default_user_list_dict = image_config_default_user_list_instance.to_dict()
# create an instance of ImageConfigDefaultUserList from a dict
image_config_default_user_list_from_dict = ImageConfigDefaultUserList.from_dict(image_config_default_user_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


