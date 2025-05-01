# UpdateIntegrationRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Integration name. | 
**is_enabled** | **bool** | Integration enabled status. | 
**is_all_teams** | **bool** | If **true**, the integration will be enabled for all teams. If **false**, the integration will be enabled for the teams specified in the *teamIds* field.  | 
**team_ids** | **List[int]** | List of Sysdig&#39;s internal team ids for which the integration will be enabled. This field is required if *isAllTeams* is **false**.  | 
**jira_url** | **str** | Customer&#39;s Jira URL. | 
**jira_email** | **str** | The user email associated with the Jira account. | 
**jira_access_token** | **str** | Jira access token for the provided Jira account. | 
**jira_assignee** | **str** | The default assignee Jira account ID for this integration. Please refer to the [Jira documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-user-search/#api-group-user-search \&quot;Jira user documentation\&quot;) for more info.  | 
**jira_labels** | **List[str]** | The list of Jira labels available for this integration. Please refer to the [Jira documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-labels/#api-group-labels \&quot;Jira labels documentation\&quot;) for more info.  | 
**parent_issue_type_id** | **int** | Internal Sysdig&#39;s issue type id, which will act as a parent issue type for the integration.  | 
**child_issue_type_id** | **int** | Internal Sysdig&#39;s issue type id, which will act as a child issue type for the integration.  | 

## Example

```python
from sysdig_client.models.update_integration_request_v1 import UpdateIntegrationRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIntegrationRequestV1 from a JSON string
update_integration_request_v1_instance = UpdateIntegrationRequestV1.from_json(json)
# print the JSON string representation of the object
print(UpdateIntegrationRequestV1.to_json())

# convert the object into a dict
update_integration_request_v1_dict = update_integration_request_v1_instance.to_dict()
# create an instance of UpdateIntegrationRequestV1 from a dict
update_integration_request_v1_from_dict = UpdateIntegrationRequestV1.from_dict(update_integration_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


