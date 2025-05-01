# UpdateAccessKeyRequestV1

Update access key request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_limit** | **int** | Maximum number of agents that can be connected with the access key | [optional] 
**agent_reservation** | **int** | Number of agents that are guaranteed to be available for the access key | [optional] 
**team_id** | **int** | ID of team that owns the access key | [optional] 
**is_enabled** | **bool** | Flag that indicates if the access key should be disabled or enabled | 
**metadata** | **Dict[str, str]** | Access key metadata (maximum of 20 key-value pairs where key can be up to 25 characters long and value can be up to 50 characters long) | [optional] 

## Example

```python
from sysdig_client.models.update_access_key_request_v1 import UpdateAccessKeyRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAccessKeyRequestV1 from a JSON string
update_access_key_request_v1_instance = UpdateAccessKeyRequestV1.from_json(json)
# print the JSON string representation of the object
print(UpdateAccessKeyRequestV1.to_json())

# convert the object into a dict
update_access_key_request_v1_dict = update_access_key_request_v1_instance.to_dict()
# create an instance of UpdateAccessKeyRequestV1 from a dict
update_access_key_request_v1_from_dict = UpdateAccessKeyRequestV1.from_dict(update_access_key_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


