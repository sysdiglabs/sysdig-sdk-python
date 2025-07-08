# WastedWorkloadSpendDataResponseGroupByDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **Dict[str, str]** | Key-value pairs representing grouping labels. | [optional] 
**accrued** | **float** | Accrued cost for this group. | [optional] 
**estimated** | **float** | Estimated cost for this group. | [optional] 
**wasted** | **float** | Wasted cost for this group. | [optional] 

## Example

```python
from sysdig_client.models.wasted_workload_spend_data_response_group_by_data_inner import WastedWorkloadSpendDataResponseGroupByDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of WastedWorkloadSpendDataResponseGroupByDataInner from a JSON string
wasted_workload_spend_data_response_group_by_data_inner_instance = WastedWorkloadSpendDataResponseGroupByDataInner.from_json(json)
# print the JSON string representation of the object
print(WastedWorkloadSpendDataResponseGroupByDataInner.to_json())

# convert the object into a dict
wasted_workload_spend_data_response_group_by_data_inner_dict = wasted_workload_spend_data_response_group_by_data_inner_instance.to_dict()
# create an instance of WastedWorkloadSpendDataResponseGroupByDataInner from a dict
wasted_workload_spend_data_response_group_by_data_inner_from_dict = WastedWorkloadSpendDataResponseGroupByDataInner.from_dict(wasted_workload_spend_data_response_group_by_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


