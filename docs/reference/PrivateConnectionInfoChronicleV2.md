# PrivateConnectionInfoChronicleV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials_o_auth2** | **str** | The Chronicle v2 OAuth2 credentials | [optional] 

## Example

```python
from sysdig_client.models.private_connection_info_chronicle_v2 import PrivateConnectionInfoChronicleV2

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateConnectionInfoChronicleV2 from a JSON string
private_connection_info_chronicle_v2_instance = PrivateConnectionInfoChronicleV2.from_json(json)
# print the JSON string representation of the object
print(PrivateConnectionInfoChronicleV2.to_json())

# convert the object into a dict
private_connection_info_chronicle_v2_dict = private_connection_info_chronicle_v2_instance.to_dict()
# create an instance of PrivateConnectionInfoChronicleV2 from a dict
private_connection_info_chronicle_v2_from_dict = PrivateConnectionInfoChronicleV2.from_dict(private_connection_info_chronicle_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


