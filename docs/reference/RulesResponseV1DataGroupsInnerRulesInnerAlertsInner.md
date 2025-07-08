# RulesResponseV1DataGroupsInnerRulesInnerAlertsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | Current state of the alert. | 
**active_at** | **datetime** | Timestamp when the alert became active. | 
**value** | **str** | The numerical value that triggered the alert. | 

## Example

```python
from sysdig_client.models.rules_response_v1_data_groups_inner_rules_inner_alerts_inner import RulesResponseV1DataGroupsInnerRulesInnerAlertsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RulesResponseV1DataGroupsInnerRulesInnerAlertsInner from a JSON string
rules_response_v1_data_groups_inner_rules_inner_alerts_inner_instance = RulesResponseV1DataGroupsInnerRulesInnerAlertsInner.from_json(json)
# print the JSON string representation of the object
print(RulesResponseV1DataGroupsInnerRulesInnerAlertsInner.to_json())

# convert the object into a dict
rules_response_v1_data_groups_inner_rules_inner_alerts_inner_dict = rules_response_v1_data_groups_inner_rules_inner_alerts_inner_instance.to_dict()
# create an instance of RulesResponseV1DataGroupsInnerRulesInnerAlertsInner from a dict
rules_response_v1_data_groups_inner_rules_inner_alerts_inner_from_dict = RulesResponseV1DataGroupsInnerRulesInnerAlertsInner.from_dict(rules_response_v1_data_groups_inner_rules_inner_alerts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


