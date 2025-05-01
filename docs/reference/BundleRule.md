# BundleRule

A Rule definition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_type** | **str** | The type of the rule. It may be one of the following: - vulnSeverityAndThreats - vulnDenyList - imageConfigDefaultUser - imageConfigLabel - imageConfigEnvVariable - imageConfigInstructionNotRecommended - imageConfigInstructionIsPkgManager - imageConfigCreationDate - imageConfigSensitiveInformationAndSecrets - pkgDenyList  | 
**predicates** | [**List[BundleRulePredicatesInner]**](BundleRulePredicatesInner.md) | The Predicates defining this Rule | 
**rule_id** | **str** |  | 

## Example

```python
from sysdig_client.models.bundle_rule import BundleRule

# TODO update the JSON string below
json = "{}"
# create an instance of BundleRule from a JSON string
bundle_rule_instance = BundleRule.from_json(json)
# print the JSON string representation of the object
print(BundleRule.to_json())

# convert the object into a dict
bundle_rule_dict = bundle_rule_instance.to_dict()
# create an instance of BundleRule from a dict
bundle_rule_from_dict = BundleRule.from_dict(bundle_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


