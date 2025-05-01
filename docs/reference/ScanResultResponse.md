# ScanResultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_type** | **str** | scan result asset type | 
**stage** | **str** | scan result stage | 
**metadata** | [**ScanResultResponseMetadata**](ScanResultResponseMetadata.md) |  | 
**packages** | [**Dict[str, Package]**](Package.md) |  | 
**vulnerabilities** | [**Dict[str, Vulnerability]**](Vulnerability.md) |  | [optional] 
**layers** | [**Dict[str, Layer]**](Layer.md) |  | [optional] 
**base_images** | [**Dict[str, BaseImage]**](BaseImage.md) |  | [optional] 
**policies** | [**Policies**](Policies.md) |  | [optional] 
**risk_accepts** | [**Dict[str, RiskAcceptanceDefinition]**](RiskAcceptanceDefinition.md) |  | [optional] 
**producer** | [**Producer**](Producer.md) |  | [optional] 

## Example

```python
from sysdig_client.models.scan_result_response import ScanResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScanResultResponse from a JSON string
scan_result_response_instance = ScanResultResponse.from_json(json)
# print the JSON string representation of the object
print(ScanResultResponse.to_json())

# convert the object into a dict
scan_result_response_dict = scan_result_response_instance.to_dict()
# create an instance of ScanResultResponse from a dict
scan_result_response_from_dict = ScanResultResponse.from_dict(scan_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


