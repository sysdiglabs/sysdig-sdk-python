# BaseConnectionInfoGooglePubSub


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | **str** | GCP project ID hosting the target pub/sub | 
**topic** | **str** | pub/sub topic onto which publish the data | 
**ordering_key** | **str** | The key to use to order the messages. Required to enable ordered delivery | [optional] 
**attributes** | [**List[KeyValueObject]**](KeyValueObject.md) | Extra headers to add to the request. Each header mapping requires 2 keys: \&quot;key\&quot; for the header key and \&quot;value\&quot; for its value | [optional] 

## Example

```python
from sysdig_client.models.base_connection_info_google_pub_sub import BaseConnectionInfoGooglePubSub

# TODO update the JSON string below
json = "{}"
# create an instance of BaseConnectionInfoGooglePubSub from a JSON string
base_connection_info_google_pub_sub_instance = BaseConnectionInfoGooglePubSub.from_json(json)
# print the JSON string representation of the object
print(BaseConnectionInfoGooglePubSub.to_json())

# convert the object into a dict
base_connection_info_google_pub_sub_dict = base_connection_info_google_pub_sub_instance.to_dict()
# create an instance of BaseConnectionInfoGooglePubSub from a dict
base_connection_info_google_pub_sub_from_dict = BaseConnectionInfoGooglePubSub.from_dict(base_connection_info_google_pub_sub_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


