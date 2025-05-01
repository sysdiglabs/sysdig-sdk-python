# IntegrationResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Integration id. | 
**name** | **str** | Integration name. | 
**created_at** | **datetime** | Integration creation date. | 
**modified_at** | **datetime** | Integration modification date. | 
**deleted_at** | **datetime** | Integration deletion date. | [optional] 
**customer_id** | **int** | Customer identifier for which the integration was created. | 
**is_enabled** | **bool** | Integration enabled status. | 
**is_valid** | **bool** | Integration valid status. | 
**is_all_teams** | **bool** | **True** if the integration is enabled for all teams, **false** otherwise and the *teamIds* for which is accessible will be defined.  | 
**team_ids** | **List[int]** | The list of internal Sysdig team ids that the integration is enabled for. | [optional] 
**jira_project_id** | **str** | Jira project id. | 
**jira_project_name** | **str** | Jira project name. | [optional] 
**jira_url** | **str** | Customer&#39;s Jira URL. | 
**jira_email** | **str** | User&#39;s Jira email. | 
**jira_assignee** | **str** | The default assignee account id for this integration. | [optional] 
**jira_labels** | **List[str]** | The list of labels available for this integration. | [optional] 
**parent_issue_type** | [**IssueTypeResponseV1**](IssueTypeResponseV1.md) | Parent issue type for the integration. | [optional] 
**child_issue_type** | [**IssueTypeResponseV1**](IssueTypeResponseV1.md) | Child issue type for the integration. | [optional] 

## Example

```python
from sysdig_client.models.integration_response_v1 import IntegrationResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationResponseV1 from a JSON string
integration_response_v1_instance = IntegrationResponseV1.from_json(json)
# print the JSON string representation of the object
print(IntegrationResponseV1.to_json())

# convert the object into a dict
integration_response_v1_dict = integration_response_v1_instance.to_dict()
# create an instance of IntegrationResponseV1 from a dict
integration_response_v1_from_dict = IntegrationResponseV1.from_dict(integration_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


