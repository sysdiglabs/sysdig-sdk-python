# CreateIpFilterV1

Request to create IP filter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_range** | **str** | IP range in CIDR notation | 
**note** | **str** |  | [optional] 
**is_enabled** | **bool** |  | 

## Example

```python
from sysdig_client.models.create_ip_filter_v1 import CreateIpFilterV1

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIpFilterV1 from a JSON string
create_ip_filter_v1_instance = CreateIpFilterV1.from_json(json)
# print the JSON string representation of the object
print(CreateIpFilterV1.to_json())

# convert the object into a dict
create_ip_filter_v1_dict = create_ip_filter_v1_instance.to_dict()
# create an instance of CreateIpFilterV1 from a dict
create_ip_filter_v1_from_dict = CreateIpFilterV1.from_dict(create_ip_filter_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


