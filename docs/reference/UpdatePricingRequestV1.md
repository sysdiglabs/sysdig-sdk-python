# UpdatePricingRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PricingType**](PricingType.md) |  | 
**cluster_name** | **str** | The name of the cluster. Required when &#x60;type&#x60; is &#x60;CLUSTER&#x60;. | [optional] 
**name** | **str** | The name of the pricing profile. | 
**unit_pricing** | [**UnitPricingV1**](UnitPricingV1.md) | The unit pricing configuration used to compute costs. | 
**spot_label** | **str** | The name of a node label that is used to identify the node as a spot node. | [optional] 
**spot_label_value** | **str** | The value of the spot node label. | [optional] 
**version** | **int** | The current version of the resource.  | 

## Example

```python
from sysdig_client.models.update_pricing_request_v1 import UpdatePricingRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePricingRequestV1 from a JSON string
update_pricing_request_v1_instance = UpdatePricingRequestV1.from_json(json)
# print the JSON string representation of the object
print(UpdatePricingRequestV1.to_json())

# convert the object into a dict
update_pricing_request_v1_dict = update_pricing_request_v1_instance.to_dict()
# create an instance of UpdatePricingRequestV1 from a dict
update_pricing_request_v1_from_dict = UpdatePricingRequestV1.from_dict(update_pricing_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


