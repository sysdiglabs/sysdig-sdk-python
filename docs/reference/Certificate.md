# Certificate

An X-509 certificate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The certificate ID. | 
**certificate_name** | **str** | The certificate Name. | 
**created** | **datetime** | The timestamp the certificate was created. | 
**issuer** | **str** | The Distinguished Name of the certificate issuer. | 
**validity** | [**CertificateValidity**](CertificateValidity.md) |  | 
**usage** | **int** | The number of services that currently use that certificate. | 
**fingerprint** | **str** | The certificate fingerprint | 

## Example

```python
from sysdig_client.models.certificate import Certificate

# TODO update the JSON string below
json = "{}"
# create an instance of Certificate from a JSON string
certificate_instance = Certificate.from_json(json)
# print the JSON string representation of the object
print(Certificate.to_json())

# convert the object into a dict
certificate_dict = certificate_instance.to_dict()
# create an instance of Certificate from a dict
certificate_from_dict = Certificate.from_dict(certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


