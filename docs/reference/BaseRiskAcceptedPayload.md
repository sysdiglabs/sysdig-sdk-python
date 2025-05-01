# BaseRiskAcceptedPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_value** | **str** | A value to match with the entityType | [optional] 
**expiration_date** | **date** | Date when the accepted risk will expire (in YYYY-MM-DD format) | [optional] 
**reason** | **str** | Reason for acceptance | [optional] 
**description** | **str** | Description of why the accepted risk was created | [optional] 
**stages** | **List[str]** | List of stages where the risk acceptance is applied, empty list enables risk acceptance for all the stages | [optional] 

## Example

```python
from sysdig_client.models.base_risk_accepted_payload import BaseRiskAcceptedPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BaseRiskAcceptedPayload from a JSON string
base_risk_accepted_payload_instance = BaseRiskAcceptedPayload.from_json(json)
# print the JSON string representation of the object
print(BaseRiskAcceptedPayload.to_json())

# convert the object into a dict
base_risk_accepted_payload_dict = base_risk_accepted_payload_instance.to_dict()
# create an instance of BaseRiskAcceptedPayload from a dict
base_risk_accepted_payload_from_dict = BaseRiskAcceptedPayload.from_dict(base_risk_accepted_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


