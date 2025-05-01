# CreateRiskAcceptedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_value** | **str** | A value to match with the entityType | 
**expiration_date** | **date** | Date when the accepted risk will expire (in YYYY-MM-DD format) | [optional] 
**reason** | **str** | Reason for acceptance | 
**description** | **str** | Description of why the accepted risk was created | 
**stages** | **List[str]** | List of stages where the risk acceptance is applied, empty list enables risk acceptance for all the stages | [optional] 
**entity_type** | **str** | The entity where the Accepted Risk will be applied. | 
**context** | [**CreateRiskAcceptedRequestAllOfContext**](CreateRiskAcceptedRequestAllOfContext.md) |  | 

## Example

```python
from sysdig_client.models.create_risk_accepted_request import CreateRiskAcceptedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRiskAcceptedRequest from a JSON string
create_risk_accepted_request_instance = CreateRiskAcceptedRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRiskAcceptedRequest.to_json())

# convert the object into a dict
create_risk_accepted_request_dict = create_risk_accepted_request_instance.to_dict()
# create an instance of CreateRiskAcceptedRequest from a dict
create_risk_accepted_request_from_dict = CreateRiskAcceptedRequest.from_dict(create_risk_accepted_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


