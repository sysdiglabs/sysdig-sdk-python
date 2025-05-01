# VulnAgeExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | **int** | The age of the vulnerability in days. | [optional] 

## Example

```python
from sysdig_client.models.vuln_age_extra import VulnAgeExtra

# TODO update the JSON string below
json = "{}"
# create an instance of VulnAgeExtra from a JSON string
vuln_age_extra_instance = VulnAgeExtra.from_json(json)
# print the JSON string representation of the object
print(VulnAgeExtra.to_json())

# convert the object into a dict
vuln_age_extra_dict = vuln_age_extra_instance.to_dict()
# create an instance of VulnAgeExtra from a dict
vuln_age_extra_from_dict = VulnAgeExtra.from_dict(vuln_age_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


