# UpdateChronicleIntegrationConnInfoV2

Update Chronicle Integration Connection V2 Info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **str** | The target region | [optional] [default to 'us']
**chronicle_customer_id** | **str** | Unique identifier (UUID) corresponding to a particular Chronicle instance | 
**namespace** | **str** | User-configured environment namespace to identify the data domain the logs originated from | 
**credentials_o_auth2** | **str** | The Chronicle v2 OAuth2 credentials | [optional] 

## Example

```python
from sysdig_client.models.update_chronicle_integration_conn_info_v2 import UpdateChronicleIntegrationConnInfoV2

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateChronicleIntegrationConnInfoV2 from a JSON string
update_chronicle_integration_conn_info_v2_instance = UpdateChronicleIntegrationConnInfoV2.from_json(json)
# print the JSON string representation of the object
print(UpdateChronicleIntegrationConnInfoV2.to_json())

# convert the object into a dict
update_chronicle_integration_conn_info_v2_dict = update_chronicle_integration_conn_info_v2_instance.to_dict()
# create an instance of UpdateChronicleIntegrationConnInfoV2 from a dict
update_chronicle_integration_conn_info_v2_from_dict = UpdateChronicleIntegrationConnInfoV2.from_dict(update_chronicle_integration_conn_info_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


