# AuthenticatedConnectionInfoKafka


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
from sysdig_client.models.authenticated_connection_info_kafka import AuthenticatedConnectionInfoKafka

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatedConnectionInfoKafka from a JSON string
authenticated_connection_info_kafka_instance = AuthenticatedConnectionInfoKafka.from_json(json)
# print the JSON string representation of the object
print(AuthenticatedConnectionInfoKafka.to_json())

# convert the object into a dict
authenticated_connection_info_kafka_dict = authenticated_connection_info_kafka_instance.to_dict()
# create an instance of AuthenticatedConnectionInfoKafka from a dict
authenticated_connection_info_kafka_from_dict = AuthenticatedConnectionInfoKafka.from_dict(authenticated_connection_info_kafka_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


