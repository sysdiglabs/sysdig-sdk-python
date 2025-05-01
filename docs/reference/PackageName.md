# PackageName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_type** | **str** | Matcher type to apply | [optional] 
**context_value** | **str** | Value to match | [optional] 

## Example

```python
from sysdig_client.models.package_name import PackageName

# TODO update the JSON string below
json = "{}"
# create an instance of PackageName from a JSON string
package_name_instance = PackageName.from_json(json)
# print the JSON string representation of the object
print(PackageName.to_json())

# convert the object into a dict
package_name_dict = package_name_instance.to_dict()
# create an instance of PackageName from a dict
package_name_from_dict = PackageName.from_dict(package_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


