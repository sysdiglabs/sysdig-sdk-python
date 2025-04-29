# BaseAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ActionType**](ActionType.md) |  | 

## Example

```python
from sysdig_client.models.base_action import BaseAction

# TODO update the JSON string below
json = "{}"
# create an instance of BaseAction from a JSON string
base_action_instance = BaseAction.from_json(json)
# print the JSON string representation of the object
print(BaseAction.to_json())

# convert the object into a dict
base_action_dict = base_action_instance.to_dict()
# create an instance of BaseAction from a dict
base_action_from_dict = BaseAction.from_dict(base_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


