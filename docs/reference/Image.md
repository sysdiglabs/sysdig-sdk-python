# Image

An Image resource that returns as part of of the image summary.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | **str** | Resource unique identifier | 
**name** | **str** | Resource name | 
**type** | **str** | The resource type | 
**pull_string** | **str** | The pull string for the image. | 
**vulnerability_summary** | [**VulnerabilitySummary**](VulnerabilitySummary.md) |  | 
**in_use_vulnerability_summary** | [**VulnerabilitySummary**](VulnerabilitySummary.md) |  | 
**vm_api_endpoint** | **str** | A link that provides vulnerability management information about an image (Images only). | 

## Example

```python
from sysdig_client.models.image import Image

# TODO update the JSON string below
json = "{}"
# create an instance of Image from a JSON string
image_instance = Image.from_json(json)
# print the JSON string representation of the object
print(Image.to_json())

# convert the object into a dict
image_dict = image_instance.to_dict()
# create an instance of Image from a dict
image_from_dict = Image.from_dict(image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


