# GoogleSCCCreateConnectionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization** | **str** | ID of your GCP organization | 
**security_marks** | [**List[KeyValueObject]**](KeyValueObject.md) | additional annotations to add to assets or findings as they get forwarded to Security Command Center | [optional] 
**credentials_json** | **str** | JSON credentials for the service account Sysdig will use to send data | 

## Example

```python
from sysdig_client.models.google_scc_create_connection_info import GoogleSCCCreateConnectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleSCCCreateConnectionInfo from a JSON string
google_scc_create_connection_info_instance = GoogleSCCCreateConnectionInfo.from_json(json)
# print the JSON string representation of the object
print(GoogleSCCCreateConnectionInfo.to_json())

# convert the object into a dict
google_scc_create_connection_info_dict = google_scc_create_connection_info_instance.to_dict()
# create an instance of GoogleSCCCreateConnectionInfo from a dict
google_scc_create_connection_info_from_dict = GoogleSCCCreateConnectionInfo.from_dict(google_scc_create_connection_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


