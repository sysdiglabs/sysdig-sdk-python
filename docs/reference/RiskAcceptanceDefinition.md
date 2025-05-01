# RiskAcceptanceDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id of the risk acceptance | 
**entity_type** | **str** | entity type for the risk | 
**entity_value** | **str** | entity value relative to the the entity type | 
**context** | [**List[Context]**](Context.md) |  | 
**status** | **str** |  | 
**reason** | **str** | risk acceptance reason | [optional] 
**description** | **str** | risk acceptance description | [optional] 
**expiration_date** | **date** |  | 
**created_at** | **str** | datetime of creation | 
**updated_at** | **str** | datetime of last update | 

## Example

```python
from sysdig_client.models.risk_acceptance_definition import RiskAcceptanceDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of RiskAcceptanceDefinition from a JSON string
risk_acceptance_definition_instance = RiskAcceptanceDefinition.from_json(json)
# print the JSON string representation of the object
print(RiskAcceptanceDefinition.to_json())

# convert the object into a dict
risk_acceptance_definition_dict = risk_acceptance_definition_instance.to_dict()
# create an instance of RiskAcceptanceDefinition from a dict
risk_acceptance_definition_from_dict = RiskAcceptanceDefinition.from_dict(risk_acceptance_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


