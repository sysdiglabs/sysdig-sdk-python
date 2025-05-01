# CreateTeamServiceAccountRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The display name of the Service Account. | 
**expiration_date** | **int** | Time when the Service Account API key expires, | in number of milliseconds since January 1, 1970, 00:00:00 GMT | [optional] 
**team_role** | **str** | Team role to be assigned to the team service account. | It can be a string for predefined roles or an id of a custom role. | 

## Example

```python
from sysdig_client.models.create_team_service_account_request_v1 import CreateTeamServiceAccountRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTeamServiceAccountRequestV1 from a JSON string
create_team_service_account_request_v1_instance = CreateTeamServiceAccountRequestV1.from_json(json)
# print the JSON string representation of the object
print(CreateTeamServiceAccountRequestV1.to_json())

# convert the object into a dict
create_team_service_account_request_v1_dict = create_team_service_account_request_v1_instance.to_dict()
# create an instance of CreateTeamServiceAccountRequestV1 from a dict
create_team_service_account_request_v1_from_dict = CreateTeamServiceAccountRequestV1.from_dict(create_team_service_account_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


