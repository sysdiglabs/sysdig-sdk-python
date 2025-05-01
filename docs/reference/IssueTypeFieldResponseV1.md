# IssueTypeFieldResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Issue type field id. | 
**jira_id** | **str** | Issue type field id on Jira. | 
**jira_name** | **str** | Jira issue type field name. | 
**type** | **str** | Issue type field type. | 
**is_required** | **bool** | Indicates if the field is required. | 
**has_default_value** | **bool** | Indicates if the field has a default value. | 
**allowed_values** | [**List[IssueTypeFieldResponseV1AllowedValuesInner]**](IssueTypeFieldResponseV1AllowedValuesInner.md) | Allowed values for the field. | [optional] 

## Example

```python
from sysdig_client.models.issue_type_field_response_v1 import IssueTypeFieldResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of IssueTypeFieldResponseV1 from a JSON string
issue_type_field_response_v1_instance = IssueTypeFieldResponseV1.from_json(json)
# print the JSON string representation of the object
print(IssueTypeFieldResponseV1.to_json())

# convert the object into a dict
issue_type_field_response_v1_dict = issue_type_field_response_v1_instance.to_dict()
# create an instance of IssueTypeFieldResponseV1 from a dict
issue_type_field_response_v1_from_dict = IssueTypeFieldResponseV1.from_dict(issue_type_field_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


