# PoliciesPage

Page details, providing both returned and total count of matched elements. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**returned** | **int** | The number returned elements: always less or equal the limit specified in the request.  | 
**matched** | **int** | Total count of elements matched the provided filter.  | 
**next** | **str** | Cursor used to retrieve the next page of results. | [optional] 

## Example

```python
from sysdig_client.models.policies_page import PoliciesPage

# TODO update the JSON string below
json = "{}"
# create an instance of PoliciesPage from a JSON string
policies_page_instance = PoliciesPage.from_json(json)
# print the JSON string representation of the object
print(PoliciesPage.to_json())

# convert the object into a dict
policies_page_dict = policies_page_instance.to_dict()
# create an instance of PoliciesPage from a dict
policies_page_from_dict = PoliciesPage.from_dict(policies_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


