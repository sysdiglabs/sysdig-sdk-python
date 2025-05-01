# PkgVulnFailure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | description of the failure | 
**package_ref** | **str** | reference to the affected package | [optional] 
**vulnerability_ref** | **str** | reference to the vulnerability | [optional] 
**risk_accept_refs** | **List[str]** | list of accepted risks for the failure | [optional] 

## Example

```python
from sysdig_client.models.pkg_vuln_failure import PkgVulnFailure

# TODO update the JSON string below
json = "{}"
# create an instance of PkgVulnFailure from a JSON string
pkg_vuln_failure_instance = PkgVulnFailure.from_json(json)
# print the JSON string representation of the object
print(PkgVulnFailure.to_json())

# convert the object into a dict
pkg_vuln_failure_dict = pkg_vuln_failure_instance.to_dict()
# create an instance of PkgVulnFailure from a dict
pkg_vuln_failure_from_dict = PkgVulnFailure.from_dict(pkg_vuln_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


