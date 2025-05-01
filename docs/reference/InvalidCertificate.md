# InvalidCertificate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**message** | **str** |  | 
**details** | **List[object]** |  | [optional] 

## Example

```python
from sysdig_client.models.invalid_certificate import InvalidCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidCertificate from a JSON string
invalid_certificate_instance = InvalidCertificate.from_json(json)
# print the JSON string representation of the object
print(InvalidCertificate.to_json())

# convert the object into a dict
invalid_certificate_dict = invalid_certificate_instance.to_dict()
# create an instance of InvalidCertificate from a dict
invalid_certificate_from_dict = InvalidCertificate.from_dict(invalid_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


