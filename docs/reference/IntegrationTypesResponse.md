# IntegrationTypesResponse

The list of supported integration types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[IntegrationType]**](IntegrationType.md) |  | 

## Example

```python
from sysdig_client.models.integration_types_response import IntegrationTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationTypesResponse from a JSON string
integration_types_response_instance = IntegrationTypesResponse.from_json(json)
# print the JSON string representation of the object
print(IntegrationTypesResponse.to_json())

# convert the object into a dict
integration_types_response_dict = integration_types_response_instance.to_dict()
# create an instance of IntegrationTypesResponse from a dict
integration_types_response_from_dict = IntegrationTypesResponse.from_dict(integration_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


