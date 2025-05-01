# Fileaccess

Represents a file access operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The audit event id. | 
**timestamp** | **int** | Timestamp the audit event occured, expressed in nanoseconds. | 
**type** | **str** | The entry type | 
**hostname** | **str** | The Kubernetes hostname. | 
**container_id** | **str** | The container id. &#x60;containerId&#x60; is present only if the audit event was collected in a container context.  | [optional] 
**comm** | **str** | The name of the command. | 
**pid** | **int** | Id of the process owning the connection. | 
**directory** | **str** | The Directory for the file access. | 
**filename** | **str** | The Filename involved in file access. | 
**permissions** | **str** | The Permissions of the file access. | 
**tty** | **int** | TTY number. | [optional] 
**labels** | **Dict[str, str]** | Key value pairs of labels. | [optional] 

## Example

```python
from sysdig_client.models.fileaccess import Fileaccess

# TODO update the JSON string below
json = "{}"
# create an instance of Fileaccess from a JSON string
fileaccess_instance = Fileaccess.from_json(json)
# print the JSON string representation of the object
print(Fileaccess.to_json())

# convert the object into a dict
fileaccess_dict = fileaccess_instance.to_dict()
# create an instance of Fileaccess from a dict
fileaccess_from_dict = Fileaccess.from_dict(fileaccess_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


