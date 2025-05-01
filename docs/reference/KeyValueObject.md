# KeyValueObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key | 
**value** | **str** | The value | 

## Example

```python
from sysdig_client.models.key_value_object import KeyValueObject

# TODO update the JSON string below
json = "{}"
# create an instance of KeyValueObject from a JSON string
key_value_object_instance = KeyValueObject.from_json(json)
# print the JSON string representation of the object
print(KeyValueObject.to_json())

# convert the object into a dict
key_value_object_dict = key_value_object_instance.to_dict()
# create an instance of KeyValueObject from a dict
key_value_object_from_dict = KeyValueObject.from_dict(key_value_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


