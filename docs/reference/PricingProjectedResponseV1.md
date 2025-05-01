# PricingProjectedResponseV1

The monthly projected cost for a specific cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** | The name of the cluster. | [optional] 
**monthly_projected_cost** | **float** | Monthly projected cost. | [optional] 

## Example

```python
from sysdig_client.models.pricing_projected_response_v1 import PricingProjectedResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of PricingProjectedResponseV1 from a JSON string
pricing_projected_response_v1_instance = PricingProjectedResponseV1.from_json(json)
# print the JSON string representation of the object
print(PricingProjectedResponseV1.to_json())

# convert the object into a dict
pricing_projected_response_v1_dict = pricing_projected_response_v1_instance.to_dict()
# create an instance of PricingProjectedResponseV1 from a dict
pricing_projected_response_v1_from_dict = PricingProjectedResponseV1.from_dict(pricing_projected_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


