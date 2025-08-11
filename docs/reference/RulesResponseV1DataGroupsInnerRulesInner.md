# RulesResponseV1DataGroupsInnerRulesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of rule (alerting or recording). |
**name** | **str** | Name of the rule. |
**query** | **str** | PromQL query associated with the rule. |
**duration** | **str** | Duration for which the rule must be active before triggering. | [optional]
**labels** | **Dict[str, str]** | Labels assigned to the rule. | [optional]
**annotations** | **Dict[str, str]** | Annotations providing additional information about the rule. | [optional]
**alerts** | [**List[RulesResponseV1DataGroupsInnerRulesInnerAlertsInner]**](RulesResponseV1DataGroupsInnerRulesInnerAlertsInner.md) | List of active alerts for this rule (only for alerting rules). | [optional]

## Example

```python
from sysdig_client.models.rules_response_v1_data_groups_inner_rules_inner import RulesResponseV1DataGroupsInnerRulesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RulesResponseV1DataGroupsInnerRulesInner from a JSON string
rules_response_v1_data_groups_inner_rules_inner_instance = RulesResponseV1DataGroupsInnerRulesInner.from_json(json)
# print the JSON string representation of the object
print(RulesResponseV1DataGroupsInnerRulesInner.to_json())

# convert the object into a dict
rules_response_v1_data_groups_inner_rules_inner_dict = rules_response_v1_data_groups_inner_rules_inner_instance.to_dict()
# create an instance of RulesResponseV1DataGroupsInnerRulesInner from a dict
rules_response_v1_data_groups_inner_rules_inner_from_dict = RulesResponseV1DataGroupsInnerRulesInner.from_dict(rules_response_v1_data_groups_inner_rules_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


