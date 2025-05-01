# PrivateConnectionInfoAmazonSqs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** | Access Key for authenticating on AWS to send data on the queue | [optional] 
**access_secret** | **str** | Access Secret for authenticating on AWS to send data on the queue | [optional] 

## Example

```python
from sysdig_client.models.private_connection_info_amazon_sqs import PrivateConnectionInfoAmazonSqs

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateConnectionInfoAmazonSqs from a JSON string
private_connection_info_amazon_sqs_instance = PrivateConnectionInfoAmazonSqs.from_json(json)
# print the JSON string representation of the object
print(PrivateConnectionInfoAmazonSqs.to_json())

# convert the object into a dict
private_connection_info_amazon_sqs_dict = private_connection_info_amazon_sqs_instance.to_dict()
# create an instance of PrivateConnectionInfoAmazonSqs from a dict
private_connection_info_amazon_sqs_from_dict = PrivateConnectionInfoAmazonSqs.from_dict(private_connection_info_amazon_sqs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


