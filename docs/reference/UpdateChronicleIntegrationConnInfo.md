# UpdateChronicleIntegrationConnInfo

Update Chronicle Integration Connection Info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **str** | The target region | [optional] [default to 'us']
**api_key** | **str** | The Chronicle v1 API key | [optional] 

## Example

```python
from sysdig_client.models.update_chronicle_integration_conn_info import UpdateChronicleIntegrationConnInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateChronicleIntegrationConnInfo from a JSON string
update_chronicle_integration_conn_info_instance = UpdateChronicleIntegrationConnInfo.from_json(json)
# print the JSON string representation of the object
print(UpdateChronicleIntegrationConnInfo.to_json())

# convert the object into a dict
update_chronicle_integration_conn_info_dict = update_chronicle_integration_conn_info_instance.to_dict()
# create an instance of UpdateChronicleIntegrationConnInfo from a dict
update_chronicle_integration_conn_info_from_dict = UpdateChronicleIntegrationConnInfo.from_dict(update_chronicle_integration_conn_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


