# GoogleSCCCreateConnectionInfo1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization** | **str** | ID of your GCP organization | 
**security_marks** | [**List[KeyValueObject]**](KeyValueObject.md) | additional annotations to add to assets or findings as they get forwarded to Security Command Center | [optional] 
**credentials_json** | **str** | JSON credentials for the service account Sysdig will use to send data | [optional] 

## Example

```python
from sysdig_client.models.google_scc_create_connection_info1 import GoogleSCCCreateConnectionInfo1

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleSCCCreateConnectionInfo1 from a JSON string
google_scc_create_connection_info1_instance = GoogleSCCCreateConnectionInfo1.from_json(json)
# print the JSON string representation of the object
print(GoogleSCCCreateConnectionInfo1.to_json())

# convert the object into a dict
google_scc_create_connection_info1_dict = google_scc_create_connection_info1_instance.to_dict()
# create an instance of GoogleSCCCreateConnectionInfo1 from a dict
google_scc_create_connection_info1_from_dict = GoogleSCCCreateConnectionInfo1.from_dict(google_scc_create_connection_info1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


