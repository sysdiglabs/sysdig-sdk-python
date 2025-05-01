# InhibitionRuleResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID of the resource. | [optional] 
**version** | **int** | The current version of the resource. | [optional] 
**created_on** | **datetime** | Creation date. | [optional] 
**modified_on** | **datetime** | Last modification date. | [optional] 
**customer_id** | **int** | ID of customer that owns the inhibition rule. | [optional] 
**team_id** | **int** | ID of team that owns the inhibition rule. | [optional] 
**is_enabled** | **bool** | Indicates if the inhibition rule is enabled or not. | [optional] [default to True]
**name** | **str** | Name of the inhibition rule. | [optional] 
**description** | **str** | Description of the inhibition rule. | [optional] 
**source_matchers** | [**List[LabelMatcherV1]**](LabelMatcherV1.md) | List of source matchers for which one or more alerts have to exist for the inhibition to take effect. | [optional] 
**target_matchers** | [**List[LabelMatcherV1]**](LabelMatcherV1.md) | List of target matchers that have to be fulfilled by the target alerts to be muted. | [optional] 
**equal** | **List[str]** | List of labels that must have an equal value in the source and target alert for the inhibition to take effect. | [optional] 

## Example

```python
from sysdig_client.models.inhibition_rule_response_v1 import InhibitionRuleResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of InhibitionRuleResponseV1 from a JSON string
inhibition_rule_response_v1_instance = InhibitionRuleResponseV1.from_json(json)
# print the JSON string representation of the object
print(InhibitionRuleResponseV1.to_json())

# convert the object into a dict
inhibition_rule_response_v1_dict = inhibition_rule_response_v1_instance.to_dict()
# create an instance of InhibitionRuleResponseV1 from a dict
inhibition_rule_response_v1_from_dict = InhibitionRuleResponseV1.from_dict(inhibition_rule_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


