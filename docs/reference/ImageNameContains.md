# ImageNameContains


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_type** | **str** | Matcher type to apply | [optional] 
**context_value** | **str** | Value to match | [optional] 

## Example

```python
from sysdig_client.models.image_name_contains import ImageNameContains

# TODO update the JSON string below
json = "{}"
# create an instance of ImageNameContains from a JSON string
image_name_contains_instance = ImageNameContains.from_json(json)
# print the JSON string representation of the object
print(ImageNameContains.to_json())

# convert the object into a dict
image_name_contains_dict = image_name_contains_instance.to_dict()
# create an instance of ImageNameContains from a dict
image_name_contains_from_dict = ImageNameContains.from_dict(image_name_contains_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


