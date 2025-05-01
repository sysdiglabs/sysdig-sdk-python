# SamlUpdateRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_url** | **str** | The metadata URL of the SAML provider. **Mutually exclusive with metadata* | [optional] 
**metadata_xml** | **str** | The metadata XML of the SAML provider. **Mutually exclusive with metadataUrl* | [optional] 
**email_parameter** | **str** | The email parameter of the SAML provider. | 
**is_signature_validation_enabled** | **bool** | Flag that indicates if the signature validation is enabled. | 
**is_signed_assertion_enabled** | **bool** | Flag that indicates if the signed assertion is enabled. | 
**is_destination_verification_enabled** | **bool** | Flag that indicates if the destination verification is enabled. | 
**is_encryption_support_enabled** | **bool** | Flag that indicates if the encryption support is enabled. | 

## Example

```python
from sysdig_client.models.saml_update_request_v1 import SamlUpdateRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of SamlUpdateRequestV1 from a JSON string
saml_update_request_v1_instance = SamlUpdateRequestV1.from_json(json)
# print the JSON string representation of the object
print(SamlUpdateRequestV1.to_json())

# convert the object into a dict
saml_update_request_v1_dict = saml_update_request_v1_instance.to_dict()
# create an instance of SamlUpdateRequestV1 from a dict
saml_update_request_v1_from_dict = SamlUpdateRequestV1.from_dict(saml_update_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


