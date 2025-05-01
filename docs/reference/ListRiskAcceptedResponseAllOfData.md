# ListRiskAcceptedResponseAllOfData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | The entity where the Accepted Risk will be applied. | 
**context** | [**RiskAcceptedResponseAllOfContext**](RiskAcceptedResponseAllOfContext.md) |  | 
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

## Example

```python
from sysdig_client.models.list_risk_accepted_response_all_of_data import ListRiskAcceptedResponseAllOfData

# TODO update the JSON string below
json = "{}"
# create an instance of ListRiskAcceptedResponseAllOfData from a JSON string
list_risk_accepted_response_all_of_data_instance = ListRiskAcceptedResponseAllOfData.from_json(json)
# print the JSON string representation of the object
print(ListRiskAcceptedResponseAllOfData.to_json())

# convert the object into a dict
list_risk_accepted_response_all_of_data_dict = list_risk_accepted_response_all_of_data_instance.to_dict()
# create an instance of ListRiskAcceptedResponseAllOfData from a dict
list_risk_accepted_response_all_of_data_from_dict = ListRiskAcceptedResponseAllOfData.from_dict(list_risk_accepted_response_all_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


