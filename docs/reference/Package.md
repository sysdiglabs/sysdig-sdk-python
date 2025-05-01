# Package


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | scan result package type, example values are:   - os   - rust   - java   - ruby   - javascript   - python   - php   - golang   - C# | 
**name** | **str** | name of the package | 
**is_running** | **bool** | whether the package is used by a running process | [optional] 
**is_removed** | **bool** | whether the package has been removed | [optional] 
**version** | **str** | version of the affected package | 
**license** | **str** | license of the package | [optional] 
**path** | **str** | path of the package | [optional] 
**suggested_fix** | **str** | suggested fix for the package | [optional] 
**layer_ref** | **str** | reference to layer | [optional] 
**vulnerabilities_refs** | **List[str]** | reference to vulnerabilities of the package | [optional] 

## Example

```python
from sysdig_client.models.package import Package

# TODO update the JSON string below
json = "{}"
# create an instance of Package from a JSON string
package_instance = Package.from_json(json)
# print the JSON string representation of the object
print(Package.to_json())

# convert the object into a dict
package_dict = package_instance.to_dict()
# create an instance of Package from a dict
package_from_dict = Package.from_dict(package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


