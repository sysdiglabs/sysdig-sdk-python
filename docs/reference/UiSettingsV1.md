# UiSettingsV1

UI related settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_point** | [**EntryPointV1**](EntryPointV1.md) |  | [optional] 
**theme** | **str** | The color assigned to the team. | [optional] 

## Example

```python
from sysdig_client.models.ui_settings_v1 import UiSettingsV1

# TODO update the JSON string below
json = "{}"
# create an instance of UiSettingsV1 from a JSON string
ui_settings_v1_instance = UiSettingsV1.from_json(json)
# print the JSON string representation of the object
print(UiSettingsV1.to_json())

# convert the object into a dict
ui_settings_v1_dict = ui_settings_v1_instance.to_dict()
# create an instance of UiSettingsV1 from a dict
ui_settings_v1_from_dict = UiSettingsV1.from_dict(ui_settings_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


