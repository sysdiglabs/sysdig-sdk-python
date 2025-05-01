# InventoryResourceResponse

A paged response of resources that match the filter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[InventoryResource]**](InventoryResource.md) | The resources that matches the filter | 
**page** | [**InventoryPage**](InventoryPage.md) |  | 

## Example

```python
from sysdig_client.models.inventory_resource_response import InventoryResourceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryResourceResponse from a JSON string
inventory_resource_response_instance = InventoryResourceResponse.from_json(json)
# print the JSON string representation of the object
print(InventoryResourceResponse.to_json())

# convert the object into a dict
inventory_resource_response_dict = inventory_resource_response_instance.to_dict()
# create an instance of InventoryResourceResponse from a dict
inventory_resource_response_from_dict = InventoryResourceResponse.from_dict(inventory_resource_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


