# GetChronicleIntegrationResponseAllOfConnectionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **str** | The target region | [optional] [default to 'us']
**chronicle_customer_id** | **str** | Unique identifier (UUID) corresponding to a particular Chronicle instance | 
**namespace** | **str** | User-configured environment namespace to identify the data domain the logs originated from | 

## Example

```python
from sysdig_client.models.get_chronicle_integration_response_all_of_connection_info import GetChronicleIntegrationResponseAllOfConnectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GetChronicleIntegrationResponseAllOfConnectionInfo from a JSON string
get_chronicle_integration_response_all_of_connection_info_instance = GetChronicleIntegrationResponseAllOfConnectionInfo.from_json(json)
# print the JSON string representation of the object
print(GetChronicleIntegrationResponseAllOfConnectionInfo.to_json())

# convert the object into a dict
get_chronicle_integration_response_all_of_connection_info_dict = get_chronicle_integration_response_all_of_connection_info_instance.to_dict()
# create an instance of GetChronicleIntegrationResponseAllOfConnectionInfo from a dict
get_chronicle_integration_response_all_of_connection_info_from_dict = GetChronicleIntegrationResponseAllOfConnectionInfo.from_dict(get_chronicle_integration_response_all_of_connection_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


