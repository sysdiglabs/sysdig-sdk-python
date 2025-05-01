# UpdateUserRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | The name of the user.  | [optional] 
**last_name** | **str** | The surname of the user.  | [optional] 
**is_admin** | **bool** | **True** if the user has Administration permissions.  | [optional] 
**version** | **int** | The current version of the resource.  | 

## Example

```python
from sysdig_client.models.update_user_request_v1 import UpdateUserRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserRequestV1 from a JSON string
update_user_request_v1_instance = UpdateUserRequestV1.from_json(json)
# print the JSON string representation of the object
print(UpdateUserRequestV1.to_json())

# convert the object into a dict
update_user_request_v1_dict = update_user_request_v1_instance.to_dict()
# create an instance of UpdateUserRequestV1 from a dict
update_user_request_v1_from_dict = UpdateUserRequestV1.from_dict(update_user_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


