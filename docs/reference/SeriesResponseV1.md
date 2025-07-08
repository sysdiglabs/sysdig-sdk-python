# SeriesResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Query status. | [optional] 
**data** | **List[object]** | List of matching time series, each represented as a set of labels. | [optional] 
**warnings** | **List[str]** | A set of warning messages attached to the response. | [optional] 
**infos** | **List[str]** | A set of information messages attached to the response. | [optional] 

## Example

```python
from sysdig_client.models.series_response_v1 import SeriesResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesResponseV1 from a JSON string
series_response_v1_instance = SeriesResponseV1.from_json(json)
# print the JSON string representation of the object
print(SeriesResponseV1.to_json())

# convert the object into a dict
series_response_v1_dict = series_response_v1_instance.to_dict()
# create an instance of SeriesResponseV1 from a dict
series_response_v1_from_dict = SeriesResponseV1.from_dict(series_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


