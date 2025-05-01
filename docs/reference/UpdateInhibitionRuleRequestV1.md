# UpdateInhibitionRuleRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | Indicates if the inhibition rule is enabled or not. | [optional] [default to True]
**name** | **str** | Name of the inhibition rule. If provided, must be unique. | [optional] 
**description** | **str** | Description of the inhibition rule. | [optional] 
**source_matchers** | [**List[LabelMatcherV1]**](LabelMatcherV1.md) | List of source matchers for which one or more alerts have to exist for the inhibition to take effect. | 
**target_matchers** | [**List[LabelMatcherV1]**](LabelMatcherV1.md) | List of target matchers that have to be fulfilled by the target alerts to be muted. | 
**equal** | **List[str]** | List of labels that must have an equal value in the source and target alert for the inhibition to take effect. | [optional] 
**version** | **int** | The current version of the resource. | 

## Example

```python
from sysdig_client.models.update_inhibition_rule_request_v1 import UpdateInhibitionRuleRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInhibitionRuleRequestV1 from a JSON string
update_inhibition_rule_request_v1_instance = UpdateInhibitionRuleRequestV1.from_json(json)
# print the JSON string representation of the object
print(UpdateInhibitionRuleRequestV1.to_json())

# convert the object into a dict
update_inhibition_rule_request_v1_dict = update_inhibition_rule_request_v1_instance.to_dict()
# create an instance of UpdateInhibitionRuleRequestV1 from a dict
update_inhibition_rule_request_v1_from_dict = UpdateInhibitionRuleRequestV1.from_dict(update_inhibition_rule_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


