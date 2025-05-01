# IpFiltersPaginatedResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**OffsetPaginatedResponsePage**](OffsetPaginatedResponsePage.md) |  | [optional] 
**data** | [**List[IpFilterResponseV1]**](IpFilterResponseV1.md) |  | [optional] 

## Example

```python
from sysdig_client.models.ip_filters_paginated_response_v1 import IpFiltersPaginatedResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of IpFiltersPaginatedResponseV1 from a JSON string
ip_filters_paginated_response_v1_instance = IpFiltersPaginatedResponseV1.from_json(json)
# print the JSON string representation of the object
print(IpFiltersPaginatedResponseV1.to_json())

# convert the object into a dict
ip_filters_paginated_response_v1_dict = ip_filters_paginated_response_v1_instance.to_dict()
# create an instance of IpFiltersPaginatedResponseV1 from a dict
ip_filters_paginated_response_v1_from_dict = IpFiltersPaginatedResponseV1.from_dict(ip_filters_paginated_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


