# ImageConfigFailure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | image configuration failure description | [optional] 
**remediation** | **str** | image configuration failure remediation | 
**arguments** | **object** |  | 
**package_ref** | **str** | reference to the affected package | [optional] 
**vulnerability_ref** | **str** | reference to the vulnerability | [optional] 
**risk_accept_refs** | **List[str]** | list of accepted risks for the failure | [optional] 

## Example

```python
from sysdig_client.models.image_config_failure import ImageConfigFailure

# TODO update the JSON string below
json = "{}"
# create an instance of ImageConfigFailure from a JSON string
image_config_failure_instance = ImageConfigFailure.from_json(json)
# print the JSON string representation of the object
print(ImageConfigFailure.to_json())

# convert the object into a dict
image_config_failure_dict = image_config_failure_instance.to_dict()
# create an instance of ImageConfigFailure from a dict
image_config_failure_from_dict = ImageConfigFailure.from_dict(image_config_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


