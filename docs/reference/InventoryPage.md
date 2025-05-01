# InventoryPage

The total number of pages the matched the filter, and the next and previous page numbers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **int** | The next page | [optional] 
**previous** | **int** | The previous page | [optional] 
**total** | **int** | Total page count | 

## Example

```python
from sysdig_client.models.inventory_page import InventoryPage

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryPage from a JSON string
inventory_page_instance = InventoryPage.from_json(json)
# print the JSON string representation of the object
print(InventoryPage.to_json())

# convert the object into a dict
inventory_page_dict = inventory_page_instance.to_dict()
# create an instance of InventoryPage from a dict
inventory_page_from_dict = InventoryPage.from_dict(inventory_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


