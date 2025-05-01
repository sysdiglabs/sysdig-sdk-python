# IssueTypesResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[IssueTypeResponseV1]**](IssueTypeResponseV1.md) | List of issue types. | [optional] 

## Example

```python
from sysdig_client.models.issue_types_response_v1 import IssueTypesResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of IssueTypesResponseV1 from a JSON string
issue_types_response_v1_instance = IssueTypesResponseV1.from_json(json)
# print the JSON string representation of the object
print(IssueTypesResponseV1.to_json())

# convert the object into a dict
issue_types_response_v1_dict = issue_types_response_v1_instance.to_dict()
# create an instance of IssueTypesResponseV1 from a dict
issue_types_response_v1_from_dict = IssueTypesResponseV1.from_dict(issue_types_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


