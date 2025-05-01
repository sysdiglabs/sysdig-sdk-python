# PrivateConnectionInfoGooglePubSub


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials_json** | **str** | JSON credentials for the service account Sysdig will use to send data | [optional] 

## Example

```python
from sysdig_client.models.private_connection_info_google_pub_sub import PrivateConnectionInfoGooglePubSub

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateConnectionInfoGooglePubSub from a JSON string
private_connection_info_google_pub_sub_instance = PrivateConnectionInfoGooglePubSub.from_json(json)
# print the JSON string representation of the object
print(PrivateConnectionInfoGooglePubSub.to_json())

# convert the object into a dict
private_connection_info_google_pub_sub_dict = private_connection_info_google_pub_sub_instance.to_dict()
# create an instance of PrivateConnectionInfoGooglePubSub from a dict
private_connection_info_google_pub_sub_from_dict = PrivateConnectionInfoGooglePubSub.from_dict(private_connection_info_google_pub_sub_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


