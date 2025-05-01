# AdditionalTeamPermissionsV1

Additional permissions available to the users of the team.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_sysdig_captures** | **bool** | Enable the Sysdig captures feature for this team. | [optional] [default to False]
**has_infrastructure_events** | **bool** |  | [optional] [default to False]
**has_aws_data** | **bool** |  | [optional] [default to False]
**has_rapid_response** | **bool** |  | [optional] [default to False]
**has_agent_cli** | **bool** |  | [optional] [default to False]
**has_beacon_metrics** | **bool** |  | [optional] [default to False]

## Example

```python
from sysdig_client.models.additional_team_permissions_v1 import AdditionalTeamPermissionsV1

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalTeamPermissionsV1 from a JSON string
additional_team_permissions_v1_instance = AdditionalTeamPermissionsV1.from_json(json)
# print the JSON string representation of the object
print(AdditionalTeamPermissionsV1.to_json())

# convert the object into a dict
additional_team_permissions_v1_dict = additional_team_permissions_v1_instance.to_dict()
# create an instance of AdditionalTeamPermissionsV1 from a dict
additional_team_permissions_v1_from_dict = AdditionalTeamPermissionsV1.from_dict(additional_team_permissions_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


