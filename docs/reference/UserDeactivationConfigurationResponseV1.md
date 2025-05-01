# UserDeactivationConfigurationResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **int** | The customer Id.  | [optional] 
**is_enabled** | **bool** | Specifies if user deactivation is enabled for this customer. | [optional] 
**number_days_before_deactivation** | **int** | Number of days before inactive users are deactivated.  | [optional] 

## Example

```python
from sysdig_client.models.user_deactivation_configuration_response_v1 import UserDeactivationConfigurationResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of UserDeactivationConfigurationResponseV1 from a JSON string
user_deactivation_configuration_response_v1_instance = UserDeactivationConfigurationResponseV1.from_json(json)
# print the JSON string representation of the object
print(UserDeactivationConfigurationResponseV1.to_json())

# convert the object into a dict
user_deactivation_configuration_response_v1_dict = user_deactivation_configuration_response_v1_instance.to_dict()
# create an instance of UserDeactivationConfigurationResponseV1 from a dict
user_deactivation_configuration_response_v1_from_dict = UserDeactivationConfigurationResponseV1.from_dict(user_deactivation_configuration_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


