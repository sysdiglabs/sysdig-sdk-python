# BOMMetadata

Provides additional information about a BOM.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | The date and time (timestamp) when the BOM was created. | [optional] 
**lifecycle** | **str** | The product lifecycle(s) that this BOM represents. | [optional] 
**tools** | **object** | The tool(s) used in the creation of the BOM. | [optional] 
**component** | [**SbomComponent**](SbomComponent.md) |  | [optional] 

## Example

```python
from sysdig_client.models.bom_metadata import BOMMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of BOMMetadata from a JSON string
bom_metadata_instance = BOMMetadata.from_json(json)
# print the JSON string representation of the object
print(BOMMetadata.to_json())

# convert the object into a dict
bom_metadata_dict = bom_metadata_instance.to_dict()
# create an instance of BOMMetadata from a dict
bom_metadata_from_dict = BOMMetadata.from_dict(bom_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


