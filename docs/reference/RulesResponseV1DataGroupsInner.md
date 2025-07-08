# RulesResponseV1DataGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the rule group. | 
**interval** | **str** | Evaluation interval of the rule group. | 
**rules** | [**List[RulesResponseV1DataGroupsInnerRulesInner]**](RulesResponseV1DataGroupsInnerRulesInner.md) | List of rules in the group. | 

## Example

```python
from sysdig_client.models.rules_response_v1_data_groups_inner import RulesResponseV1DataGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RulesResponseV1DataGroupsInner from a JSON string
rules_response_v1_data_groups_inner_instance = RulesResponseV1DataGroupsInner.from_json(json)
# print the JSON string representation of the object
print(RulesResponseV1DataGroupsInner.to_json())

# convert the object into a dict
rules_response_v1_data_groups_inner_dict = rules_response_v1_data_groups_inner_instance.to_dict()
# create an instance of RulesResponseV1DataGroupsInner from a dict
rules_response_v1_data_groups_inner_from_dict = RulesResponseV1DataGroupsInner.from_dict(rules_response_v1_data_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


