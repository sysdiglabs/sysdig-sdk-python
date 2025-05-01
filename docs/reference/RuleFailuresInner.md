# RuleFailuresInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | description of the failure | 
**remediation** | **str** | image configuration failure remediation | 
**arguments** | **object** |  | 
**package_ref** | **str** | reference to the affected package | [optional] 
**vulnerability_ref** | **str** | reference to the vulnerability | [optional] 
**risk_accept_refs** | **List[str]** | list of accepted risks for the failure | [optional] 

## Example

```python
from sysdig_client.models.rule_failures_inner import RuleFailuresInner

# TODO update the JSON string below
json = "{}"
# create an instance of RuleFailuresInner from a JSON string
rule_failures_inner_instance = RuleFailuresInner.from_json(json)
# print the JSON string representation of the object
print(RuleFailuresInner.to_json())

# convert the object into a dict
rule_failures_inner_dict = rule_failures_inner_instance.to_dict()
# create an instance of RuleFailuresInner from a dict
rule_failures_inner_from_dict = RuleFailuresInner.from_dict(rule_failures_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


