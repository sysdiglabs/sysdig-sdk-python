# ContainerInfo

Kubernetes container information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pod_name** | **str** | Pod name | 
**container_id** | **str** | Container id. | 
**container_name** | **str** | Container name. | 
**pull_string** | **str** | Pull string for image used for the container. | [optional] 

## Example

```python
from sysdig_client.models.container_info import ContainerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerInfo from a JSON string
container_info_instance = ContainerInfo.from_json(json)
# print the JSON string representation of the object
print(ContainerInfo.to_json())

# convert the object into a dict
container_info_dict = container_info_instance.to_dict()
# create an instance of ContainerInfo from a dict
container_info_from_dict = ContainerInfo.from_dict(container_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


