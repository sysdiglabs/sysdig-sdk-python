# PrivateConnectionInfoGoogleScc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials_json** | **str** | JSON credentials for the service account Sysdig will use to send data | [optional] 

## Example

```python
from sysdig_client.models.private_connection_info_google_scc import PrivateConnectionInfoGoogleScc

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateConnectionInfoGoogleScc from a JSON string
private_connection_info_google_scc_instance = PrivateConnectionInfoGoogleScc.from_json(json)
# print the JSON string representation of the object
print(PrivateConnectionInfoGoogleScc.to_json())

# convert the object into a dict
private_connection_info_google_scc_dict = private_connection_info_google_scc_instance.to_dict()
# create an instance of PrivateConnectionInfoGoogleScc from a dict
private_connection_info_google_scc_from_dict = PrivateConnectionInfoGoogleScc.from_dict(private_connection_info_google_scc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


