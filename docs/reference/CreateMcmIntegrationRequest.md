# CreateMcmIntegrationRequest

Create IBM Multicloud Manager Integration Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name to give to the integration | 
**is_enabled** | **bool** | If the forwarding should be enabled or not | [optional] [default to True]
**type** | [**IntegrationType**](IntegrationType.md) |  | 
**channels** | [**List[IntegrationChannel]**](IntegrationChannel.md) | Data types to forward. Must be compatible with the specified Integration type | [optional] 
**connection_info** | [**IBMMulticloudCloudCreateConnectionInfo**](IBMMulticloudCloudCreateConnectionInfo.md) |  | 

## Example

```python
from sysdig_client.models.create_mcm_integration_request import CreateMcmIntegrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMcmIntegrationRequest from a JSON string
create_mcm_integration_request_instance = CreateMcmIntegrationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMcmIntegrationRequest.to_json())

# convert the object into a dict
create_mcm_integration_request_dict = create_mcm_integration_request_instance.to_dict()
# create an instance of CreateMcmIntegrationRequest from a dict
create_mcm_integration_request_from_dict = CreateMcmIntegrationRequest.from_dict(create_mcm_integration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


