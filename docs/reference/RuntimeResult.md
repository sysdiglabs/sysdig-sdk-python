# RuntimeResult

Runtime result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **object** | Scope labels that define the asset | [optional] 
**result_id** | **str** | Identifier of the scan result | [optional] 
**resource_id** | **str** | Identifier of the scanned resource: it will be the image ID for container images or the host ID for hosts. | [optional] 
**sbom_id** | **str** | Identifier of the sbom | [optional] 
**main_asset_name** | **str** | Name of the scanned asset | [optional] 
**running_vuln_total_by_severity** | [**VulnTotalBySeverity**](VulnTotalBySeverity.md) |  | [optional] 
**vuln_total_by_severity** | [**VulnTotalBySeverity**](VulnTotalBySeverity.md) |  | [optional] 
**policy_evaluation_result** | [**PolicyEvaluationResult**](PolicyEvaluationResult.md) |  | [optional] 
**is_risk_spotlight_enabled** | **bool** | Whether risk spotlight is enabled or not | [optional] 

## Example

```python
from sysdig_client.models.runtime_result import RuntimeResult

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeResult from a JSON string
runtime_result_instance = RuntimeResult.from_json(json)
# print the JSON string representation of the object
print(RuntimeResult.to_json())

# convert the object into a dict
runtime_result_dict = runtime_result_instance.to_dict()
# create an instance of RuntimeResult from a dict
runtime_result_from_dict = RuntimeResult.from_dict(runtime_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


