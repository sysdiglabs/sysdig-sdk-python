# ServiceAccountResponseV1


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

## Example

```python
from sysdig_client.models.service_account_response_v1 import ServiceAccountResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountResponseV1 from a JSON string
service_account_response_v1_instance = ServiceAccountResponseV1.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountResponseV1.to_json())

# convert the object into a dict
service_account_response_v1_dict = service_account_response_v1_instance.to_dict()
# create an instance of ServiceAccountResponseV1 from a dict
service_account_response_v1_from_dict = ServiceAccountResponseV1.from_dict(service_account_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


