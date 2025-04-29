# StatsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api** | **str** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from sysdig_client.models.stats_inner import StatsInner

# TODO update the JSON string below
json = "{}"
# create an instance of StatsInner from a JSON string
stats_inner_instance = StatsInner.from_json(json)
# print the JSON string representation of the object
print(StatsInner.to_json())

# convert the object into a dict
stats_inner_dict = stats_inner_instance.to_dict()
# create an instance of StatsInner from a dict
stats_inner_from_dict = StatsInner.from_dict(stats_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


