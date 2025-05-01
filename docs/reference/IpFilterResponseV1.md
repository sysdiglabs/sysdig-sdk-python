# IpFilterResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |   | [optional] 
**ip_range** | **str** | IP range in CIDR notation | [optional] 
**note** | **str** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**is_allowed** | **bool** | Whether the IP range is allowed or not. | [optional] 
**last_updated** | **datetime** | The date when IP filter was last updated. | [optional] 

## Example

```python
from sysdig_client.models.ip_filter_response_v1 import IpFilterResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of IpFilterResponseV1 from a JSON string
ip_filter_response_v1_instance = IpFilterResponseV1.from_json(json)
# print the JSON string representation of the object
print(IpFilterResponseV1.to_json())

# convert the object into a dict
ip_filter_response_v1_dict = ip_filter_response_v1_instance.to_dict()
# create an instance of IpFilterResponseV1 from a dict
ip_filter_response_v1_from_dict = IpFilterResponseV1.from_dict(ip_filter_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


