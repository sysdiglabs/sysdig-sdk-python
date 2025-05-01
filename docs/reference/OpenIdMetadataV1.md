# OpenIdMetadataV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer** | **str** | The base issuer URL of the OpenID Connect provider. | [optional] 
**authorization_endpoint** | **str** | The authorization endpoint of the OpenID Connect provider. | 
**token_endpoint** | **str** | The token endpoint of the OpenID Connect provider. | 
**jwks_uri** | **str** | The JSON Web Key Set URI of the OpenID Connect provider. | [optional] 
**end_session_endpoint** | **str** | Single sign-out endpoint of the OpenID Connect provider. | [optional] 
**user_info_endpoint** | **str** | The user info endpoint of the OpenID Connect provider. | [optional] 
**token_auth_method** | **str** | The token authentication method of the OpenID Connect provider. | 

## Example

```python
from sysdig_client.models.open_id_metadata_v1 import OpenIdMetadataV1

# TODO update the JSON string below
json = "{}"
# create an instance of OpenIdMetadataV1 from a JSON string
open_id_metadata_v1_instance = OpenIdMetadataV1.from_json(json)
# print the JSON string representation of the object
print(OpenIdMetadataV1.to_json())

# convert the object into a dict
open_id_metadata_v1_dict = open_id_metadata_v1_instance.to_dict()
# create an instance of OpenIdMetadataV1 from a dict
open_id_metadata_v1_from_dict = OpenIdMetadataV1.from_dict(open_id_metadata_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


