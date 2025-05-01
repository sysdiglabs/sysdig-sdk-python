# PrivateConnectionInfoChronicle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | The Chronicle v1 API key | [optional] 

## Example

```python
from sysdig_client.models.private_connection_info_chronicle import PrivateConnectionInfoChronicle

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateConnectionInfoChronicle from a JSON string
private_connection_info_chronicle_instance = PrivateConnectionInfoChronicle.from_json(json)
# print the JSON string representation of the object
print(PrivateConnectionInfoChronicle.to_json())

# convert the object into a dict
private_connection_info_chronicle_dict = private_connection_info_chronicle_instance.to_dict()
# create an instance of PrivateConnectionInfoChronicle from a dict
private_connection_info_chronicle_from_dict = PrivateConnectionInfoChronicle.from_dict(private_connection_info_chronicle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


