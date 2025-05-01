# ListPoliciesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**PoliciesPage**](PoliciesPage.md) |  | 
**data** | [**List[PolicySummary]**](PolicySummary.md) | Policies collection | 

## Example

```python
from sysdig_client.models.list_policies_response import ListPoliciesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListPoliciesResponse from a JSON string
list_policies_response_instance = ListPoliciesResponse.from_json(json)
# print the JSON string representation of the object
print(ListPoliciesResponse.to_json())

# convert the object into a dict
list_policies_response_dict = list_policies_response_instance.to_dict()
# create an instance of ListPoliciesResponse from a dict
list_policies_response_from_dict = ListPoliciesResponse.from_dict(list_policies_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


