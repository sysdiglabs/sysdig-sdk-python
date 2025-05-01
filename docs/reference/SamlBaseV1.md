# SamlBaseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_url** | **str** | The metadata URL of the SAML provider. **Mutually exclusive with metadata* | [optional] 
**metadata_xml** | **str** | The metadata XML of the SAML provider. **Mutually exclusive with metadataUrl* | [optional] 
**email_parameter** | **str** | The email parameter of the SAML provider. | [optional] 
**is_signature_validation_enabled** | **bool** | Flag that indicates if the signature validation is enabled. | [optional] 
**is_signed_assertion_enabled** | **bool** | Flag that indicates if the signed assertion is enabled. | [optional] 
**is_destination_verification_enabled** | **bool** | Flag that indicates if the destination verification is enabled. | [optional] 
**is_encryption_support_enabled** | **bool** | Flag that indicates if the encryption support is enabled. | [optional] 

## Example

```python
from sysdig_client.models.saml_base_v1 import SamlBaseV1

# TODO update the JSON string below
json = "{}"
# create an instance of SamlBaseV1 from a JSON string
saml_base_v1_instance = SamlBaseV1.from_json(json)
# print the JSON string representation of the object
print(SamlBaseV1.to_json())

# convert the object into a dict
saml_base_v1_dict = saml_base_v1_instance.to_dict()
# create an instance of SamlBaseV1 from a dict
saml_base_v1_from_dict = SamlBaseV1.from_dict(saml_base_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


