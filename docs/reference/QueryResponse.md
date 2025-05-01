# QueryResponse

Response object containing query results and metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**QueryResponseEntities**](QueryResponseEntities.md) |  | 
**items** | **List[Dict[str, object]]** | Array of query results based on the query fields. | 
**id** | **str** | Unique identifier for the query execution. | 
**summary** | [**QuerySummary**](QuerySummary.md) |  | 

## Example

```python
from sysdig_client.models.query_response import QueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryResponse from a JSON string
query_response_instance = QueryResponse.from_json(json)
# print the JSON string representation of the object
print(QueryResponse.to_json())

# convert the object into a dict
query_response_dict = query_response_instance.to_dict()
# create an instance of QueryResponse from a dict
query_response_from_dict = QueryResponse.from_dict(query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


