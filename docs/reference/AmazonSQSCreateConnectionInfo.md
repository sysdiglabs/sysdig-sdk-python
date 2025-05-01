# AmazonSQSCreateConnectionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_account** | **str** | The AWS account ID of the account that created the queue | [optional] 
**region** | **str** | Region in which the SQS queue is hosted | 
**queue** | **str** | Queue name | 
**delay** | **int** | Delay, in seconds, applied to the data | [optional] 
**headers** | [**List[KeyValueObject]**](KeyValueObject.md) | Extra headers to add to the payload. Each header mapping requires 2 keys: &#39;key&#39; for the header key and &#39;value&#39; for its value | [optional] 
**access_key** | **str** | Access Key for authenticating on AWS to send data on the queue | 
**access_secret** | **str** | Access Secret for authenticating on AWS to send data on the queue | 

## Example

```python
from sysdig_client.models.amazon_sqs_create_connection_info import AmazonSQSCreateConnectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonSQSCreateConnectionInfo from a JSON string
amazon_sqs_create_connection_info_instance = AmazonSQSCreateConnectionInfo.from_json(json)
# print the JSON string representation of the object
print(AmazonSQSCreateConnectionInfo.to_json())

# convert the object into a dict
amazon_sqs_create_connection_info_dict = amazon_sqs_create_connection_info_instance.to_dict()
# create an instance of AmazonSQSCreateConnectionInfo from a dict
amazon_sqs_create_connection_info_from_dict = AmazonSQSCreateConnectionInfo.from_dict(amazon_sqs_create_connection_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


