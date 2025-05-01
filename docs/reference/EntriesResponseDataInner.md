# EntriesResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The audit event id. | 
**timestamp** | **int** | Timestamp the audit event occured, expressed in nanoseconds. | 
**type** | **str** | The entry type | 
**container_id** | **str** | The container id. &#x60;containerId&#x60; is present only if the audit event was collected in a container context.  | 
**cmdline** | **str** | Full command line | 
**comm** | **str** | The name of the command. | 
**pcomm** | **str** | The name of the parent command. | 
**pid** | **int** | Id of the process owning the connection. | 
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
**dns_domains** | **List[str]** | DNS information for the connection event. | [default to []]
**process_name** | **str** | Name of the process owning the connection. | 
**client_ipv4** | **str** | The IPv4 dotted notation of the client address. | 
**client_port** | **int** | The client port. | 
**server_ipv4** | **str** | The IPv4 dotted notation of the server address. | 
**server_port** | **int** | The server port. | 
**direction** | **str** | The direction of the connection. | 
**l4protocol** | **str** | The layer 4 protocol. | 
**directory** | **str** | The Directory for the file access. | 
**filename** | **str** | The Filename involved in file access. | 
**permissions** | **str** | The Permissions of the file access. | 
**resource** | **str** | The Kubernetes resource. | 
**sub_resource** | **str** | The Kubernetes subresource. | 
**namespace** | **str** | The Kubernetes namespace. | 
**name** | **str** | The name of the resource. | 
**source_addresses** | **List[str]** |  | 
**user** | [**User**](User.md) |  | 
**user_agent** | **str** | The user agent of the client | 
**args** | **object** | Arguments specific for the different types of Kubernetes audit entries. In case of &#x60;pods:exec&#x60;, &#x60;args&#x60; will contain the fields &#x60;command&#x60; and &#x60;container&#x60; representing the command called and the name of the container in the pod where the command was executed respectively.  | 

## Example

```python
from sysdig_client.models.entries_response_data_inner import EntriesResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of EntriesResponseDataInner from a JSON string
entries_response_data_inner_instance = EntriesResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(EntriesResponseDataInner.to_json())

# convert the object into a dict
entries_response_data_inner_dict = entries_response_data_inner_instance.to_dict()
# create an instance of EntriesResponseDataInner from a dict
entries_response_data_inner_from_dict = EntriesResponseDataInner.from_dict(entries_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


