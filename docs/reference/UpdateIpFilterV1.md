# UpdateIpFilterV1

Request to update IP filter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_range** | **str** | IP range in CIDR notation | 
**note** | **str** |  | 
**is_enabled** | **bool** |  | 

## Example

```python
from sysdig_client.models.update_ip_filter_v1 import UpdateIpFilterV1

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIpFilterV1 from a JSON string
update_ip_filter_v1_instance = UpdateIpFilterV1.from_json(json)
# print the JSON string representation of the object
print(UpdateIpFilterV1.to_json())

# convert the object into a dict
update_ip_filter_v1_dict = update_ip_filter_v1_instance.to_dict()
# create an instance of UpdateIpFilterV1 from a dict
update_ip_filter_v1_from_dict = UpdateIpFilterV1.from_dict(update_ip_filter_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


