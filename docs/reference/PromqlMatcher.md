# PromqlMatcher

A PromQL-style filter that narrows the dataset to resources matching specific labels. If not provided, no additional filtering is applied. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | A valid Prometheus label name. Must match ^[a-zA-Z_][a-zA-Z0-9_]*$ | 
**operator** | **str** | The operator to use in the filter:   - &#x60;EQUAL&#x60; (&#x60;&#x3D;&#x60;): Exact match   - &#x60;NOT_EQUAL&#x60; (&#x60;!&#x3D;&#x60;): Exclude exact match   - &#x60;REGEX_MATCH&#x60; (&#x60;&#x3D;~&#x60;): Regular expression match   - &#x60;REGEX_NOT_MATCH&#x60; (&#x60;!~&#x60;): Regular expression mismatch  | 
**value** | **str** | The value to match against. | 

## Example

```python
from sysdig_client.models.promql_matcher import PromqlMatcher

# TODO update the JSON string below
json = "{}"
# create an instance of PromqlMatcher from a JSON string
promql_matcher_instance = PromqlMatcher.from_json(json)
# print the JSON string representation of the object
print(PromqlMatcher.to_json())

# convert the object into a dict
promql_matcher_dict = promql_matcher_instance.to_dict()
# create an instance of PromqlMatcher from a dict
promql_matcher_from_dict = PromqlMatcher.from_dict(promql_matcher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


