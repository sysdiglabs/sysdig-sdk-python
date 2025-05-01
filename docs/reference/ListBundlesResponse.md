# ListBundlesResponse

Bundles list response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**PoliciesPage**](PoliciesPage.md) |  | 
**data** | [**List[GetBundleResponse]**](GetBundleResponse.md) | Bundles collection | 

## Example

```python
from sysdig_client.models.list_bundles_response import ListBundlesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListBundlesResponse from a JSON string
list_bundles_response_instance = ListBundlesResponse.from_json(json)
# print the JSON string representation of the object
print(ListBundlesResponse.to_json())

# convert the object into a dict
list_bundles_response_dict = list_bundles_response_instance.to_dict()
# create an instance of ListBundlesResponse from a dict
list_bundles_response_from_dict = ListBundlesResponse.from_dict(list_bundles_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


