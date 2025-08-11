# QueryResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Query status. | [optional]
**data** | [**QueryResponseV1Data**](QueryResponseV1Data.md) |  | [optional]
**warnings** | **List[str]** | A set of warning messages attached to the response. | [optional]
**infos** | **List[str]** | A set of information messages attached to the response. | [optional]

## Example

```python
from sysdig_client.models.query_response_v1 import QueryResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of QueryResponseV1 from a JSON string
query_response_v1_instance = QueryResponseV1.from_json(json)
# print the JSON string representation of the object
print(QueryResponseV1.to_json())

# convert the object into a dict
query_response_v1_dict = query_response_v1_instance.to_dict()
# create an instance of QueryResponseV1 from a dict
query_response_v1_from_dict = QueryResponseV1.from_dict(query_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


