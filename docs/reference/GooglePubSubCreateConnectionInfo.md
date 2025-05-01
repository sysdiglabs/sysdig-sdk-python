# GooglePubSubCreateConnectionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | **str** | GCP project ID hosting the target pub/sub | 
**topic** | **str** | pub/sub topic onto which publish the data | 
**ordering_key** | **str** | The key to use to order the messages. Required to enable ordered delivery | [optional] 
**attributes** | [**List[KeyValueObject]**](KeyValueObject.md) | Extra headers to add to the request. Each header mapping requires 2 keys: \&quot;key\&quot; for the header key and \&quot;value\&quot; for its value | [optional] 
**credentials_json** | **str** | JSON credentials for the service account Sysdig will use to send data | 

## Example

```python
from sysdig_client.models.google_pub_sub_create_connection_info import GooglePubSubCreateConnectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GooglePubSubCreateConnectionInfo from a JSON string
google_pub_sub_create_connection_info_instance = GooglePubSubCreateConnectionInfo.from_json(json)
# print the JSON string representation of the object
print(GooglePubSubCreateConnectionInfo.to_json())

# convert the object into a dict
google_pub_sub_create_connection_info_dict = google_pub_sub_create_connection_info_instance.to_dict()
# create an instance of GooglePubSubCreateConnectionInfo from a dict
google_pub_sub_create_connection_info_from_dict = GooglePubSubCreateConnectionInfo.from_dict(google_pub_sub_create_connection_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


