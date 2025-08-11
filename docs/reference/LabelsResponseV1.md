# LabelsResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Query status. | [optional]
**data** | **List[str]** | List of label names. | [optional]
**warnings** | **List[str]** | A set of warning messages attached to the response. | [optional]
**infos** | **List[str]** | A set of information messages attached to the response. | [optional]

## Example

```python
from sysdig_client.models.labels_response_v1 import LabelsResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of LabelsResponseV1 from a JSON string
labels_response_v1_instance = LabelsResponseV1.from_json(json)
# print the JSON string representation of the object
print(LabelsResponseV1.to_json())

# convert the object into a dict
labels_response_v1_dict = labels_response_v1_instance.to_dict()
# create an instance of LabelsResponseV1 from a dict
labels_response_v1_from_dict = LabelsResponseV1.from_dict(labels_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


