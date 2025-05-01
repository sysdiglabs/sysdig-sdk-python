# AuthenticatedConnectionInfoElasticsearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | Elasticsearch instance endpoint URL | 
**index** | **str** | Name of the index to store the data in | 
**is_insecure** | **bool** | Don&#39;t verify TLS certificate | [optional] [default to False]
**auth** | **str** | Authentication method | 
**format** | **str** | If specified, transforms &#x60;content.fields&#x60; and &#x60;labels&#x60; * &#x60;KV_PAIRS&#x60; - from objects (i.e. &#x60;{\&quot;foo\&quot;: \&quot;bar\&quot;, ...}&#x60;) to arrays of objects with \&quot;key\&quot; and \&quot;value\&quot; properties {i.e. &#x60;[{\&quot;key\&quot; : \&quot;foo\&quot;, \&quot;value\&quot;: \&quot;bar\&quot;}, ...]&#x60;)  | [optional] 
**secret** | **str** | Authentication secret. To be set if auth is specified | 

## Example

```python
from sysdig_client.models.authenticated_connection_info_elasticsearch import AuthenticatedConnectionInfoElasticsearch

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatedConnectionInfoElasticsearch from a JSON string
authenticated_connection_info_elasticsearch_instance = AuthenticatedConnectionInfoElasticsearch.from_json(json)
# print the JSON string representation of the object
print(AuthenticatedConnectionInfoElasticsearch.to_json())

# convert the object into a dict
authenticated_connection_info_elasticsearch_dict = authenticated_connection_info_elasticsearch_instance.to_dict()
# create an instance of AuthenticatedConnectionInfoElasticsearch from a dict
authenticated_connection_info_elasticsearch_from_dict = AuthenticatedConnectionInfoElasticsearch.from_dict(authenticated_connection_info_elasticsearch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


