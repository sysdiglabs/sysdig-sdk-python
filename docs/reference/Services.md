# Services

Certificate registrations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_id** | **int** | The certificate ID. | 
**service_type** | **str** | The service type. | 
**registered_at** | **datetime** | The timestamp the service was configured to use this certificate. | 
**service_id** | **str** | The integration ID for the service owning the integration that uses the certificate. | 

## Example

```python
from sysdig_client.models.services import Services

# TODO update the JSON string below
json = "{}"
# create an instance of Services from a JSON string
services_instance = Services.from_json(json)
# print the JSON string representation of the object
print(Services.to_json())

# convert the object into a dict
services_dict = services_instance.to_dict()
# create an instance of Services from a dict
services_from_dict = Services.from_dict(services_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


