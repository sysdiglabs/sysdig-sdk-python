# PosturePolicySummary

The posture policy summary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pass_percentage** | **int** | Percentage of policies passing | 
**policies** | [**List[PoliciesSummaryEntry]**](PoliciesSummaryEntry.md) | The policies list | 

## Example

```python
from sysdig_client.models.posture_policy_summary import PosturePolicySummary

# TODO update the JSON string below
json = "{}"
# create an instance of PosturePolicySummary from a JSON string
posture_policy_summary_instance = PosturePolicySummary.from_json(json)
# print the JSON string representation of the object
print(PosturePolicySummary.to_json())

# convert the object into a dict
posture_policy_summary_dict = posture_policy_summary_instance.to_dict()
# create an instance of PosturePolicySummary from a dict
posture_policy_summary_from_dict = PosturePolicySummary.from_dict(posture_policy_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


