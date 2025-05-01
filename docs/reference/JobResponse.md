# JobResponse

Schema for a job response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the job. | 
**user_id** | **int** | ID of the user who created the job. | 
**team_id** | **int** | ID of the team the job was created under. | 
**customer_id** | **int** | ID of the user associated with the job. | 
**iac_task_id** | **int** | ID of the IAC scheduled task. | [optional] 
**schedule_id** | **str** | ID of the schedule associated with the job | [optional] 
**report_id** | **int** | ID of the report | 
**is_report_template** | **bool** | Indicates if the report is a template | 
**report_format** | **str** | Format of the report | 
**job_type** | **str** | Type of the job | 
**job_name** | **str** | Name of the job | [optional] 
**zones** | **List[int]** | List of zone IDs | 
**policies** | **List[int]** | List of policy IDs | [optional] 
**status** | **str** | Status of the job | 
**timezone** | **str** | Timezone of the request time frame | [optional] 
**time_frame** | [**TimeFrame**](TimeFrame.md) |  | [optional] 
**file_name** | **str** | File name of the report | [optional] 
**file_path** | **str** | File path of the report | [optional] 
**created_by** | **str** | Email of the user who created the job | 
**scheduled_on** | **datetime** | Timestamp when the job was scheduled | 
**started_on** | **datetime** | Timestamp when the job was started | [optional] 
**completed_on** | **datetime** | Timestamp when the job was completed | [optional] 

## Example

```python
from sysdig_client.models.job_response import JobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JobResponse from a JSON string
job_response_instance = JobResponse.from_json(json)
# print the JSON string representation of the object
print(JobResponse.to_json())

# convert the object into a dict
job_response_dict = job_response_instance.to_dict()
# create an instance of JobResponse from a dict
job_response_from_dict = JobResponse.from_dict(job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


