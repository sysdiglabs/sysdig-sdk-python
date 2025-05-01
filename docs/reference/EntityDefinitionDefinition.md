# EntityDefinitionDefinition

Detailed definition of the field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**def_type** | **str** | Type of the definition. | 
**name** | **str** | Name of the field. | 
**type** | **str** | Data type of the field. | 
**hidden** | **bool** | Indicates if the field is hidden from view. | [optional] 

## Example

```python
from sysdig_client.models.entity_definition_definition import EntityDefinitionDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of EntityDefinitionDefinition from a JSON string
entity_definition_definition_instance = EntityDefinitionDefinition.from_json(json)
# print the JSON string representation of the object
print(EntityDefinitionDefinition.to_json())

# convert the object into a dict
entity_definition_definition_dict = entity_definition_definition_instance.to_dict()
# create an instance of EntityDefinitionDefinition from a dict
entity_definition_definition_from_dict = EntityDefinitionDefinition.from_dict(entity_definition_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


