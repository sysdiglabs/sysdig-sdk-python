# UpdateUserDeactivationConfigurationRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | Specifies if user deactivation is enabled for this customer. | 
**number_days_before_deactivation** | **int** | Number of days before inactive users are deactivated.  | 

## Example

```python
from sysdig_client.models.update_user_deactivation_configuration_request_v1 import UpdateUserDeactivationConfigurationRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserDeactivationConfigurationRequestV1 from a JSON string
update_user_deactivation_configuration_request_v1_instance = UpdateUserDeactivationConfigurationRequestV1.from_json(json)
# print the JSON string representation of the object
print(UpdateUserDeactivationConfigurationRequestV1.to_json())

# convert the object into a dict
update_user_deactivation_configuration_request_v1_dict = update_user_deactivation_configuration_request_v1_instance.to_dict()
# create an instance of UpdateUserDeactivationConfigurationRequestV1 from a dict
update_user_deactivation_configuration_request_v1_from_dict = UpdateUserDeactivationConfigurationRequestV1.from_dict(update_user_deactivation_configuration_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


