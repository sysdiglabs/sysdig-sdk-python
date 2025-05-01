# ImageName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_type** | **str** | Matcher type to apply | [optional] 
**context_value** | **str** | Value to match | [optional] 

## Example

```python
from sysdig_client.models.image_name import ImageName

# TODO update the JSON string below
json = "{}"
# create an instance of ImageName from a JSON string
image_name_instance = ImageName.from_json(json)
# print the JSON string representation of the object
print(ImageName.to_json())

# convert the object into a dict
image_name_dict = image_name_instance.to_dict()
# create an instance of ImageName from a dict
image_name_from_dict = ImageName.from_dict(image_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


