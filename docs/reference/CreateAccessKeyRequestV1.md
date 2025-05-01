# CreateAccessKeyRequestV1

Create access key request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_limit** | **int** | Maximum number of agents that can be connected with the access key | [optional] 
**agent_reservation** | **int** | Number of agents that are guaranteed to be available for the access key | [optional] 
**team_id** | **int** | ID of team that owns the access key | [optional] 
**metadata** | **Dict[str, str]** | Access key metadata (maximum of 20 key-value pairs where key can be up to 25 characters long and value can be up to 50 characters long) | [optional] 

## Example

```python
from sysdig_client.models.create_access_key_request_v1 import CreateAccessKeyRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccessKeyRequestV1 from a JSON string
create_access_key_request_v1_instance = CreateAccessKeyRequestV1.from_json(json)
# print the JSON string representation of the object
print(CreateAccessKeyRequestV1.to_json())

# convert the object into a dict
create_access_key_request_v1_dict = create_access_key_request_v1_instance.to_dict()
# create an instance of CreateAccessKeyRequestV1 from a dict
create_access_key_request_v1_from_dict = CreateAccessKeyRequestV1.from_dict(create_access_key_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


