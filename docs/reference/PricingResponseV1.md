# PricingResponseV1

The pricing configuration used to compute costs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |   | [optional] 
**type** | [**PricingType**](PricingType.md) |  | [optional] 
**cluster_name** | **str** | The name of the cluster. Required when &#x60;type&#x60; is &#x60;CLUSTER&#x60;. | [optional] 
**name** | **str** | The name of the pricing profile. | [optional] 
**unit_pricing** | [**UnitPricingV1**](UnitPricingV1.md) | The unit pricing configuration used to compute costs. | [optional] 
**spot_label** | **str** | The name of a node label that is used to identify the node as a spot node. | [optional] 
**spot_label_value** | **str** | The value of the spot node label. | [optional] 
**version** | **int** | The current version of the resource.  | [optional] 

## Example

```python
from sysdig_client.models.pricing_response_v1 import PricingResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of PricingResponseV1 from a JSON string
pricing_response_v1_instance = PricingResponseV1.from_json(json)
# print the JSON string representation of the object
print(PricingResponseV1.to_json())

# convert the object into a dict
pricing_response_v1_dict = pricing_response_v1_instance.to_dict()
# create an instance of PricingResponseV1 from a dict
pricing_response_v1_from_dict = PricingResponseV1.from_dict(pricing_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


