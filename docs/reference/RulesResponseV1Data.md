# RulesResponseV1Data

Response payload containing rule groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[RulesResponseV1DataGroupsInner]**](RulesResponseV1DataGroupsInner.md) | List of rule groups. | [optional] 

## Example

```python
from sysdig_client.models.rules_response_v1_data import RulesResponseV1Data

# TODO update the JSON string below
json = "{}"
# create an instance of RulesResponseV1Data from a JSON string
rules_response_v1_data_instance = RulesResponseV1Data.from_json(json)
# print the JSON string representation of the object
print(RulesResponseV1Data.to_json())

# convert the object into a dict
rules_response_v1_data_dict = rules_response_v1_data_instance.to_dict()
# create an instance of RulesResponseV1Data from a dict
rules_response_v1_data_from_dict = RulesResponseV1Data.from_dict(rules_response_v1_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


