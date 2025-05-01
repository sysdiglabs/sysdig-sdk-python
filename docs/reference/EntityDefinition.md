# EntityDefinition

Defines the structure and metadata of a field in the query result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the entity. | 
**alias** | **str** | The alias used in the query. | [optional] 
**definition** | [**EntityDefinitionDefinition**](EntityDefinitionDefinition.md) |  | 

## Example

```python
from sysdig_client.models.entity_definition import EntityDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of EntityDefinition from a JSON string
entity_definition_instance = EntityDefinition.from_json(json)
# print the JSON string representation of the object
print(EntityDefinition.to_json())

# convert the object into a dict
entity_definition_dict = entity_definition_instance.to_dict()
# create an instance of EntityDefinition from a dict
entity_definition_from_dict = EntityDefinition.from_dict(entity_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


