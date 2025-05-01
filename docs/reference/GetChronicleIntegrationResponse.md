# GetChronicleIntegrationResponse

Get Google Chronicle Integration Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name to give to the integration | 
**is_enabled** | **bool** | If the forwarding should be enabled or not | [default to True]
**type** | [**IntegrationType**](IntegrationType.md) |  | 
**channels** | [**List[IntegrationChannel]**](IntegrationChannel.md) | Data types to forward. Must be compatible with the specified Integration type | 
**id** | **int** | The ID of the integration | 
**connection_info** | [**GetChronicleIntegrationResponseAllOfConnectionInfo**](GetChronicleIntegrationResponseAllOfConnectionInfo.md) |  | 

## Example

```python
from sysdig_client.models.get_chronicle_integration_response import GetChronicleIntegrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetChronicleIntegrationResponse from a JSON string
get_chronicle_integration_response_instance = GetChronicleIntegrationResponse.from_json(json)
# print the JSON string representation of the object
print(GetChronicleIntegrationResponse.to_json())

# convert the object into a dict
get_chronicle_integration_response_dict = get_chronicle_integration_response_instance.to_dict()
# create an instance of GetChronicleIntegrationResponse from a dict
get_chronicle_integration_response_from_dict = GetChronicleIntegrationResponse.from_dict(get_chronicle_integration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


