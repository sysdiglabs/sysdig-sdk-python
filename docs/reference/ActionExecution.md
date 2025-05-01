# ActionExecution

The submitted Response Action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the Response Action. | 
**caller_id** | **str** | The ID of the user that executed the Response action. | [optional] 
**action_type** | **str** | The name of the Response Action to execute. It may be one of the following: - KILL_PROCESS - KILL_CONTAINER - STOP_CONTAINER - PAUSE_CONTAINER - FILE_QUARANTINE - FILE_ACQUIRE - UNPAUSE_CONTAINER - FILE_UNQUARANTINE - START_CONTAINER  The following actions serve as the undo for previous actions: - START_CONTAINER: undo for STOP_CONTAINER\\ - UNPAUSE_CONTAINER: undo for PAUSE_CONTAINER\\ - FILE_UNQUARANTINE: undo for FILE_QUARANTINE\\  Do not use undo actions in [submitActionExecutionv1](#tag/Response-actions/operation/submitActionExecutionv1).  You can execute an undo actions using the service [undoActionExecutionV1](#tag/Response-actions/operation/undoActionExecutionV1).  | 
**execution_context** | **Dict[str, str]** | The context in which the Response Action is executed.\\ It may contain additional information on the Response Action being executed, such as the host name or the MAC address.\\ For example:\\ &#x60;&#x60;&#x60;json {     \&quot;host.hostName\&quot;: \&quot;my-host\&quot;,     \&quot;host.mac\&quot;: \&quot;00:00:00:00:00:00\&quot;,     \&quot;host.id\&quot;: \&quot;abc123\&quot; } &#x60;&#x60;&#x60;  | 
**parameters** | [**Dict[str, ActionExecutionParameterValue]**](ActionExecutionParameterValue.md) | The parameters used to request the Response Action execution. | 
**outputs** | [**Dict[str, ActionExecutionParameterValue]**](ActionExecutionParameterValue.md) | The parameters used to request the Response Action execution. | [optional] 
**failure** | [**Failure**](Failure.md) |  | [optional] 
**status** | [**ActionExecutionStatus**](ActionExecutionStatus.md) |  | 
**user_id** | **int** | The ID of the user that submitted the Response Action. | [optional] 
**created_at** | **datetime** | The date and time the Response Action was submitted. | 
**updated_at** | **datetime** | The date and time the Response Action was last updated. | [optional] 
**action_execution_id_being_undone** | **str** | The ID of the Response Action being undone. | [optional] 

## Example

```python
from sysdig_client.models.action_execution import ActionExecution

# TODO update the JSON string below
json = "{}"
# create an instance of ActionExecution from a JSON string
action_execution_instance = ActionExecution.from_json(json)
# print the JSON string representation of the object
print(ActionExecution.to_json())

# convert the object into a dict
action_execution_dict = action_execution_instance.to_dict()
# create an instance of ActionExecution from a dict
action_execution_from_dict = ActionExecution.from_dict(action_execution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


