# ActionExecutions

A list of Response Action executions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ActionExecution]**](ActionExecution.md) | The list of Response Actions. | 

## Example

```python
from sysdig_client.models.action_executions import ActionExecutions

# TODO update the JSON string below
json = "{}"
# create an instance of ActionExecutions from a JSON string
action_executions_instance = ActionExecutions.from_json(json)
# print the JSON string representation of the object
print(ActionExecutions.to_json())

# convert the object into a dict
action_executions_dict = action_executions_instance.to_dict()
# create an instance of ActionExecutions from a dict
action_executions_from_dict = ActionExecutions.from_dict(action_executions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


