# OpenIdRequestBaseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer_url** | **str** | The issuer URL of the OpenID Connect provider. | [optional] 
**client_id** | **str** | The client ID of the OpenID Connect provider. | [optional] 
**is_metadata_discovery_enabled** | **bool** | Flag to indicate if the metadata discovery is enabled. | [optional] 
**metadata** | [**OpenIdMetadataV1**](OpenIdMetadataV1.md) | The metadata of the OpenID Connect provider. | [optional] 
**group_attribute_name** | **str** | The group attribute name of the OpenID Connect provider. | [optional] 
**is_additional_scopes_check_enabled** | **bool** | Flag to indicate if the additional scopes verification on login. | [optional] 
**additional_scopes** | **List[str]** | List of additional scopes to be verified on login. | [optional] 
**client_secret** | **str** | The client secret of the OpenID Connect provider. | [optional] 

## Example

```python
from sysdig_client.models.open_id_request_base_v1 import OpenIdRequestBaseV1

# TODO update the JSON string below
json = "{}"
# create an instance of OpenIdRequestBaseV1 from a JSON string
open_id_request_base_v1_instance = OpenIdRequestBaseV1.from_json(json)
# print the JSON string representation of the object
print(OpenIdRequestBaseV1.to_json())

# convert the object into a dict
open_id_request_base_v1_dict = open_id_request_base_v1_instance.to_dict()
# create an instance of OpenIdRequestBaseV1 from a dict
open_id_request_base_v1_from_dict = OpenIdRequestBaseV1.from_dict(open_id_request_base_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


