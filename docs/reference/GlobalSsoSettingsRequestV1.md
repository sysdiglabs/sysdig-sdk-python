# GlobalSsoSettingsRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_password_login_enabled** | **bool** | Set to &#x60;true&#x60; to enable password login when SSO is enabled, or &#x60;false&#x60; to disable it. |

## Example

```python
from sysdig_client.models.global_sso_settings_request_v1 import GlobalSsoSettingsRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalSsoSettingsRequestV1 from a JSON string
global_sso_settings_request_v1_instance = GlobalSsoSettingsRequestV1.from_json(json)
# print the JSON string representation of the object
print(GlobalSsoSettingsRequestV1.to_json())

# convert the object into a dict
global_sso_settings_request_v1_dict = global_sso_settings_request_v1_instance.to_dict()
# create an instance of GlobalSsoSettingsRequestV1 from a dict
global_sso_settings_request_v1_from_dict = GlobalSsoSettingsRequestV1.from_dict(global_sso_settings_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


