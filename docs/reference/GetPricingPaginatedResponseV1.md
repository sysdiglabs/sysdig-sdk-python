# GetPricingPaginatedResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**OffsetPaginatedResponsePage**](OffsetPaginatedResponsePage.md) |  | [optional] 
**data** | [**List[PricingResponseV1]**](PricingResponseV1.md) |  | [optional] 

## Example

```python
from sysdig_client.models.get_pricing_paginated_response_v1 import GetPricingPaginatedResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of GetPricingPaginatedResponseV1 from a JSON string
get_pricing_paginated_response_v1_instance = GetPricingPaginatedResponseV1.from_json(json)
# print the JSON string representation of the object
print(GetPricingPaginatedResponseV1.to_json())

# convert the object into a dict
get_pricing_paginated_response_v1_dict = get_pricing_paginated_response_v1_instance.to_dict()
# create an instance of GetPricingPaginatedResponseV1 from a dict
get_pricing_paginated_response_v1_from_dict = GetPricingPaginatedResponseV1.from_dict(get_pricing_paginated_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


