# PrivateConnectionInfoElasticsearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | **str** | Authentication method | [optional] 
**secret** | **str** | Authentication secret. To be set if auth is specified | [optional] 

## Example

```python
from sysdig_client.models.private_connection_info_elasticsearch import PrivateConnectionInfoElasticsearch

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateConnectionInfoElasticsearch from a JSON string
private_connection_info_elasticsearch_instance = PrivateConnectionInfoElasticsearch.from_json(json)
# print the JSON string representation of the object
print(PrivateConnectionInfoElasticsearch.to_json())

# convert the object into a dict
private_connection_info_elasticsearch_dict = private_connection_info_elasticsearch_instance.to_dict()
# create an instance of PrivateConnectionInfoElasticsearch from a dict
private_connection_info_elasticsearch_from_dict = PrivateConnectionInfoElasticsearch.from_dict(private_connection_info_elasticsearch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


