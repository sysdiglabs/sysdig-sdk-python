# OffsetPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**OffsetPaginatedResponsePage**](OffsetPaginatedResponsePage.md) |  | [optional] 
**data** | **List[object]** | Paginated data. | [optional] 

## Example

```python
from sysdig_client.models.offset_paginated_response import OffsetPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OffsetPaginatedResponse from a JSON string
offset_paginated_response_instance = OffsetPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(OffsetPaginatedResponse.to_json())

# convert the object into a dict
offset_paginated_response_dict = offset_paginated_response_instance.to_dict()
# create an instance of OffsetPaginatedResponse from a dict
offset_paginated_response_from_dict = OffsetPaginatedResponse.from_dict(offset_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


