# AllSsoSettingsResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SsoSettingsResponseV1]**](SsoSettingsResponseV1.md) | The list of SSO settings. | [optional] 

## Example

```python
from sysdig_client.models.all_sso_settings_response_v1 import AllSsoSettingsResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of AllSsoSettingsResponseV1 from a JSON string
all_sso_settings_response_v1_instance = AllSsoSettingsResponseV1.from_json(json)
# print the JSON string representation of the object
print(AllSsoSettingsResponseV1.to_json())

# convert the object into a dict
all_sso_settings_response_v1_dict = all_sso_settings_response_v1_instance.to_dict()
# create an instance of AllSsoSettingsResponseV1 from a dict
all_sso_settings_response_v1_from_dict = AllSsoSettingsResponseV1.from_dict(all_sso_settings_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


