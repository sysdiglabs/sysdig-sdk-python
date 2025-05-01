# ResponseAction

The action metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The name of the Response Action to execute. It may be one of the following: - KILL_PROCESS - KILL_CONTAINER - STOP_CONTAINER - PAUSE_CONTAINER - FILE_QUARANTINE - FILE_ACQUIRE - UNPAUSE_CONTAINER - FILE_UNQUARANTINE - START_CONTAINER  The following actions serve as the undo for previous actions: - START_CONTAINER: undo for STOP_CONTAINER\\ - UNPAUSE_CONTAINER: undo for PAUSE_CONTAINER\\ - FILE_UNQUARANTINE: undo for FILE_QUARANTINE\\  Do not use undo actions in [submitActionExecutionv1](#tag/Response-actions/operation/submitActionExecutionv1).  You can execute an undo actions using the service [undoActionExecutionV1](#tag/Response-actions/operation/undoActionExecutionV1).  | 
**parameters** | [**List[ActionParameterMetadata]**](ActionParameterMetadata.md) | the list of parameters that the action supports | 
**outputs** | [**List[ActionOutputsMetadata]**](ActionOutputsMetadata.md) |  | [optional] 
**description** | **str** | The description of the action. | 
**is_undoable** | **bool** | Whether the action is undoable. | 

## Example

```python
from sysdig_client.models.response_action import ResponseAction

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseAction from a JSON string
response_action_instance = ResponseAction.from_json(json)
# print the JSON string representation of the object
print(ResponseAction.to_json())

# convert the object into a dict
response_action_dict = response_action_instance.to_dict()
# create an instance of ResponseAction from a dict
response_action_from_dict = ResponseAction.from_dict(response_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


