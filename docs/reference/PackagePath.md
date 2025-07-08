# PackagePath


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_type** | **str** | Matcher type to apply | [optional] 
**context_value** | **str** | Value to match | [optional] 

## Example

```python
from sysdig_client.models.package_path import PackagePath

# TODO update the JSON string below
json = "{}"
# create an instance of PackagePath from a JSON string
package_path_instance = PackagePath.from_json(json)
# print the JSON string representation of the object
print(PackagePath.to_json())

# convert the object into a dict
package_path_dict = package_path_instance.to_dict()
# create an instance of PackagePath from a dict
package_path_from_dict = PackagePath.from_dict(package_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


