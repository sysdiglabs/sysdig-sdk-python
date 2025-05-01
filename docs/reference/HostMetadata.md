# HostMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **str** | host architecture | [optional] 
**host_id** | **str** | host id | 
**host_name** | **str** | host name | 
**os** | **str** | host os | 

## Example

```python
from sysdig_client.models.host_metadata import HostMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of HostMetadata from a JSON string
host_metadata_instance = HostMetadata.from_json(json)
# print the JSON string representation of the object
print(HostMetadata.to_json())

# convert the object into a dict
host_metadata_dict = host_metadata_instance.to_dict()
# create an instance of HostMetadata from a dict
host_metadata_from_dict = HostMetadata.from_dict(host_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


