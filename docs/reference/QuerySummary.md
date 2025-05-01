# QuerySummary

Summary of query execution metrics and timing information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_after** | **int** | Time taken for results to become available in milliseconds. | 
**consumed_after** | **int** | Time taken to consume results in milliseconds. | 
**total_time** | **int** | Total query execution time in milliseconds. | 

## Example

```python
from sysdig_client.models.query_summary import QuerySummary

# TODO update the JSON string below
json = "{}"
# create an instance of QuerySummary from a JSON string
query_summary_instance = QuerySummary.from_json(json)
# print the JSON string representation of the object
print(QuerySummary.to_json())

# convert the object into a dict
query_summary_dict = query_summary_instance.to_dict()
# create an instance of QuerySummary from a dict
query_summary_from_dict = QuerySummary.from_dict(query_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


