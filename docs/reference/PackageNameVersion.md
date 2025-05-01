# PackageNameVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_type** | **str** | Matcher type to apply | [optional] 
**context_value** | **str** | Value to match | [optional] 

## Example

```python
from sysdig_client.models.package_name_version import PackageNameVersion

# TODO update the JSON string below
json = "{}"
# create an instance of PackageNameVersion from a JSON string
package_name_version_instance = PackageNameVersion.from_json(json)
# print the JSON string representation of the object
print(PackageNameVersion.to_json())

# convert the object into a dict
package_name_version_dict = package_name_version_instance.to_dict()
# create an instance of PackageNameVersion from a dict
package_name_version_from_dict = PackageNameVersion.from_dict(package_name_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


