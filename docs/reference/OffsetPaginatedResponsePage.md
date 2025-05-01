# OffsetPaginatedResponsePage

Page information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous** | **str** |  | [optional] 
**next** | **str** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from sysdig_client.models.offset_paginated_response_page import OffsetPaginatedResponsePage

# TODO update the JSON string below
json = "{}"
# create an instance of OffsetPaginatedResponsePage from a JSON string
offset_paginated_response_page_instance = OffsetPaginatedResponsePage.from_json(json)
# print the JSON string representation of the object
print(OffsetPaginatedResponsePage.to_json())

# convert the object into a dict
offset_paginated_response_page_dict = offset_paginated_response_page_instance.to_dict()
# create an instance of OffsetPaginatedResponsePage from a dict
offset_paginated_response_page_from_dict = OffsetPaginatedResponsePage.from_dict(offset_paginated_response_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


