# ServiceAccountWithKeyResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |   | [optional] 
**name** | **str** | Service Account display name. | [optional] 
**date_created** | **datetime** | Date and time when the Service Account was created. | [optional] 
**last_updated** | **datetime** | Date and time when the Service Account was last updated. | [optional] 
**last_used** | **datetime** | Date and time when the Service Account API key was last used. | [optional] 
**expiration_date** | **datetime** | Date and time when the Service Account API key expires. | [optional] 
**team_id** | **int** | Team ID of the team the service account is associated with. | [optional] 
**team_role** | **str** | The predefined team role for a Service Account, or an ID of a custom role. | [optional] 
**system_roles** | **List[str]** | Array of System roles assigned to the global service account. | [optional] 
**api_key** | **str** | Service Account API key | [optional] 

## Example

```python
from sysdig_client.models.service_account_with_key_response_v1 import ServiceAccountWithKeyResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountWithKeyResponseV1 from a JSON string
service_account_with_key_response_v1_instance = ServiceAccountWithKeyResponseV1.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountWithKeyResponseV1.to_json())

# convert the object into a dict
service_account_with_key_response_v1_dict = service_account_with_key_response_v1_instance.to_dict()
# create an instance of ServiceAccountWithKeyResponseV1 from a dict
service_account_with_key_response_v1_from_dict = ServiceAccountWithKeyResponseV1.from_dict(service_account_with_key_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


