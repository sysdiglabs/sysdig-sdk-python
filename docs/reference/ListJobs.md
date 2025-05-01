# ListJobs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[JobResponse]**](JobResponse.md) | List of Jobs. | 

## Example

```python
from sysdig_client.models.list_jobs import ListJobs

# TODO update the JSON string below
json = "{}"
# create an instance of ListJobs from a JSON string
list_jobs_instance = ListJobs.from_json(json)
# print the JSON string representation of the object
print(ListJobs.to_json())

# convert the object into a dict
list_jobs_dict = list_jobs_instance.to_dict()
# create an instance of ListJobs from a dict
list_jobs_from_dict = ListJobs.from_dict(list_jobs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


