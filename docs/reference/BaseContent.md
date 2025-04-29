# BaseContent

Base content for all events

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**EventContentType**](EventContentType.md) |  | 

## Example

```python
from sysdig_client.models.base_content import BaseContent

# TODO update the JSON string below
json = "{}"
# create an instance of BaseContent from a JSON string
base_content_instance = BaseContent.from_json(json)
# print the JSON string representation of the object
print(BaseContent.to_json())

# convert the object into a dict
base_content_dict = base_content_instance.to_dict()
# create an instance of BaseContent from a dict
base_content_from_dict = BaseContent.from_dict(base_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


