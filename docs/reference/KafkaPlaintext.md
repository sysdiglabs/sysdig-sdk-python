# KafkaPlaintext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_tls_enabled** | **bool** |  | [optional] 

## Example

```python
from sysdig_client.models.kafka_plaintext import KafkaPlaintext

# TODO update the JSON string below
json = "{}"
# create an instance of KafkaPlaintext from a JSON string
kafka_plaintext_instance = KafkaPlaintext.from_json(json)
# print the JSON string representation of the object
print(KafkaPlaintext.to_json())

# convert the object into a dict
kafka_plaintext_dict = kafka_plaintext_instance.to_dict()
# create an instance of KafkaPlaintext from a dict
kafka_plaintext_from_dict = KafkaPlaintext.from_dict(kafka_plaintext_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


