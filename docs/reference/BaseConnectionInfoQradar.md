# BaseConnectionInfoQradar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | DNS name or IP of the QRadar instance | 
**port** | **int** | QRadar Management Port | 
**is_insecure** | **bool** | Don&#39;t verify TLS certificate | [optional] 
**is_tls** | **bool** | Use TLS encryption | [optional] [default to False]

## Example

```python
from sysdig_client.models.base_connection_info_qradar import BaseConnectionInfoQradar

# TODO update the JSON string below
json = "{}"
# create an instance of BaseConnectionInfoQradar from a JSON string
base_connection_info_qradar_instance = BaseConnectionInfoQradar.from_json(json)
# print the JSON string representation of the object
print(BaseConnectionInfoQradar.to_json())

# convert the object into a dict
base_connection_info_qradar_dict = base_connection_info_qradar_instance.to_dict()
# create an instance of BaseConnectionInfoQradar from a dict
base_connection_info_qradar_from_dict = BaseConnectionInfoQradar.from_dict(base_connection_info_qradar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


