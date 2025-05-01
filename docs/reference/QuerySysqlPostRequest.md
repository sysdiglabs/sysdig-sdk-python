# QuerySysqlPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**q** | **str** | The SysQL statement. | 
**limit** | **int** | The limit parameter defines the maximum number of items returned in the result set, specifically  within the items array in the response.   This parameter is optional. The recommended approach is to define the limit directly in the SysQL  statement using the LIMIT clause. If specified in the request body, it will override the limit set  in the statement. If not specified, a default limit of 50 will be applied.  | [optional] [default to 50]
**offset** | **int** | The offset parameter specifies how many result set objects to skip in a MATCH statement. Use it when  you want to ignore the first few items in the result set.   This parameter is optional. The recommended approach is to set the offset directly in the SysQL  statement using the OFFSET clause. If specified in the request body, it will override the offset  in the statement. If not specified, a default offset of 0 will be applied.  Use limit and offset together in SysQL to paginate results, splitting them into pages with a defined  number of items for display.  | [optional] [default to 0]
**deterministic_order** | **bool** | The deterministic_order parameter controls whether consistent ordering is enforced in the result set.  Ordering is implicitly applied when pagination options, such as limit and offset, are specified in the  request. This is an optional parameter.  | [optional] [default to False]

## Example

```python
from sysdig_client.models.query_sysql_post_request import QuerySysqlPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuerySysqlPostRequest from a JSON string
query_sysql_post_request_instance = QuerySysqlPostRequest.from_json(json)
# print the JSON string representation of the object
print(QuerySysqlPostRequest.to_json())

# convert the object into a dict
query_sysql_post_request_dict = query_sysql_post_request_instance.to_dict()
# create an instance of QuerySysqlPostRequest from a dict
query_sysql_post_request_from_dict = QuerySysqlPostRequest.from_dict(query_sysql_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


