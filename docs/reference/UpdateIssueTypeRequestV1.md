# UpdateIssueTypeRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jira_open_status_id** | **str** | Jira status id mapped to open status. Please refer to the [Jira documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-status/#api-group-status \&quot;Jira status documentation\&quot;) for more info.  | 
**jira_in_progress_status_id** | **str** | Jira status id mapped to in progress status. Please refer to the [Jira documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-status/#api-group-status \&quot;Jira status documentation\&quot;) for more info.  | 
**jira_closed_status_id** | **str** | Jira status id mapped to closed status. Please refer to the [Jira documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-status/#api-group-status \&quot;Jira status documentation\&quot;) for more info.  | 
**custom_field_ids** | **List[str]** | List of supported custom field ids for the issue type. Please refer to the [Jira documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-createmeta-get \&quot;Jira issue type fields documentation\&quot;) for more info.  | 

## Example

```python
from sysdig_client.models.update_issue_type_request_v1 import UpdateIssueTypeRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIssueTypeRequestV1 from a JSON string
update_issue_type_request_v1_instance = UpdateIssueTypeRequestV1.from_json(json)
# print the JSON string representation of the object
print(UpdateIssueTypeRequestV1.to_json())

# convert the object into a dict
update_issue_type_request_v1_dict = update_issue_type_request_v1_instance.to_dict()
# create an instance of UpdateIssueTypeRequestV1 from a dict
update_issue_type_request_v1_from_dict = UpdateIssueTypeRequestV1.from_dict(update_issue_type_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


