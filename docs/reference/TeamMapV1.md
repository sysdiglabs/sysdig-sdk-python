# TeamMapV1

Determines the teams to which a group is mapped.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_for_all_teams** | **bool** | If true, the group is mapped to all teams.  | [optional] 
**team_ids** | **List[int]** | The list of teams to which group is mapped. It is empty when &#39;isForAllTeams&#39; is true, otherwise it should have at least 1 element.  | [optional] 

## Example

```python
from sysdig_client.models.team_map_v1 import TeamMapV1

# TODO update the JSON string below
json = "{}"
# create an instance of TeamMapV1 from a JSON string
team_map_v1_instance = TeamMapV1.from_json(json)
# print the JSON string representation of the object
print(TeamMapV1.to_json())

# convert the object into a dict
team_map_v1_dict = team_map_v1_instance.to_dict()
# create an instance of TeamMapV1 from a dict
team_map_v1_from_dict = TeamMapV1.from_dict(team_map_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


