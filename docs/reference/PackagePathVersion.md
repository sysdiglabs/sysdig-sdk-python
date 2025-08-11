# PackagePathVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_type** | **str** | Matcher type to apply | [optional]
**context_value** | **str** | Value to match | [optional]

## Example

```python
from sysdig_client.models.package_path_version import PackagePathVersion

# TODO update the JSON string below
json = "{}"
# create an instance of PackagePathVersion from a JSON string
package_path_version_instance = PackagePathVersion.from_json(json)
# print the JSON string representation of the object
print(PackagePathVersion.to_json())

# convert the object into a dict
package_path_version_dict = package_path_version_instance.to_dict()
# create an instance of PackagePathVersion from a dict
package_path_version_from_dict = PackagePathVersion.from_dict(package_path_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


