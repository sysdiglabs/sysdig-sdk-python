# PaginatedIntegrationsResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**OffsetPaginatedResponsePage**](OffsetPaginatedResponsePage.md) |  | [optional] 
**data** | [**List[IntegrationResponseV1]**](IntegrationResponseV1.md) |  | [optional] 

## Example

```python
from sysdig_client.models.paginated_integrations_response_v1 import PaginatedIntegrationsResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedIntegrationsResponseV1 from a JSON string
paginated_integrations_response_v1_instance = PaginatedIntegrationsResponseV1.from_json(json)
# print the JSON string representation of the object
print(PaginatedIntegrationsResponseV1.to_json())

# convert the object into a dict
paginated_integrations_response_v1_dict = paginated_integrations_response_v1_instance.to_dict()
# create an instance of PaginatedIntegrationsResponseV1 from a dict
paginated_integrations_response_v1_from_dict = PaginatedIntegrationsResponseV1.from_dict(paginated_integrations_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


