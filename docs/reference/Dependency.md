# Dependency

Defines the direct dependencies of a component or service. Components or services that do not have their own dependencies MUST be declared as empty elements within the graph. Components or services that are not represented in the dependency graph MAY have unknown dependencies. It is RECOMMENDED that implementations assume this to be opaque and not an indicator of a object being dependency-free. It is RECOMMENDED to leverage compositions to indicate unknown dependency graphs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** | References a component or service by its bom-ref attribute | 
**depends_on** | **List[str]** | The bom-ref identifiers of the components or services that are dependencies of this dependency object. | [optional] 

## Example

```python
from sysdig_client.models.dependency import Dependency

# TODO update the JSON string below
json = "{}"
# create an instance of Dependency from a JSON string
dependency_instance = Dependency.from_json(json)
# print the JSON string representation of the object
print(Dependency.to_json())

# convert the object into a dict
dependency_dict = dependency_instance.to_dict()
# create an instance of Dependency from a dict
dependency_from_dict = Dependency.from_dict(dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


