# SbomResultResponse

SBOM of the requested asset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bom_format** | **str** | Specifies the format of the BOM. This helps to identify the file as CycloneDX since BOMs do not have a filename convention nor does JSON schema support namespaces. This value MUST be \&quot;CycloneDX\&quot;. | 
**spec_version** | **str** | The version of the CycloneDX specification a BOM conforms to (starting at version 1.2). | 
**serial_number** | **str** | Every BOM generated SHOULD have a unique serial number, even if the contents of the BOM have not changed over time. If specified, the serial number MUST conform to RFC-4122. Use of serial numbers are RECOMMENDED. | [optional] 
**version** | **int** | Whenever an existing BOM is modified, either manually or through automated processes, the version of the BOM SHOULD be incremented by 1. When a system is presented with multiple BOMs with identical serial numbers, the system SHOULD use the most recent version of the BOM. The default version is &#39;1&#39;. | [optional] [default to 1]
**metadata** | [**BOMMetadata**](BOMMetadata.md) |  | [optional] 
**components** | [**List[SbomComponent]**](SbomComponent.md) | A list of software and hardware components. | [optional] 
**dependencies** | [**List[Dependency]**](Dependency.md) | Provides the ability to document dependency relationships. | [optional] 
**compositions** | [**List[CompositionsInner]**](CompositionsInner.md) | Compositions describe constituent parts (including components, services, and dependency relationships) and their completeness. The completeness of vulnerabilities expressed in a BOM may also be described. | [optional] 

## Example

```python
from sysdig_client.models.sbom_result_response import SbomResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SbomResultResponse from a JSON string
sbom_result_response_instance = SbomResultResponse.from_json(json)
# print the JSON string representation of the object
print(SbomResultResponse.to_json())

# convert the object into a dict
sbom_result_response_dict = sbom_result_response_instance.to_dict()
# create an instance of SbomResultResponse from a dict
sbom_result_response_from_dict = SbomResultResponse.from_dict(sbom_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


