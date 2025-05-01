# Rule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | rule&#39;s id | [optional] 
**rule_type** | **str** | rule type | 
**evaluation_result** | **str** | result of rule evaluation | [optional] 
**predicates** | [**List[Predicate]**](Predicate.md) | list of rule&#39;s predicates | [optional] 
**failure_type** | **str** | rule failure type | 
**description** | **str** | rule description | 
**failures** | [**List[RuleFailuresInner]**](RuleFailuresInner.md) | list of rule failures | [optional] 

## Example

```python
from sysdig_client.models.rule import Rule

# TODO update the JSON string below
json = "{}"
# create an instance of Rule from a JSON string
rule_instance = Rule.from_json(json)
# print the JSON string representation of the object
print(Rule.to_json())

# convert the object into a dict
rule_dict = rule_instance.to_dict()
# create an instance of Rule from a dict
rule_from_dict = Rule.from_dict(rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


