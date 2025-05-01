# BaseConnectionInfoElasticsearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | Elasticsearch instance endpoint URL | 
**index** | **str** | Name of the index to store the data in | 
**is_insecure** | **bool** | Don&#39;t verify TLS certificate | [optional] [default to False]
**auth** | **str** | Authentication method | [optional] 
**format** | **str** | If specified, transforms &#x60;content.fields&#x60; and &#x60;labels&#x60; * &#x60;KV_PAIRS&#x60; - from objects (i.e. &#x60;{\&quot;foo\&quot;: \&quot;bar\&quot;, ...}&#x60;) to arrays of objects with \&quot;key\&quot; and \&quot;value\&quot; properties {i.e. &#x60;[{\&quot;key\&quot; : \&quot;foo\&quot;, \&quot;value\&quot;: \&quot;bar\&quot;}, ...]&#x60;)  | [optional] 

## Example

```python
from sysdig_client.models.base_connection_info_elasticsearch import BaseConnectionInfoElasticsearch

# TODO update the JSON string below
json = "{}"
# create an instance of BaseConnectionInfoElasticsearch from a JSON string
base_connection_info_elasticsearch_instance = BaseConnectionInfoElasticsearch.from_json(json)
# print the JSON string representation of the object
print(BaseConnectionInfoElasticsearch.to_json())

# convert the object into a dict
base_connection_info_elasticsearch_dict = base_connection_info_elasticsearch_instance.to_dict()
# create an instance of BaseConnectionInfoElasticsearch from a dict
base_connection_info_elasticsearch_from_dict = BaseConnectionInfoElasticsearch.from_dict(base_connection_info_elasticsearch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


