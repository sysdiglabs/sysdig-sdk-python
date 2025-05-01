# InvalidRequest1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**message** | **str** |  | 
**details** | **List[object]** |  | [optional] 

## Example

```python
from sysdig_client.models.invalid_request1 import InvalidRequest1

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidRequest1 from a JSON string
invalid_request1_instance = InvalidRequest1.from_json(json)
# print the JSON string representation of the object
print(InvalidRequest1.to_json())

# convert the object into a dict
invalid_request1_dict = invalid_request1_instance.to_dict()
# create an instance of InvalidRequest1 from a dict
invalid_request1_from_dict = InvalidRequest1.from_dict(invalid_request1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


