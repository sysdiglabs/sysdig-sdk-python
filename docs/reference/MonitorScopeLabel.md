# MonitorScopeLabel

Scope Label.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The label key. | [optional]
**value** | **List[str]** | The scope label value(s) | [optional]

## Example

```python
from sysdig_client.models.monitor_scope_label import MonitorScopeLabel

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorScopeLabel from a JSON string
monitor_scope_label_instance = MonitorScopeLabel.from_json(json)
# print the JSON string representation of the object
print(MonitorScopeLabel.to_json())

# convert the object into a dict
monitor_scope_label_dict = monitor_scope_label_instance.to_dict()
# create an instance of MonitorScopeLabel from a dict
monitor_scope_label_from_dict = MonitorScopeLabel.from_dict(monitor_scope_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


