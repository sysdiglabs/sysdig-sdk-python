# CreateKafkaIntegrationRequest

Create Kafka Integration Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name to give to the integration | 
**is_enabled** | **bool** | If the forwarding should be enabled or not | [optional] [default to True]
**type** | [**IntegrationType**](IntegrationType.md) |  | 
**channels** | [**List[IntegrationChannel]**](IntegrationChannel.md) | Data types to forward. Must be compatible with the specified Integration type | [optional] 
**connection_info** | [**CreateKafkaIntegrationRequestAllOfConnectionInfo**](CreateKafkaIntegrationRequestAllOfConnectionInfo.md) |  | 

## Example

```python
from sysdig_client.models.create_kafka_integration_request import CreateKafkaIntegrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKafkaIntegrationRequest from a JSON string
create_kafka_integration_request_instance = CreateKafkaIntegrationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateKafkaIntegrationRequest.to_json())

# convert the object into a dict
create_kafka_integration_request_dict = create_kafka_integration_request_instance.to_dict()
# create an instance of CreateKafkaIntegrationRequest from a dict
create_kafka_integration_request_from_dict = CreateKafkaIntegrationRequest.from_dict(create_kafka_integration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


