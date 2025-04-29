# DriftPreventedAction

Automatic action preventing the execution of a file not present in the original container image.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ActionType**](ActionType.md) |  | 
**is_successful** | **bool** | Whether or not the action was completed successfully. | [optional] 
**err_msg** | **str** | When &#x60;isSuccessful&#x60; is &#x60;false&#x60;, details on why the action failed.  | [optional] 

## Example

```python
from sysdig_client.models.drift_prevented_action import DriftPreventedAction

# TODO update the JSON string below
json = "{}"
# create an instance of DriftPreventedAction from a JSON string
drift_prevented_action_instance = DriftPreventedAction.from_json(json)
# print the JSON string representation of the object
print(DriftPreventedAction.to_json())

# convert the object into a dict
drift_prevented_action_dict = drift_prevented_action_instance.to_dict()
# create an instance of DriftPreventedAction from a dict
drift_prevented_action_from_dict = DriftPreventedAction.from_dict(drift_prevented_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


