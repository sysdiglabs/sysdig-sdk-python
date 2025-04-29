# CaptureAction

Outcome of the Take Capture action configured in the policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ActionType**](ActionType.md) |  | 
**is_successful** | **bool** | Whether or not the Capture was taken successfully. | [optional] 
**err_msg** | **str** | When &#x60;isSuccessful&#x60; is &#x60;false&#x60;, details on why the action failed.  | [optional] 
**token** | **str** | Token to retrieve the related capture. | [optional] 
**after_event_ns** | **int** | Amount of nanoseconds after the event the Capture spans.  | [optional] 
**before_event_ns** | **int** | Amount of nanoseconds before the event the Capture spans.  | [optional] 

## Example

```python
from sysdig_client.models.capture_action import CaptureAction

# TODO update the JSON string below
json = "{}"
# create an instance of CaptureAction from a JSON string
capture_action_instance = CaptureAction.from_json(json)
# print the JSON string representation of the object
print(CaptureAction.to_json())

# convert the object into a dict
capture_action_dict = capture_action_instance.to_dict()
# create an instance of CaptureAction from a dict
capture_action_from_dict = CaptureAction.from_dict(capture_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


