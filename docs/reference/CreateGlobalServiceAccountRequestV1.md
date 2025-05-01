# CreateGlobalServiceAccountRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The display name of the Service Account. | 
**expiration_date** | **int** | Time when the Service Account API key expires, | in number of milliseconds since January 1, 1970, 00:00:00 GMT | [optional] 
**system_roles** | **List[str]** | Array of System roles assigned to the global service account. | 

## Example

```python
from sysdig_client.models.create_global_service_account_request_v1 import CreateGlobalServiceAccountRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGlobalServiceAccountRequestV1 from a JSON string
create_global_service_account_request_v1_instance = CreateGlobalServiceAccountRequestV1.from_json(json)
# print the JSON string representation of the object
print(CreateGlobalServiceAccountRequestV1.to_json())

# convert the object into a dict
create_global_service_account_request_v1_dict = create_global_service_account_request_v1_instance.to_dict()
# create an instance of CreateGlobalServiceAccountRequestV1 from a dict
create_global_service_account_request_v1_from_dict = CreateGlobalServiceAccountRequestV1.from_dict(create_global_service_account_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


