# ListZonesResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**OffsetPaginatedResponsePage**](OffsetPaginatedResponsePage.md) |  | [optional] 
**data** | [**List[ListZonesResponseV1AllOfData]**](ListZonesResponseV1AllOfData.md) |  | [optional] 

## Example

```python
from sysdig_client.models.list_zones_response_v1 import ListZonesResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of ListZonesResponseV1 from a JSON string
list_zones_response_v1_instance = ListZonesResponseV1.from_json(json)
# print the JSON string representation of the object
print(ListZonesResponseV1.to_json())

# convert the object into a dict
list_zones_response_v1_dict = list_zones_response_v1_instance.to_dict()
# create an instance of ListZonesResponseV1 from a dict
list_zones_response_v1_from_dict = ListZonesResponseV1.from_dict(list_zones_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


