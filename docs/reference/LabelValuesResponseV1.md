# LabelValuesResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Query status. | [optional]
**data** | **List[str]** | List of values associated with the specified label. | [optional]
**warnings** | **List[str]** | A set of warning messages attached to the response. | [optional]
**infos** | **List[str]** | A set of information messages attached to the response. | [optional]

## Example

```python
from sysdig_client.models.label_values_response_v1 import LabelValuesResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of LabelValuesResponseV1 from a JSON string
label_values_response_v1_instance = LabelValuesResponseV1.from_json(json)
# print the JSON string representation of the object
print(LabelValuesResponseV1.to_json())

# convert the object into a dict
label_values_response_v1_dict = label_values_response_v1_instance.to_dict()
# create an instance of LabelValuesResponseV1 from a dict
label_values_response_v1_from_dict = LabelValuesResponseV1.from_dict(label_values_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


