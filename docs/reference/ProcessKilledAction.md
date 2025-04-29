# ProcessKilledAction

Process kill automatic action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ActionType**](ActionType.md) |  | 
**is_successful** | **bool** | Whether or not the action was completed successfully. | [optional] 
**err_msg** | **str** | When &#x60;isSuccessful&#x60; is &#x60;false&#x60;, details on why the action failed.  | [optional] 

## Example

```python
from sysdig_client.models.process_killed_action import ProcessKilledAction

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessKilledAction from a JSON string
process_killed_action_instance = ProcessKilledAction.from_json(json)
# print the JSON string representation of the object
print(ProcessKilledAction.to_json())

# convert the object into a dict
process_killed_action_dict = process_killed_action_instance.to_dict()
# create an instance of ProcessKilledAction from a dict
process_killed_action_from_dict = ProcessKilledAction.from_dict(process_killed_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


