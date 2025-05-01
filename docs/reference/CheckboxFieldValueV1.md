# CheckboxFieldValueV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Jira checkbox field id. | 
**value** | **str** | Jira checkbox field value. | 

## Example

```python
from sysdig_client.models.checkbox_field_value_v1 import CheckboxFieldValueV1

# TODO update the JSON string below
json = "{}"
# create an instance of CheckboxFieldValueV1 from a JSON string
checkbox_field_value_v1_instance = CheckboxFieldValueV1.from_json(json)
# print the JSON string representation of the object
print(CheckboxFieldValueV1.to_json())

# convert the object into a dict
checkbox_field_value_v1_dict = checkbox_field_value_v1_instance.to_dict()
# create an instance of CheckboxFieldValueV1 from a dict
checkbox_field_value_v1_from_dict = CheckboxFieldValueV1.from_dict(checkbox_field_value_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


