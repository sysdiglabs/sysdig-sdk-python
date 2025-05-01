# PrivateConnectionInfoKafka


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keytab** | **str** | base64 encoded Kerberos keytab | [optional] 

## Example

```python
from sysdig_client.models.private_connection_info_kafka import PrivateConnectionInfoKafka

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateConnectionInfoKafka from a JSON string
private_connection_info_kafka_instance = PrivateConnectionInfoKafka.from_json(json)
# print the JSON string representation of the object
print(PrivateConnectionInfoKafka.to_json())

# convert the object into a dict
private_connection_info_kafka_dict = private_connection_info_kafka_instance.to_dict()
# create an instance of PrivateConnectionInfoKafka from a dict
private_connection_info_kafka_from_dict = PrivateConnectionInfoKafka.from_dict(private_connection_info_kafka_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


