# GlobalSsoSettingsResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_password_login_enabled** | **bool** | Indicates whether password login is enabled. | [optional] 

## Example

```python
from sysdig_client.models.global_sso_settings_response_v1 import GlobalSsoSettingsResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalSsoSettingsResponseV1 from a JSON string
global_sso_settings_response_v1_instance = GlobalSsoSettingsResponseV1.from_json(json)
# print the JSON string representation of the object
print(GlobalSsoSettingsResponseV1.to_json())

# convert the object into a dict
global_sso_settings_response_v1_dict = global_sso_settings_response_v1_instance.to_dict()
# create an instance of GlobalSsoSettingsResponseV1 from a dict
global_sso_settings_response_v1_from_dict = GlobalSsoSettingsResponseV1.from_dict(global_sso_settings_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


