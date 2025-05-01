# ListSchedules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ScheduleResponse]**](ScheduleResponse.md) | List of Schedules. | 

## Example

```python
from sysdig_client.models.list_schedules import ListSchedules

# TODO update the JSON string below
json = "{}"
# create an instance of ListSchedules from a JSON string
list_schedules_instance = ListSchedules.from_json(json)
# print the JSON string representation of the object
print(ListSchedules.to_json())

# convert the object into a dict
list_schedules_dict = list_schedules_instance.to_dict()
# create an instance of ListSchedules from a dict
list_schedules_from_dict = ListSchedules.from_dict(list_schedules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


