# CreateUserRequestV1

Request to create the User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The email address of the user. If the activation flow is set, this address will be used to send the activation email.  | 
**first_name** | **str** | The name of the user.  | [optional] 
**last_name** | **str** | The surname of the user.  | [optional] 
**is_admin** | **bool** | **True** if the user has Administration permissions.  | [optional] [default to False]
**products** | [**List[Product]**](Product.md) | The user will be added to the default teams specified by this field. | [optional] 

## Example

```python
from sysdig_client.models.create_user_request_v1 import CreateUserRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserRequestV1 from a JSON string
create_user_request_v1_instance = CreateUserRequestV1.from_json(json)
# print the JSON string representation of the object
print(CreateUserRequestV1.to_json())

# convert the object into a dict
create_user_request_v1_dict = create_user_request_v1_instance.to_dict()
# create an instance of CreateUserRequestV1 from a dict
create_user_request_v1_from_dict = CreateUserRequestV1.from_dict(create_user_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


