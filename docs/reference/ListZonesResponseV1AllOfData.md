# ListZonesResponseV1AllOfData

A paged list of Zones

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |   | [optional] 
**name** | **str** | The name of the Zone | [optional] 
**description** | **str** | The description of the Zone | [optional] 
**author** | **str** | Email of the user who created this Zone | [optional] 
**last_modified_by** | **str** | Email of the user who last modified the Zone | [optional] 
**last_updated** | **int** | Timestamp indicating the moment the Zone has been last updated.\\ It is expressed in milliseconds elapsed since January 1, 1970 UTC.  | [optional] 
**is_system** | **bool** | Boolean value indicating if the Zone is a *System* one | [optional] 
**scopes** | [**List[ZoneScope]**](ZoneScope.md) | Attached Zone Scopes | [optional] 

## Example

```python
from sysdig_client.models.list_zones_response_v1_all_of_data import ListZonesResponseV1AllOfData

# TODO update the JSON string below
json = "{}"
# create an instance of ListZonesResponseV1AllOfData from a JSON string
list_zones_response_v1_all_of_data_instance = ListZonesResponseV1AllOfData.from_json(json)
# print the JSON string representation of the object
print(ListZonesResponseV1AllOfData.to_json())

# convert the object into a dict
list_zones_response_v1_all_of_data_dict = list_zones_response_v1_all_of_data_instance.to_dict()
# create an instance of ListZonesResponseV1AllOfData from a dict
list_zones_response_v1_all_of_data_from_dict = ListZonesResponseV1AllOfData.from_dict(list_zones_response_v1_all_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


