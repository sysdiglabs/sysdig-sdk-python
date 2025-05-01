# UnitPricingV1

The unit pricing configuration used to compute costs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **float** | Hourly cost of one CPU. | 
**ram** | **float** | Hourly cost of one GB of RAM. | 
**storage** | **float** | Hourly cost of one GB of storage. | 
**spot_cpu** | **float** | Hourly cost of one CPU for a spot node. | [optional] 
**spot_ram** | **float** | Hourly cost of one GB of RAM for a spot node. | [optional] 

## Example

```python
from sysdig_client.models.unit_pricing_v1 import UnitPricingV1

# TODO update the JSON string below
json = "{}"
# create an instance of UnitPricingV1 from a JSON string
unit_pricing_v1_instance = UnitPricingV1.from_json(json)
# print the JSON string representation of the object
print(UnitPricingV1.to_json())

# convert the object into a dict
unit_pricing_v1_dict = unit_pricing_v1_instance.to_dict()
# create an instance of UnitPricingV1 from a dict
unit_pricing_v1_from_dict = UnitPricingV1.from_dict(unit_pricing_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


