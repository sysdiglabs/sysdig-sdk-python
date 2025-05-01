# CertificateValidity

The certificate validity interval.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after** | **datetime** | The beginning of the certificate validity period. | [optional] 
**before** | **datetime** | The end of the certificate validity period. | [optional] 

## Example

```python
from sysdig_client.models.certificate_validity import CertificateValidity

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateValidity from a JSON string
certificate_validity_instance = CertificateValidity.from_json(json)
# print the JSON string representation of the object
print(CertificateValidity.to_json())

# convert the object into a dict
certificate_validity_dict = certificate_validity_instance.to_dict()
# create an instance of CertificateValidity from a dict
certificate_validity_from_dict = CertificateValidity.from_dict(certificate_validity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


