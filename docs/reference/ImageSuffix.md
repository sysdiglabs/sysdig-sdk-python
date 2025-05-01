# ImageSuffix


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_type** | **str** | Matcher type to apply | [optional] 
**context_value** | **str** | Value to match | [optional] 

## Example

```python
from sysdig_client.models.image_suffix import ImageSuffix

# TODO update the JSON string below
json = "{}"
# create an instance of ImageSuffix from a JSON string
image_suffix_instance = ImageSuffix.from_json(json)
# print the JSON string representation of the object
print(ImageSuffix.to_json())

# convert the object into a dict
image_suffix_dict = image_suffix_instance.to_dict()
# create an instance of ImageSuffix from a dict
image_suffix_from_dict = ImageSuffix.from_dict(image_suffix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


