# ContainerKilledAction

Container kill automatic action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ActionType**](ActionType.md) |  | 
**is_successful** | **bool** | Whether or not the action was completed successfully. | [optional] 
**err_msg** | **str** | When &#x60;isSuccessful&#x60; is &#x60;false&#x60;, details on why the action failed.  | [optional] 

## Example

```python
from sysdig_client.models.container_killed_action import ContainerKilledAction

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerKilledAction from a JSON string
container_killed_action_instance = ContainerKilledAction.from_json(json)
# print the JSON string representation of the object
print(ContainerKilledAction.to_json())

# convert the object into a dict
container_killed_action_dict = container_killed_action_instance.to_dict()
# create an instance of ContainerKilledAction from a dict
container_killed_action_from_dict = ContainerKilledAction.from_dict(container_killed_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


