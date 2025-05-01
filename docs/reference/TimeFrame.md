# TimeFrame

The start and end time of the request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **int** |   | [optional] 
**to** | **int** |   | [optional] 

## Example

```python
from sysdig_client.models.time_frame import TimeFrame

# TODO update the JSON string below
json = "{}"
# create an instance of TimeFrame from a JSON string
time_frame_instance = TimeFrame.from_json(json)
# print the JSON string representation of the object
print(TimeFrame.to_json())

# convert the object into a dict
time_frame_dict = time_frame_instance.to_dict()
# create an instance of TimeFrame from a dict
time_frame_from_dict = TimeFrame.from_dict(time_frame_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


