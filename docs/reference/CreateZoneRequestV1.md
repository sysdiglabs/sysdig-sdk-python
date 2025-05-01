# CreateZoneRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Zone. It must be unique | 
**description** | **str** | The Zone description. It can be useful for adding extra information | [optional] 
**scopes** | [**List[CreateZoneScopeRequestV1]**](CreateZoneScopeRequestV1.md) | Zone attached scopes | 

## Example

```python
from sysdig_client.models.create_zone_request_v1 import CreateZoneRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of CreateZoneRequestV1 from a JSON string
create_zone_request_v1_instance = CreateZoneRequestV1.from_json(json)
# print the JSON string representation of the object
print(CreateZoneRequestV1.to_json())

# convert the object into a dict
create_zone_request_v1_dict = create_zone_request_v1_instance.to_dict()
# create an instance of CreateZoneRequestV1 from a dict
create_zone_request_v1_from_dict = CreateZoneRequestV1.from_dict(create_zone_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


