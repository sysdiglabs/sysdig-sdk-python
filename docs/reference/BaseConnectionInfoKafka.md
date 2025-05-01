# BaseConnectionInfoKafka


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brokers** | **List[str]** | Kafka server endpoint. A Kafka cluster may provide several brokers; it follows the &#39;hostname: port&#39; (without protocol scheme). | 
**topic** | **str** | Kafka topic where you want to store the forwarded data | 
**balancer** | **str** | Algorithm that the client uses to multiplex data between the multiple Brokers. For compatibility with the Java client, Murmur2 is used as the default partitioner | [optional] [default to 'murmur2']
**compression** | **str** | Compression standard used for the data | [optional] 
**is_tls_enabled** | **bool** |  | [optional] 
**is_insecure** | **bool** | Skip TLS certificate verification | [optional] [default to False]

## Example

```python
from sysdig_client.models.base_connection_info_kafka import BaseConnectionInfoKafka

# TODO update the JSON string below
json = "{}"
# create an instance of BaseConnectionInfoKafka from a JSON string
base_connection_info_kafka_instance = BaseConnectionInfoKafka.from_json(json)
# print the JSON string representation of the object
print(BaseConnectionInfoKafka.to_json())

# convert the object into a dict
base_connection_info_kafka_dict = base_connection_info_kafka_instance.to_dict()
# create an instance of BaseConnectionInfoKafka from a dict
base_connection_info_kafka_from_dict = BaseConnectionInfoKafka.from_dict(base_connection_info_kafka_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


