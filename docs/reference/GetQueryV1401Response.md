# GetQueryV1401Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | Epoch timestamp (milliseconds) when the error occurred. | 
**status** | **int** | HTTP status code of the response. | 
**error** | **str** | A human-readable error message. | 
**path** | **str** | The requested endpoint path that triggered the error. | 

## Example

```python
from sysdig_client.models.get_query_v1401_response import GetQueryV1401Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetQueryV1401Response from a JSON string
get_query_v1401_response_instance = GetQueryV1401Response.from_json(json)
# print the JSON string representation of the object
print(GetQueryV1401Response.to_json())

# convert the object into a dict
get_query_v1401_response_dict = get_query_v1401_response_instance.to_dict()
# create an instance of GetQueryV1401Response from a dict
get_query_v1401_response_from_dict = GetQueryV1401Response.from_dict(get_query_v1401_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


