# CompositionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregate** | **str** | Specifies an aggregate type that describe how complete a relationship is.  * __complete__ &#x3D; The relationship is complete. No further relationships including constituent components, services, or dependencies are known to exist. * __incomplete__ &#x3D; The relationship is incomplete. Additional relationships exist and may include constituent components, services, or dependencies. * __incomplete&amp;#95;first&amp;#95;party&amp;#95;only__ &#x3D; The relationship is incomplete. Only relationships for first-party components, services, or their dependencies are represented. * __incomplete&amp;#95;first&amp;#95;party&amp;#95;proprietary&amp;#95;only__ &#x3D; The relationship is incomplete. Only relationships for first-party components, services, or their dependencies are represented, limited specifically to those that are proprietary. * __incomplete&amp;#95;first&amp;#95;party&amp;#95;opensource&amp;#95;only__ &#x3D; The relationship is incomplete. Only relationships for first-party components, services, or their dependencies are represented, limited specifically to those that are opensource. * __incomplete&amp;#95;third&amp;#95;party&amp;#95;only__ &#x3D; The relationship is incomplete. Only relationships for third-party components, services, or their dependencies are represented. * __incomplete&amp;#95;third&amp;#95;party&amp;#95;proprietary&amp;#95;only__ &#x3D; The relationship is incomplete. Only relationships for third-party components, services, or their dependencies are represented, limited specifically to those that are proprietary. * __incomplete&amp;#95;third&amp;#95;party&amp;#95;opensource&amp;#95;only__ &#x3D; The relationship is incomplete. Only relationships for third-party components, services, or their dependencies are represented, limited specifically to those that are opensource. * __unknown__ &#x3D; The relationship may be complete or incomplete. This usually signifies a &#39;best-effort&#39; to obtain constituent components, services, or dependencies but the completeness is inconclusive. * __not&amp;#95;specified__ &#x3D; The relationship completeness is not specified.  | 
**assemblies** | **List[str]** | The bom-ref identifiers of the components or services being described. Assemblies refer to nested relationships whereby a constituent part may include other constituent parts. References do not cascade to child parts. References are explicit for the specified constituent part only. | [optional] 
**dependencies** | **List[str]** | The bom-ref identifiers of the components or services being described. Assemblies refer to nested relationships whereby a constituent part may include other constituent parts. References do not cascade to child parts. References are explicit for the specified constituent part only. | [optional] 

## Example

```python
from sysdig_client.models.compositions_inner import CompositionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompositionsInner from a JSON string
compositions_inner_instance = CompositionsInner.from_json(json)
# print the JSON string representation of the object
print(CompositionsInner.to_json())

# convert the object into a dict
compositions_inner_dict = compositions_inner_instance.to_dict()
# create an instance of CompositionsInner from a dict
compositions_inner_from_dict = CompositionsInner.from_dict(compositions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


