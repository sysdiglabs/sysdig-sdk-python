# SupportedFiltersResponse

The list of supported attributes for filtering events.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SupportedFilter]**](SupportedFilter.md) | The list of supported attributes for filtering events. | 

## Example

```python
from sysdig_client.models.supported_filters_response import SupportedFiltersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedFiltersResponse from a JSON string
supported_filters_response_instance = SupportedFiltersResponse.from_json(json)
# print the JSON string representation of the object
print(SupportedFiltersResponse.to_json())

# convert the object into a dict
supported_filters_response_dict = supported_filters_response_instance.to_dict()
# create an instance of SupportedFiltersResponse from a dict
supported_filters_response_from_dict = SupportedFiltersResponse.from_dict(supported_filters_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


