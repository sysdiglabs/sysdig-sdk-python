# PoliciesSummaryEntry

A Policy summary that indicates whether a policy failed or passed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Policy Id | 
**name** | **str** | Policy Name | 
**is_passed** | **bool** | True for passed, false for failed | 

## Example

```python
from sysdig_client.models.policies_summary_entry import PoliciesSummaryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of PoliciesSummaryEntry from a JSON string
policies_summary_entry_instance = PoliciesSummaryEntry.from_json(json)
# print the JSON string representation of the object
print(PoliciesSummaryEntry.to_json())

# convert the object into a dict
policies_summary_entry_dict = policies_summary_entry_instance.to_dict()
# create an instance of PoliciesSummaryEntry from a dict
policies_summary_entry_from_dict = PoliciesSummaryEntry.from_dict(policies_summary_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


