# InventoryZone

a Zone

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The zone identifier | 
**name** | **str** | The zone name | 

## Example

```python
from sysdig_client.models.inventory_zone import InventoryZone

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryZone from a JSON string
inventory_zone_instance = InventoryZone.from_json(json)
# print the JSON string representation of the object
print(InventoryZone.to_json())

# convert the object into a dict
inventory_zone_dict = inventory_zone_instance.to_dict()
# create an instance of InventoryZone from a dict
inventory_zone_from_dict = InventoryZone.from_dict(inventory_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


