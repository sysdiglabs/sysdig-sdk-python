# KafkaTlsEncrypted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_tls_enabled** | **bool** |  | [optional] 
**is_insecure** | **bool** | Skip TLS certificate verification | [optional] [default to False]

## Example

```python
from sysdig_client.models.kafka_tls_encrypted import KafkaTlsEncrypted

# TODO update the JSON string below
json = "{}"
# create an instance of KafkaTlsEncrypted from a JSON string
kafka_tls_encrypted_instance = KafkaTlsEncrypted.from_json(json)
# print the JSON string representation of the object
print(KafkaTlsEncrypted.to_json())

# convert the object into a dict
kafka_tls_encrypted_dict = kafka_tls_encrypted_instance.to_dict()
# create an instance of KafkaTlsEncrypted from a dict
kafka_tls_encrypted_from_dict = KafkaTlsEncrypted.from_dict(kafka_tls_encrypted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


