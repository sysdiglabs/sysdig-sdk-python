# UserResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |   | [optional] 
**email** | **str** | The email address of the user.  | [optional] 
**first_name** | **str** | The name of the user.  | [optional] 
**last_name** | **str** | The last name of the user.  | [optional] 
**is_admin** | **bool** | **True** if the user has Administration permissions.  | [optional] 
**activation_status** | **str** | The current activation status of the user.  | [optional] 
**date_created** | **datetime** | The date and time when the user was created.  | [optional] 
**last_updated** | **datetime** | The date and time when the user was last updated.  | [optional] 
**version** | **int** | The current version of the resource.  | [optional] 

## Example

```python
from sysdig_client.models.user_response_v1 import UserResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of UserResponseV1 from a JSON string
user_response_v1_instance = UserResponseV1.from_json(json)
# print the JSON string representation of the object
print(UserResponseV1.to_json())

# convert the object into a dict
user_response_v1_dict = user_response_v1_instance.to_dict()
# create an instance of UserResponseV1 from a dict
user_response_v1_from_dict = UserResponseV1.from_dict(user_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


