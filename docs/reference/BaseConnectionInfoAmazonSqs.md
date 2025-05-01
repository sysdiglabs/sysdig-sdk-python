# BaseConnectionInfoAmazonSqs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_account** | **str** | The AWS account ID of the account that created the queue | [optional] 
**region** | **str** | Region in which the SQS queue is hosted | 
**queue** | **str** | Queue name | 
**delay** | **int** | Delay, in seconds, applied to the data | [optional] 
**headers** | [**List[KeyValueObject]**](KeyValueObject.md) | Extra headers to add to the payload. Each header mapping requires 2 keys: &#39;key&#39; for the header key and &#39;value&#39; for its value | [optional] 

## Example

```python
from sysdig_client.models.base_connection_info_amazon_sqs import BaseConnectionInfoAmazonSqs

# TODO update the JSON string below
json = "{}"
# create an instance of BaseConnectionInfoAmazonSqs from a JSON string
base_connection_info_amazon_sqs_instance = BaseConnectionInfoAmazonSqs.from_json(json)
# print the JSON string representation of the object
print(BaseConnectionInfoAmazonSqs.to_json())

# convert the object into a dict
base_connection_info_amazon_sqs_dict = base_connection_info_amazon_sqs_instance.to_dict()
# create an instance of BaseConnectionInfoAmazonSqs from a dict
base_connection_info_amazon_sqs_from_dict = BaseConnectionInfoAmazonSqs.from_dict(base_connection_info_amazon_sqs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


