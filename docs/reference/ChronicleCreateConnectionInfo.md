# ChronicleCreateConnectionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **str** | The target region | [optional] [default to 'us']
**chronicle_customer_id** | **str** | Unique identifier (UUID) corresponding to a particular Chronicle instance | 
**namespace** | **str** | User-configured environment namespace to identify the data domain the logs originated from | 
**credentials_o_auth2** | **str** | The Chronicle v2 OAuth2 credentials | 
**api_key** | **str** | The Chronicle v1 API key | 

## Example

```python
from sysdig_client.models.chronicle_create_connection_info import ChronicleCreateConnectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ChronicleCreateConnectionInfo from a JSON string
chronicle_create_connection_info_instance = ChronicleCreateConnectionInfo.from_json(json)
# print the JSON string representation of the object
print(ChronicleCreateConnectionInfo.to_json())

# convert the object into a dict
chronicle_create_connection_info_dict = chronicle_create_connection_info_instance.to_dict()
# create an instance of ChronicleCreateConnectionInfo from a dict
chronicle_create_connection_info_from_dict = ChronicleCreateConnectionInfo.from_dict(chronicle_create_connection_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


