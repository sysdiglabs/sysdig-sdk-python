# CreateChronicleIntegrationConnInfoV2

Create Chronicle Integration Connection V2 Info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **str** | The target region | [optional] [default to 'us']
**chronicle_customer_id** | **str** | Unique identifier (UUID) corresponding to a particular Chronicle instance | 
**namespace** | **str** | User-configured environment namespace to identify the data domain the logs originated from | 
**credentials_o_auth2** | **str** | The Chronicle v2 OAuth2 credentials | 

## Example

```python
from sysdig_client.models.create_chronicle_integration_conn_info_v2 import CreateChronicleIntegrationConnInfoV2

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChronicleIntegrationConnInfoV2 from a JSON string
create_chronicle_integration_conn_info_v2_instance = CreateChronicleIntegrationConnInfoV2.from_json(json)
# print the JSON string representation of the object
print(CreateChronicleIntegrationConnInfoV2.to_json())

# convert the object into a dict
create_chronicle_integration_conn_info_v2_dict = create_chronicle_integration_conn_info_v2_instance.to_dict()
# create an instance of CreateChronicleIntegrationConnInfoV2 from a dict
create_chronicle_integration_conn_info_v2_from_dict = CreateChronicleIntegrationConnInfoV2.from_dict(create_chronicle_integration_conn_info_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


