# BaseIntegrationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name to give to the integration | 
**is_enabled** | **bool** | If the forwarding should be enabled or not | [optional] [default to True]
**type** | [**IntegrationType**](IntegrationType.md) |  | 
**channels** | [**List[IntegrationChannel]**](IntegrationChannel.md) | Data types to forward. Must be compatible with the specified Integration type | [optional] 

## Example

```python
from sysdig_client.models.base_integration_payload import BaseIntegrationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BaseIntegrationPayload from a JSON string
base_integration_payload_instance = BaseIntegrationPayload.from_json(json)
# print the JSON string representation of the object
print(BaseIntegrationPayload.to_json())

# convert the object into a dict
base_integration_payload_dict = base_integration_payload_instance.to_dict()
# create an instance of BaseIntegrationPayload from a dict
base_integration_payload_from_dict = BaseIntegrationPayload.from_dict(base_integration_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


