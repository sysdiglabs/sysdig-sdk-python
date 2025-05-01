# Kubernetes

Represents a kubernetes audit event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The audit event id. | 
**timestamp** | **int** | Timestamp the audit event occured, expressed in nanoseconds. | 
**type** | **str** | The entry type | 
**hostname** | **str** | The Kubernetes hostname. | 
**container_id** | **str** | The container id. &#x60;containerId&#x60; is present only if the audit event was collected in a container context.  | 
**resource** | **str** | The Kubernetes resource. | 
**sub_resource** | **str** | The Kubernetes subresource. | 
**namespace** | **str** | The Kubernetes namespace. | 
**name** | **str** | The name of the resource. | 
**source_addresses** | **List[str]** |  | 
**user** | [**User**](User.md) |  | 
**user_agent** | **str** | The user agent of the client | 
**args** | **object** | Arguments specific for the different types of Kubernetes audit entries. In case of &#x60;pods:exec&#x60;, &#x60;args&#x60; will contain the fields &#x60;command&#x60; and &#x60;container&#x60; representing the command called and the name of the container in the pod where the command was executed respectively.  | 
**labels** | **Dict[str, str]** | Key value pairs of labels. | [optional] 

## Example

```python
from sysdig_client.models.kubernetes import Kubernetes

# TODO update the JSON string below
json = "{}"
# create an instance of Kubernetes from a JSON string
kubernetes_instance = Kubernetes.from_json(json)
# print the JSON string representation of the object
print(Kubernetes.to_json())

# convert the object into a dict
kubernetes_dict = kubernetes_instance.to_dict()
# create an instance of Kubernetes from a dict
kubernetes_from_dict = Kubernetes.from_dict(kubernetes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


