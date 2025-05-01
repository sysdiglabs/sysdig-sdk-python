# BaseConnectionInfoChronicleV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **str** | The target region | [optional] [default to 'us']
**chronicle_customer_id** | **str** | Unique identifier (UUID) corresponding to a particular Chronicle instance | 
**namespace** | **str** | User-configured environment namespace to identify the data domain the logs originated from | 

## Example

```python
from sysdig_client.models.base_connection_info_chronicle_v2 import BaseConnectionInfoChronicleV2

# TODO update the JSON string below
json = "{}"
# create an instance of BaseConnectionInfoChronicleV2 from a JSON string
base_connection_info_chronicle_v2_instance = BaseConnectionInfoChronicleV2.from_json(json)
# print the JSON string representation of the object
print(BaseConnectionInfoChronicleV2.to_json())

# convert the object into a dict
base_connection_info_chronicle_v2_dict = base_connection_info_chronicle_v2_instance.to_dict()
# create an instance of BaseConnectionInfoChronicleV2 from a dict
base_connection_info_chronicle_v2_from_dict = BaseConnectionInfoChronicleV2.from_dict(base_connection_info_chronicle_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


