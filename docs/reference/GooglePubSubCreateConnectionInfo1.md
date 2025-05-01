# GooglePubSubCreateConnectionInfo1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | **str** | GCP project ID hosting the target pub/sub | 
**topic** | **str** | pub/sub topic onto which publish the data | 
**ordering_key** | **str** | The key to use to order the messages. Required to enable ordered delivery | [optional] 
**attributes** | [**List[KeyValueObject]**](KeyValueObject.md) | Extra headers to add to the request. Each header mapping requires 2 keys: \&quot;key\&quot; for the header key and \&quot;value\&quot; for its value | [optional] 
**credentials_json** | **str** | JSON credentials for the service account Sysdig will use to send data | [optional] 

## Example

```python
from sysdig_client.models.google_pub_sub_create_connection_info1 import GooglePubSubCreateConnectionInfo1

# TODO update the JSON string below
json = "{}"
# create an instance of GooglePubSubCreateConnectionInfo1 from a JSON string
google_pub_sub_create_connection_info1_instance = GooglePubSubCreateConnectionInfo1.from_json(json)
# print the JSON string representation of the object
print(GooglePubSubCreateConnectionInfo1.to_json())

# convert the object into a dict
google_pub_sub_create_connection_info1_dict = google_pub_sub_create_connection_info1_instance.to_dict()
# create an instance of GooglePubSubCreateConnectionInfo1 from a dict
google_pub_sub_create_connection_info1_from_dict = GooglePubSubCreateConnectionInfo1.from_dict(google_pub_sub_create_connection_info1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


