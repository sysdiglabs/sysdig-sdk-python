# ActionParameterMetadata

Metadata that describes a parameter to be submitted for a Response Action execution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the parameter. | 
**description** | **str** | The description of the parameter. | 
**type** | **str** | The type of an Response Action parameter.\\ It may assume the following values:\\ * string\\ * integer\\ * boolean\\ This list of possible values may grow in the future.  | 
**required** | **bool** | If &#x60;true&#x60;, the parameter is mandatory. | 

## Example

```python
from sysdig_client.models.action_parameter_metadata import ActionParameterMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ActionParameterMetadata from a JSON string
action_parameter_metadata_instance = ActionParameterMetadata.from_json(json)
# print the JSON string representation of the object
print(ActionParameterMetadata.to_json())

# convert the object into a dict
action_parameter_metadata_dict = action_parameter_metadata_instance.to_dict()
# create an instance of ActionParameterMetadata from a dict
action_parameter_metadata_from_dict = ActionParameterMetadata.from_dict(action_parameter_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


