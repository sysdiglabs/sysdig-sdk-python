# MetadataResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Query status. | [optional] 
**data** | **Dict[str, List[MetadataResponseV1DataValueInner]]** | Metric metadata indexed by metric name. | [optional] 
**warnings** | **List[str]** | A set of warning messages attached to the response. | [optional] 
**infos** | **List[str]** | A set of information messages attached to the response. | [optional] 

## Example

```python
from sysdig_client.models.metadata_response_v1 import MetadataResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataResponseV1 from a JSON string
metadata_response_v1_instance = MetadataResponseV1.from_json(json)
# print the JSON string representation of the object
print(MetadataResponseV1.to_json())

# convert the object into a dict
metadata_response_v1_dict = metadata_response_v1_instance.to_dict()
# create an instance of MetadataResponseV1 from a dict
metadata_response_v1_from_dict = MetadataResponseV1.from_dict(metadata_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


