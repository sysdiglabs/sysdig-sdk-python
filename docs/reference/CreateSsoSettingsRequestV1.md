# CreateSsoSettingsRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | [**Product**](Product.md) | The product to which SSO settings is applied to. SSO settings are configured per specific product. | 
**is_active** | **bool** | Flag to indicate if the SSO settings is active. | [optional] 
**create_user_on_login** | **bool** | Flag to indicate if the user will be created automatically if not found in the system. | [optional] 
**is_password_login_enabled** | **bool** | Flag to indicate if the user will be able to login with password. | [optional] 
**is_single_logout_enabled** | **bool** | Flag to indicate if the single logout support is enabled. | [optional] 
**is_group_mapping_enabled** | **bool** | Flag to indicate if group mapping support is enabled. | [optional] 
**group_mapping_attribute_name** | **str** | The group mapping attribute name. | [optional] 
**config** | [**SsoSettingsCreateRequestBaseV1**](SsoSettingsCreateRequestBaseV1.md) |  | 

## Example

```python
from sysdig_client.models.create_sso_settings_request_v1 import CreateSsoSettingsRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSsoSettingsRequestV1 from a JSON string
create_sso_settings_request_v1_instance = CreateSsoSettingsRequestV1.from_json(json)
# print the JSON string representation of the object
print(CreateSsoSettingsRequestV1.to_json())

# convert the object into a dict
create_sso_settings_request_v1_dict = create_sso_settings_request_v1_instance.to_dict()
# create an instance of CreateSsoSettingsRequestV1 from a dict
create_sso_settings_request_v1_from_dict = CreateSsoSettingsRequestV1.from_dict(create_sso_settings_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


