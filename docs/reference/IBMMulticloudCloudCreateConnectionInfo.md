# IBMMulticloudCloudCreateConnectionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | The URL, including protocol and port (if non standard), to your IBM Cloud Pak for Multicloud Management API endpoint | 
**account_id** | **str** | IBM Account ID | [optional] [default to 'id-mycluster-account']
**provider_id** | **str** | The provider the findings will be associated to | [optional] [default to 'sysdig-secure']
**note_name** | **str** | The note to use. If unspecified, a note with &#x60;policy-event&#x60; ID will be created and used | [optional] 
**is_insecure** | **bool** | Skip TLS certificate verification | [optional] [default to False]
**api_key** | **str** | IBM Cloud API Key | 

## Example

```python
from sysdig_client.models.ibm_multicloud_cloud_create_connection_info import IBMMulticloudCloudCreateConnectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IBMMulticloudCloudCreateConnectionInfo from a JSON string
ibm_multicloud_cloud_create_connection_info_instance = IBMMulticloudCloudCreateConnectionInfo.from_json(json)
# print the JSON string representation of the object
print(IBMMulticloudCloudCreateConnectionInfo.to_json())

# convert the object into a dict
ibm_multicloud_cloud_create_connection_info_dict = ibm_multicloud_cloud_create_connection_info_instance.to_dict()
# create an instance of IBMMulticloudCloudCreateConnectionInfo from a dict
ibm_multicloud_cloud_create_connection_info_from_dict = IBMMulticloudCloudCreateConnectionInfo.from_dict(ibm_multicloud_cloud_create_connection_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


