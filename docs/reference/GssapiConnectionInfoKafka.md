# GssapiConnectionInfoKafka


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | **str** | The authentication method to optionally use. Currently supporting only GSSAPI | 
**principal** | **str** | GSSAPI principal | 
**realm** | **str** | GSSAPI realm | 
**service** | **str** | GSSAPI Service name | 
**krb5** | **str** | Kerberos krb5.conf file content for GSSAPI | 

## Example

```python
from sysdig_client.models.gssapi_connection_info_kafka import GssapiConnectionInfoKafka

# TODO update the JSON string below
json = "{}"
# create an instance of GssapiConnectionInfoKafka from a JSON string
gssapi_connection_info_kafka_instance = GssapiConnectionInfoKafka.from_json(json)
# print the JSON string representation of the object
print(GssapiConnectionInfoKafka.to_json())

# convert the object into a dict
gssapi_connection_info_kafka_dict = gssapi_connection_info_kafka_instance.to_dict()
# create an instance of GssapiConnectionInfoKafka from a dict
gssapi_connection_info_kafka_from_dict = GssapiConnectionInfoKafka.from_dict(gssapi_connection_info_kafka_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


