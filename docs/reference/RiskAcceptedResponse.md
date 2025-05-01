# RiskAcceptedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Accepted Risk ID | 
**expiration_date** | **date** | Date when the accepted risk will expire (in YYYY-MM-DD format) | [optional] 
**created_at** | **datetime** | Date when the Accepted Risk was created | [optional] 
**updated_at** | **datetime** | Date when the Accepted Risk was updated | [optional] 
**status** | **str** | Specifies whether the Accepted Risk is enabled or expired | 
**created_by** | **str** | User who created the risk acceptance | [optional] 
**updated_by** | **str** | User who last updated the risk acceptance | [optional] 
**entity_value** | **str** | A value to match with the entityType | 
**reason** | **str** | Reason for acceptance | 
**description** | **str** | Description of why the accepted risk was created | 
**stages** | **List[str]** | List of stages where the risk acceptance is applied, empty list enables risk acceptance for all the stages | [optional] 
**entity_type** | **str** | The entity where the Accepted Risk will be applied. | 
**context** | [**RiskAcceptedResponseAllOfContext**](RiskAcceptedResponseAllOfContext.md) |  | 

## Example

```python
from sysdig_client.models.risk_accepted_response import RiskAcceptedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RiskAcceptedResponse from a JSON string
risk_accepted_response_instance = RiskAcceptedResponse.from_json(json)
# print the JSON string representation of the object
print(RiskAcceptedResponse.to_json())

# convert the object into a dict
risk_accepted_response_dict = risk_accepted_response_instance.to_dict()
# create an instance of RiskAcceptedResponse from a dict
risk_accepted_response_from_dict = RiskAcceptedResponse.from_dict(risk_accepted_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


