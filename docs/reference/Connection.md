# Connection

Represents a connection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The audit event id. | 
**timestamp** | **int** | Timestamp the audit event occured, expressed in nanoseconds. | 
**type** | **str** | The entry type | 
**cmdline** | **str** | Full command line | 
**comm** | **str** | The name of the command. | 
**dns_domains** | **List[str]** | DNS information for the connection event. | [default to []]
**container_id** | **str** | The container id. &#x60;containerId&#x60; is present only if the audit event was collected in a container context.  | 
**pid** | **int** | Id of the process owning the connection. | 
**process_name** | **str** | Name of the process owning the connection. | 
**client_ipv4** | **str** | The IPv4 dotted notation of the client address. | 
**client_port** | **int** | The client port. | 
**server_ipv4** | **str** | The IPv4 dotted notation of the server address. | 
**server_port** | **int** | The server port. | 
**direction** | **str** | The direction of the connection. | 
**l4protocol** | **str** | The layer 4 protocol. | 
**hostname** | **str** | The Kubernetes hostname. | 
**tty** | **int** | TTY number. | 
**labels** | **Dict[str, str]** | Key value pairs of labels. | [optional] 

## Example

```python
from sysdig_client.models.connection import Connection

# TODO update the JSON string below
json = "{}"
# create an instance of Connection from a JSON string
connection_instance = Connection.from_json(json)
# print the JSON string representation of the object
print(Connection.to_json())

# convert the object into a dict
connection_dict = connection_instance.to_dict()
# create an instance of Connection from a dict
connection_from_dict = Connection.from_dict(connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


