# ServicesResponse

LedgersResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Services]**](Services.md) |  | 

## Example

```python
from sysdig_client.models.services_response import ServicesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServicesResponse from a JSON string
services_response_instance = ServicesResponse.from_json(json)
# print the JSON string representation of the object
print(ServicesResponse.to_json())

# convert the object into a dict
services_response_dict = services_response_instance.to_dict()
# create an instance of ServicesResponse from a dict
services_response_from_dict = ServicesResponse.from_dict(services_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


