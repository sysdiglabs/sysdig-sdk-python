# BaseRiskAcceptedResponsePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Accepted Risk ID | [optional] 
**expiration_date** | **date** | Date when the accepted risk will expire (in YYYY-MM-DD format) | [optional] 
**created_at** | **datetime** | Date when the Accepted Risk was created | [optional] 
**updated_at** | **datetime** | Date when the Accepted Risk was updated | [optional] 
**status** | **str** | Specifies whether the Accepted Risk is enabled or expired | [optional] 
**created_by** | **str** | User who created the risk acceptance | [optional] 
**updated_by** | **str** | User who last updated the risk acceptance | [optional] 

## Example

```python
from sysdig_client.models.base_risk_accepted_response_payload import BaseRiskAcceptedResponsePayload

# TODO update the JSON string below
json = "{}"
# create an instance of BaseRiskAcceptedResponsePayload from a JSON string
base_risk_accepted_response_payload_instance = BaseRiskAcceptedResponsePayload.from_json(json)
# print the JSON string representation of the object
print(BaseRiskAcceptedResponsePayload.to_json())

# convert the object into a dict
base_risk_accepted_response_payload_dict = base_risk_accepted_response_payload_instance.to_dict()
# create an instance of BaseRiskAcceptedResponsePayload from a dict
base_risk_accepted_response_payload_from_dict = BaseRiskAcceptedResponsePayload.from_dict(base_risk_accepted_response_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


