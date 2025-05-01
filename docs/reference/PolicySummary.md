# PolicySummary

Policy summary definition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The Policy ID | 
**name** | **str** | human readable policy name. | 
**identifier** | **str** | policy identifier generated from the name. | 
**description** | **str** | policy description | [optional] 
**stages** | **List[str]** | array of stages for the policy. An empty array means the policy is applied only when specifically requested by its identifier. It may be one of the following:   - runtime   - pipeline   - registry  | 

## Example

```python
from sysdig_client.models.policy_summary import PolicySummary

# TODO update the JSON string below
json = "{}"
# create an instance of PolicySummary from a JSON string
policy_summary_instance = PolicySummary.from_json(json)
# print the JSON string representation of the object
print(PolicySummary.to_json())

# convert the object into a dict
policy_summary_dict = policy_summary_instance.to_dict()
# create an instance of PolicySummary from a dict
policy_summary_from_dict = PolicySummary.from_dict(policy_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


