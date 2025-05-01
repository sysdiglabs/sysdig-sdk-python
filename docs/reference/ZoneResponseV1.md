# ZoneResponseV1


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
from sysdig_client.models.zone_response_v1 import ZoneResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneResponseV1 from a JSON string
zone_response_v1_instance = ZoneResponseV1.from_json(json)
# print the JSON string representation of the object
print(ZoneResponseV1.to_json())

# convert the object into a dict
zone_response_v1_dict = zone_response_v1_instance.to_dict()
# create an instance of ZoneResponseV1 from a dict
zone_response_v1_from_dict = ZoneResponseV1.from_dict(zone_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


