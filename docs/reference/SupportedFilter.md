# SupportedFilter

A supported field for filtering events.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Attribute onto which filtering is supported. | 
**type** | [**SupportedFilterType**](SupportedFilterType.md) |  | 
**operands** | [**List[Operand]**](Operand.md) | The list of supported operands for filtering events. | [optional] 

## Example

```python
from sysdig_client.models.supported_filter import SupportedFilter

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedFilter from a JSON string
supported_filter_instance = SupportedFilter.from_json(json)
# print the JSON string representation of the object
print(SupportedFilter.to_json())

# convert the object into a dict
supported_filter_dict = supported_filter_instance.to_dict()
# create an instance of SupportedFilter from a dict
supported_filter_from_dict = SupportedFilter.from_dict(supported_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


