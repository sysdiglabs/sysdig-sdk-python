# ScheduleResponse

Schema for a scheduled report

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the schedule | 
**user_id** | **int** | ID of the user who created the schedule | 
**team_id** | **int** | ID of the team associated with the schedule | 
**customer_id** | **int** | ID of the customer associated with the schedule | 
**name** | **str** | Name of the schedule | [optional] 
**description** | **str** | Description of the schedule | [optional] 
**report_id** | **int** | ID of the report | 
**report_name** | **str** | Name of the report | [optional] 
**is_report_template** | **bool** | Indicates if the report is a template | 
**report_format** | **str** | Format of the report | 
**zones** | **List[int]** | List of zone IDs | 
**policies** | **List[int]** | List of policy IDs | [optional] 
**timezone** | **str** | Timezone for the schedule | [optional] 
**schedule** | **str** | Cron expression for the schedule | 
**enabled** | **bool** | Indicates if the schedule is enabled | 
**notification_channels** | [**List[NotificationChannel]**](NotificationChannel.md) | List of notification channels | [optional] 
**iac_task_id** | **int** | ID of the IaC task | [optional] 
**password_enabled** | **bool** | Indicates if password protection is enabled | [optional] 
**compression** | **str** | Compression format | [optional] 
**created_by** | **str** | Email of the user who created the schedule | 
**updated_by** | **str** | Email of the user who last updated the schedule | [optional] 
**created_on** | **datetime** | Timestamp when the schedule was created | 
**modified_on** | **datetime** | Timestamp when the schedule was last modified | [optional] 
**last_scheduled_on** | **datetime** | Timestamp when the schedule was last run | [optional] 
**last_started_on** | **datetime** | Timestamp when the schedule was last started | [optional] 
**last_completed_on** | **datetime** | Timestamp when the schedule was last completed | [optional] 

## Example

```python
from sysdig_client.models.schedule_response import ScheduleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleResponse from a JSON string
schedule_response_instance = ScheduleResponse.from_json(json)
# print the JSON string representation of the object
print(ScheduleResponse.to_json())

# convert the object into a dict
schedule_response_dict = schedule_response_instance.to_dict()
# create an instance of ScheduleResponse from a dict
schedule_response_from_dict = ScheduleResponse.from_dict(schedule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


