# SequenceInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | The unique identifier of the log event. | 
**event_name** | **str** | The name of the event. | 
**event_time** | **datetime** | The time when the event occurred. | 
**ingestion_id** | **str** | The unique identifier of the ingestion. | 
**region** | **str** | The region where the event occurred. | 
**source** | **str** | The source of the event. | 
**source_ip_address** | **str** | The IP address of the source. | 
**sub_ingestion_id** | **str** | The unique identifier of the sub ingestion. | 

## Example

```python
from sysdig_client.models.sequence_inner import SequenceInner

# TODO update the JSON string below
json = "{}"
# create an instance of SequenceInner from a JSON string
sequence_inner_instance = SequenceInner.from_json(json)
# print the JSON string representation of the object
print(SequenceInner.to_json())

# convert the object into a dict
sequence_inner_dict = sequence_inner_instance.to_dict()
# create an instance of SequenceInner from a dict
sequence_inner_from_dict = SequenceInner.from_dict(sequence_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


