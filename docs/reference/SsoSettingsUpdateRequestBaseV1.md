# SsoSettingsUpdateRequestBaseV1

Update Request SSO Settings Base Schema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**SsoTypeV1**](SsoTypeV1.md) |  | 

## Example

```python
from sysdig_client.models.sso_settings_update_request_base_v1 import SsoSettingsUpdateRequestBaseV1

# TODO update the JSON string below
json = "{}"
# create an instance of SsoSettingsUpdateRequestBaseV1 from a JSON string
sso_settings_update_request_base_v1_instance = SsoSettingsUpdateRequestBaseV1.from_json(json)
# print the JSON string representation of the object
print(SsoSettingsUpdateRequestBaseV1.to_json())

# convert the object into a dict
sso_settings_update_request_base_v1_dict = sso_settings_update_request_base_v1_instance.to_dict()
# create an instance of SsoSettingsUpdateRequestBaseV1 from a dict
sso_settings_update_request_base_v1_from_dict = SsoSettingsUpdateRequestBaseV1.from_dict(sso_settings_update_request_base_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


