# CreateKafkaIntegrationRequestAllOfConnectionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brokers** | **List[str]** | Kafka server endpoint. A Kafka cluster may provide several brokers; it follows the &#39;hostname: port&#39; (without protocol scheme). | 
**topic** | **str** | Kafka topic where you want to store the forwarded data | 
**balancer** | **str** | Algorithm that the client uses to multiplex data between the multiple Brokers. For compatibility with the Java client, Murmur2 is used as the default partitioner | [optional] [default to 'murmur2']
**compression** | **str** | Compression standard used for the data | [optional] 
**is_tls_enabled** | **bool** |  | [optional] 
**is_insecure** | **bool** | Skip TLS certificate verification | [optional] [default to False]
**auth** | **str** | The authentication method to optionally use. Currently supporting only GSSAPI | 
**principal** | **str** | GSSAPI principal | 
**realm** | **str** | GSSAPI realm | 
**service** | **str** | GSSAPI Service name | 
**krb5** | **str** | Kerberos krb5.conf file content for GSSAPI | 
**keytab** | **str** | base64 encoded Kerberos keytab | 

## Example

```python
from sysdig_client.models.create_kafka_integration_request_all_of_connection_info import CreateKafkaIntegrationRequestAllOfConnectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKafkaIntegrationRequestAllOfConnectionInfo from a JSON string
create_kafka_integration_request_all_of_connection_info_instance = CreateKafkaIntegrationRequestAllOfConnectionInfo.from_json(json)
# print the JSON string representation of the object
print(CreateKafkaIntegrationRequestAllOfConnectionInfo.to_json())

# convert the object into a dict
create_kafka_integration_request_all_of_connection_info_dict = create_kafka_integration_request_all_of_connection_info_instance.to_dict()
# create an instance of CreateKafkaIntegrationRequestAllOfConnectionInfo from a dict
create_kafka_integration_request_all_of_connection_info_from_dict = CreateKafkaIntegrationRequestAllOfConnectionInfo.from_dict(create_kafka_integration_request_all_of_connection_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


