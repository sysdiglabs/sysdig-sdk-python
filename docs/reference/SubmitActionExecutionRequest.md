# SubmitActionExecutionRequest

The request for the execution of a Response Action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | **str** | The name of the Response Action to execute. It may be one of the following: - KILL_PROCESS - KILL_CONTAINER - STOP_CONTAINER - PAUSE_CONTAINER - FILE_QUARANTINE - FILE_ACQUIRE - UNPAUSE_CONTAINER - FILE_UNQUARANTINE - START_CONTAINER  The following actions serve as the undo for previous actions: - START_CONTAINER: undo for STOP_CONTAINER\\ - UNPAUSE_CONTAINER: undo for PAUSE_CONTAINER\\ - FILE_UNQUARANTINE: undo for FILE_QUARANTINE\\  Do not use undo actions in [submitActionExecutionv1](#tag/Response-actions/operation/submitActionExecutionv1).  You can execute an undo actions using the service [undoActionExecutionV1](#tag/Response-actions/operation/undoActionExecutionV1).  | 
**caller_id** | **str** | The ID of the user that executed the Response action. | [optional] 
**parameters** | [**Dict[str, ActionExecutionParameterValue]**](ActionExecutionParameterValue.md) | The parameters used to request the Response Action execution. | 

## Example

```python
from sysdig_client.models.submit_action_execution_request import SubmitActionExecutionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitActionExecutionRequest from a JSON string
submit_action_execution_request_instance = SubmitActionExecutionRequest.from_json(json)
# print the JSON string representation of the object
print(SubmitActionExecutionRequest.to_json())

# convert the object into a dict
submit_action_execution_request_dict = submit_action_execution_request_instance.to_dict()
# create an instance of SubmitActionExecutionRequest from a dict
submit_action_execution_request_from_dict = SubmitActionExecutionRequest.from_dict(submit_action_execution_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


