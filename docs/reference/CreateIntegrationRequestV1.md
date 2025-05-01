# CreateIntegrationRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Integration name. | 
**is_all_teams** | **bool** | If **true**, the integration will be enabled for all teams. If **false**, the integration will be enabled for the teams specified in the *teamIds* field.  | [optional] 
**team_ids** | **List[int]** | List of Sysdig&#39;s internal team ids for which the integration will be enabled. This field is required if *isAllTeams* is **false**.  | [optional] 
**jira_project** | **str** | Associated Jira project id. Please refer to the [Jira documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-projects#api-group-projects \&quot;Jira project documentation\&quot;) for more info.  | 
**jira_url** | **str** | Customer&#39;s Jira URL. | 
**jira_email** | **str** | User&#39;s email associated with the Jira account. | 
**jira_access_token** | **str** | Jira access token for the provided Jira account. | 
**jira_assignee** | **str** | The default assignee Jira account id for this integration. Please refer to the [Jira documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-user-search/#api-group-user-search \&quot;Jira user documentation\&quot;) for more info.  | [optional] 
**jira_labels** | **List[str]** | The list of Jira labels available for this integration. Please refer to the [Jira documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-labels/#api-group-labels \&quot;Jira labels documentation\&quot;) for more info.  | [optional] 

## Example

```python
from sysdig_client.models.create_integration_request_v1 import CreateIntegrationRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIntegrationRequestV1 from a JSON string
create_integration_request_v1_instance = CreateIntegrationRequestV1.from_json(json)
# print the JSON string representation of the object
print(CreateIntegrationRequestV1.to_json())

# convert the object into a dict
create_integration_request_v1_dict = create_integration_request_v1_instance.to_dict()
# create an instance of CreateIntegrationRequestV1 from a dict
create_integration_request_v1_from_dict = CreateIntegrationRequestV1.from_dict(create_integration_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


