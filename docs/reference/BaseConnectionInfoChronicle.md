# BaseConnectionInfoChronicle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **str** | The target region | [optional] [default to 'us']

## Example

```python
from sysdig_client.models.base_connection_info_chronicle import BaseConnectionInfoChronicle

# TODO update the JSON string below
json = "{}"
# create an instance of BaseConnectionInfoChronicle from a JSON string
base_connection_info_chronicle_instance = BaseConnectionInfoChronicle.from_json(json)
# print the JSON string representation of the object
print(BaseConnectionInfoChronicle.to_json())

# convert the object into a dict
base_connection_info_chronicle_dict = base_connection_info_chronicle_instance.to_dict()
# create an instance of BaseConnectionInfoChronicle from a dict
base_connection_info_chronicle_from_dict = BaseConnectionInfoChronicle.from_dict(base_connection_info_chronicle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


