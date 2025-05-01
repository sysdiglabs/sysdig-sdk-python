# NewStage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | stage name. | 
**configuration** | [**List[StageConfiguration]**](StageConfiguration.md) | Configurations for the stage | [optional] 

## Example

```python
from sysdig_client.models.new_stage import NewStage

# TODO update the JSON string below
json = "{}"
# create an instance of NewStage from a JSON string
new_stage_instance = NewStage.from_json(json)
# print the JSON string representation of the object
print(NewStage.to_json())

# convert the object into a dict
new_stage_dict = new_stage_instance.to_dict()
# create an instance of NewStage from a dict
new_stage_from_dict = NewStage.from_dict(new_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


