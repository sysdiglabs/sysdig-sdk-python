# SubmitUndoActionExecutionRequest

The request for the undo of a Response Action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caller_id** | **str** | The ID of the user that executed the Response action. | [optional] 

## Example

```python
from sysdig_client.models.submit_undo_action_execution_request import SubmitUndoActionExecutionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitUndoActionExecutionRequest from a JSON string
submit_undo_action_execution_request_instance = SubmitUndoActionExecutionRequest.from_json(json)
# print the JSON string representation of the object
print(SubmitUndoActionExecutionRequest.to_json())

# convert the object into a dict
submit_undo_action_execution_request_dict = submit_undo_action_execution_request_instance.to_dict()
# create an instance of SubmitUndoActionExecutionRequest from a dict
submit_undo_action_execution_request_from_dict = SubmitUndoActionExecutionRequest.from_dict(submit_undo_action_execution_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


