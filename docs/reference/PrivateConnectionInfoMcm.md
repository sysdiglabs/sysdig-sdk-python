# PrivateConnectionInfoMcm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | IBM Cloud API Key | [optional] 

## Example

```python
from sysdig_client.models.private_connection_info_mcm import PrivateConnectionInfoMcm

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateConnectionInfoMcm from a JSON string
private_connection_info_mcm_instance = PrivateConnectionInfoMcm.from_json(json)
# print the JSON string representation of the object
print(PrivateConnectionInfoMcm.to_json())

# convert the object into a dict
private_connection_info_mcm_dict = private_connection_info_mcm_instance.to_dict()
# create an instance of PrivateConnectionInfoMcm from a dict
private_connection_info_mcm_from_dict = PrivateConnectionInfoMcm.from_dict(private_connection_info_mcm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


