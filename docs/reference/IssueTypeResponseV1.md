# IssueTypeResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Issue type ID. | 
**jira_id** | **str** | Issue type ID on Jira. | 
**jira_name** | **str** | Jira issue type name. | 
**jira_hierarchy_level** | **int** | Issue type hierarchy level on Jira. | 
**jira_open_status_id** | **str** | Jira status ID mapped to open status. | 
**jira_in_progress_status_id** | **str** | Jira status ID mapped to in progress status. | 
**jira_closed_status_id** | **str** | Jira status ID mapped to closed status. | 
**standard_fields** | [**List[IssueTypeFieldResponseV1]**](IssueTypeFieldResponseV1.md) | Standard fields for the issue type. | 
**custom_fields** | [**List[IssueTypeFieldResponseV1]**](IssueTypeFieldResponseV1.md) | Custom fields for the issue type. | [optional] 

## Example

```python
from sysdig_client.models.issue_type_response_v1 import IssueTypeResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of IssueTypeResponseV1 from a JSON string
issue_type_response_v1_instance = IssueTypeResponseV1.from_json(json)
# print the JSON string representation of the object
print(IssueTypeResponseV1.to_json())

# convert the object into a dict
issue_type_response_v1_dict = issue_type_response_v1_instance.to_dict()
# create an instance of IssueTypeResponseV1 from a dict
issue_type_response_v1_from_dict = IssueTypeResponseV1.from_dict(issue_type_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


