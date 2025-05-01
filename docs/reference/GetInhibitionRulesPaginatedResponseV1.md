# GetInhibitionRulesPaginatedResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**OffsetPaginatedResponsePage**](OffsetPaginatedResponsePage.md) |  | [optional] 
**data** | [**List[InhibitionRuleResponseV1]**](InhibitionRuleResponseV1.md) |  | [optional] 

## Example

```python
from sysdig_client.models.get_inhibition_rules_paginated_response_v1 import GetInhibitionRulesPaginatedResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of GetInhibitionRulesPaginatedResponseV1 from a JSON string
get_inhibition_rules_paginated_response_v1_instance = GetInhibitionRulesPaginatedResponseV1.from_json(json)
# print the JSON string representation of the object
print(GetInhibitionRulesPaginatedResponseV1.to_json())

# convert the object into a dict
get_inhibition_rules_paginated_response_v1_dict = get_inhibition_rules_paginated_response_v1_instance.to_dict()
# create an instance of GetInhibitionRulesPaginatedResponseV1 from a dict
get_inhibition_rules_paginated_response_v1_from_dict = GetInhibitionRulesPaginatedResponseV1.from_dict(get_inhibition_rules_paginated_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


