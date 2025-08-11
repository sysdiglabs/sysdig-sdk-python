# MetadataResponseV1DataValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the metric. |
**help** | **str** | A brief description of the metric. |
**unit** | **str** | The unit of measurement for the metric. |

## Example

```python
from sysdig_client.models.metadata_response_v1_data_value_inner import MetadataResponseV1DataValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataResponseV1DataValueInner from a JSON string
metadata_response_v1_data_value_inner_instance = MetadataResponseV1DataValueInner.from_json(json)
# print the JSON string representation of the object
print(MetadataResponseV1DataValueInner.to_json())

# convert the object into a dict
metadata_response_v1_data_value_inner_dict = metadata_response_v1_data_value_inner_instance.to_dict()
# create an instance of MetadataResponseV1DataValueInner from a dict
metadata_response_v1_data_value_inner_from_dict = MetadataResponseV1DataValueInner.from_dict(metadata_response_v1_data_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


