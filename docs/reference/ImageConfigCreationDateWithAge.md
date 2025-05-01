# ImageConfigCreationDateWithAge

Predicate expressing \"the image has been created before the specified amount of days\". 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**extra** | [**ImageConfigCreationDateWithAgeExtra**](ImageConfigCreationDateWithAgeExtra.md) |  | 

## Example

```python
from sysdig_client.models.image_config_creation_date_with_age import ImageConfigCreationDateWithAge

# TODO update the JSON string below
json = "{}"
# create an instance of ImageConfigCreationDateWithAge from a JSON string
image_config_creation_date_with_age_instance = ImageConfigCreationDateWithAge.from_json(json)
# print the JSON string representation of the object
print(ImageConfigCreationDateWithAge.to_json())

# convert the object into a dict
image_config_creation_date_with_age_dict = image_config_creation_date_with_age_instance.to_dict()
# create an instance of ImageConfigCreationDateWithAge from a dict
image_config_creation_date_with_age_from_dict = ImageConfigCreationDateWithAge.from_dict(image_config_creation_date_with_age_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


