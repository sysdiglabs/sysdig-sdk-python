# Command

Represents a command execution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The audit event id. | 
**timestamp** | **int** | Timestamp the audit event occured, expressed in nanoseconds. | 
**type** | **str** | The entry type | 
**container_id** | **str** | The container id. &#x60;containerId&#x60; is present only if the audit event was collected in a container context.  | [optional] 
**cmdline** | **str** | Full command line | 
**comm** | **str** | The name of the command. | 
**pcomm** | **str** | The name of the parent command. | 
**pid** | **int** | Process ID. | 
**ppid** | **int** | Parent process ID. | 
**uid** | **int** | User ID | 
**username** | **str** | Username | [optional] 
**cwd** | **str** | Command working directory. | 
**login_shell_id** | **int** | Process id of the shell. | 
**login_shell_distance** | **int** | Level of nesting from the parent shell. | 
**hostname** | **str** | The Kubernetes hostname. | 
**tty** | **int** | TTY number. | 
**user_login_uid** | **int** | User login UID. | 
**user_login_name** | **str** | User login name. | 
**proc_exepath** | **str** | Process executable path. | 
**labels** | **Dict[str, str]** | Key value pairs of labels. | [optional] 

## Example

```python
from sysdig_client.models.command import Command

# TODO update the JSON string below
json = "{}"
# create an instance of Command from a JSON string
command_instance = Command.from_json(json)
# print the JSON string representation of the object
print(Command.to_json())

# convert the object into a dict
command_dict = command_instance.to_dict()
# create an instance of Command from a dict
command_from_dict = Command.from_dict(command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


