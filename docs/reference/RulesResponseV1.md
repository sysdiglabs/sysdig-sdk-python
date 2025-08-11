# RulesResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Request status. | [optional]
**data** | [**RulesResponseV1Data**](RulesResponseV1Data.md) |  | [optional]
**warnings** | **List[str]** | A set of warning messages attached to the response. | [optional]
**infos** | **List[str]** | A set of information messages attached to the response. | [optional]

## Example

```python
from sysdig_client.models.rules_response_v1 import RulesResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of RulesResponseV1 from a JSON string
rules_response_v1_instance = RulesResponseV1.from_json(json)
# print the JSON string representation of the object
print(RulesResponseV1.to_json())

# convert the object into a dict
rules_response_v1_dict = rules_response_v1_instance.to_dict()
# create an instance of RulesResponseV1 from a dict
rules_response_v1_from_dict = RulesResponseV1.from_dict(rules_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


