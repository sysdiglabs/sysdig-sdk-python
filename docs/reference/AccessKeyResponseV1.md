# AccessKeyResponseV1

Access key response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |   | [optional] 
**is_enabled** | **bool** | Indicates if the access key is enabled | [optional] 
**access_key** | **str** | Displays the access key value | [optional] 
**date_created** | **datetime** | Date and time when access key was created  | [optional] 
**date_disabled** | **datetime** | Date and time when access key was disabled  | [optional] 
**agent_limit** | **int** | Maximum number of agents that can be connected with the access key | [optional] 
**agent_reservation** | **int** | Number of agents that are guaranteed to be available for the access key | [optional] 
**team_id** | **int** | ID of team that owns the access key | [optional] 
**metadata** | **Dict[str, str]** | Access key metadata (maximum of 20 key-value pairs where key can be up to 25 characters long and value can be up to 50 characters long) | [optional] 

## Example

```python
from sysdig_client.models.access_key_response_v1 import AccessKeyResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of AccessKeyResponseV1 from a JSON string
access_key_response_v1_instance = AccessKeyResponseV1.from_json(json)
# print the JSON string representation of the object
print(AccessKeyResponseV1.to_json())

# convert the object into a dict
access_key_response_v1_dict = access_key_response_v1_instance.to_dict()
# create an instance of AccessKeyResponseV1 from a dict
access_key_response_v1_from_dict = AccessKeyResponseV1.from_dict(access_key_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


