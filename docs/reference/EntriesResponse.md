# EntriesResponse

The response to a GET entries call 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**Page**](Page.md) |  | [optional] 
**data** | [**List[EntriesResponseDataInner]**](EntriesResponseDataInner.md) | The actual data contained in one of the supported types of entry | [optional] 

## Example

```python
from sysdig_client.models.entries_response import EntriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EntriesResponse from a JSON string
entries_response_instance = EntriesResponse.from_json(json)
# print the JSON string representation of the object
print(EntriesResponse.to_json())

# convert the object into a dict
entries_response_dict = entries_response_instance.to_dict()
# create an instance of EntriesResponse from a dict
entries_response_from_dict = EntriesResponse.from_dict(entries_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


