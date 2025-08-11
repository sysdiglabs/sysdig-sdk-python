# QueryResponseV1Data

The result of the query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_type** | **str** | Type of the result set. | [optional]
**result** | [**QueryResponseV1DataResult**](QueryResponseV1DataResult.md) |  | [optional]

## Example

```python
from sysdig_client.models.query_response_v1_data import QueryResponseV1Data

# TODO update the JSON string below
json = "{}"
# create an instance of QueryResponseV1Data from a JSON string
query_response_v1_data_instance = QueryResponseV1Data.from_json(json)
# print the JSON string representation of the object
print(QueryResponseV1Data.to_json())

# convert the object into a dict
query_response_v1_data_dict = query_response_v1_data_instance.to_dict()
# create an instance of QueryResponseV1Data from a dict
query_response_v1_data_from_dict = QueryResponseV1Data.from_dict(query_response_v1_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


