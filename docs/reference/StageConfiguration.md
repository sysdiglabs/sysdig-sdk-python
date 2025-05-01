# StageConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | Scope to apply the policies for the given stage. An empty string or missing property implies the policies are always active. The scope is defined using a query language expression, which is a subset of the full metrics query language used in monitoring.  | [optional] 

## Example

```python
from sysdig_client.models.stage_configuration import StageConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of StageConfiguration from a JSON string
stage_configuration_instance = StageConfiguration.from_json(json)
# print the JSON string representation of the object
print(StageConfiguration.to_json())

# convert the object into a dict
stage_configuration_dict = stage_configuration_instance.to_dict()
# create an instance of StageConfiguration from a dict
stage_configuration_from_dict = StageConfiguration.from_dict(stage_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


