# Predicate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | predicate type | [optional] 
**extra** | **object** |  | [optional] 

## Example

```python
from sysdig_client.models.predicate import Predicate

# TODO update the JSON string below
json = "{}"
# create an instance of Predicate from a JSON string
predicate_instance = Predicate.from_json(json)
# print the JSON string representation of the object
print(Predicate.to_json())

# convert the object into a dict
predicate_dict = predicate_instance.to_dict()
# create an instance of Predicate from a dict
predicate_from_dict = Predicate.from_dict(predicate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


