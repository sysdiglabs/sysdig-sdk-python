# LabelMatcherV1

Matcher to match alerts to inhibition rules.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_name** | **str** | Label to match. | 
**operator** | **str** | Match operator. | 
**value** | **str** | Label value to match in case operator is of type equality, or regular expression in case of operator is of type regex. | 

## Example

```python
from sysdig_client.models.label_matcher_v1 import LabelMatcherV1

# TODO update the JSON string below
json = "{}"
# create an instance of LabelMatcherV1 from a JSON string
label_matcher_v1_instance = LabelMatcherV1.from_json(json)
# print the JSON string representation of the object
print(LabelMatcherV1.to_json())

# convert the object into a dict
label_matcher_v1_dict = label_matcher_v1_instance.to_dict()
# create an instance of LabelMatcherV1 from a dict
label_matcher_v1_from_dict = LabelMatcherV1.from_dict(label_matcher_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


