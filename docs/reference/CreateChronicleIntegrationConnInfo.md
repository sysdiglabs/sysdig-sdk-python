# CreateChronicleIntegrationConnInfo

Create Chronicle Integration Connection Info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **str** | The target region | [optional] [default to 'us']
**api_key** | **str** | The Chronicle v1 API key | 

## Example

```python
from sysdig_client.models.create_chronicle_integration_conn_info import CreateChronicleIntegrationConnInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChronicleIntegrationConnInfo from a JSON string
create_chronicle_integration_conn_info_instance = CreateChronicleIntegrationConnInfo.from_json(json)
# print the JSON string representation of the object
print(CreateChronicleIntegrationConnInfo.to_json())

# convert the object into a dict
create_chronicle_integration_conn_info_dict = create_chronicle_integration_conn_info_instance.to_dict()
# create an instance of CreateChronicleIntegrationConnInfo from a dict
create_chronicle_integration_conn_info_from_dict = CreateChronicleIntegrationConnInfo.from_dict(create_chronicle_integration_conn_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


