# IpFiltersSettingsV1

Used to configure IP filters settings. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_filtering_enabled** | **bool** | Specifies if IP filtering is enabled. | [optional] 

## Example

```python
from sysdig_client.models.ip_filters_settings_v1 import IpFiltersSettingsV1

# TODO update the JSON string below
json = "{}"
# create an instance of IpFiltersSettingsV1 from a JSON string
ip_filters_settings_v1_instance = IpFiltersSettingsV1.from_json(json)
# print the JSON string representation of the object
print(IpFiltersSettingsV1.to_json())

# convert the object into a dict
ip_filters_settings_v1_dict = ip_filters_settings_v1_instance.to_dict()
# create an instance of IpFiltersSettingsV1 from a dict
ip_filters_settings_v1_from_dict = IpFiltersSettingsV1.from_dict(ip_filters_settings_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


