# Page

Pagination information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | The number of events matching the search criteria. This number is always major or equal to the number of events returned.  | 
**prev** | **str** | The cursor that can be used to fetch a set of events before the first event returned in the &#x60;data&#x60; array. If this value is unset, then there are no events before the first event returned in the &#x60;data&#x60; array. By providing this value as &#x60;cursor&#x60; you will get the events preceding the first event returned in the &#x60;data&#x60; array.  | [optional] 
**next** | **str** | The cursor that can be used to fetch a set of events after the last event returned in the &#x60;data&#x60; array. If this value is unset, then there are no events after the last event returned  in the &#x60;data&#x60; array. By providing this value as &#x60;cursor&#x60; you will get the events following last event returned in the &#x60;data&#x60; array.  | [optional] 

## Example

```python
from sysdig_client.models.page import Page

# TODO update the JSON string below
json = "{}"
# create an instance of Page from a JSON string
page_instance = Page.from_json(json)
# print the JSON string representation of the object
print(Page.to_json())

# convert the object into a dict
page_dict = page_instance.to_dict()
# create an instance of Page from a dict
page_from_dict = Page.from_dict(page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


