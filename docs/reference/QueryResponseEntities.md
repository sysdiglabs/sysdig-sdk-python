# QueryResponseEntities

Metadata about the returned fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**EntityDefinition**](EntityDefinition.md) |  | [optional] 

## Example

```python
from sysdig_client.models.query_response_entities import QueryResponseEntities

# TODO update the JSON string below
json = "{}"
# create an instance of QueryResponseEntities from a JSON string
query_response_entities_instance = QueryResponseEntities.from_json(json)
# print the JSON string representation of the object
print(QueryResponseEntities.to_json())

# convert the object into a dict
query_response_entities_dict = query_response_entities_instance.to_dict()
# create an instance of QueryResponseEntities from a dict
query_response_entities_from_dict = QueryResponseEntities.from_dict(query_response_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


