# PolicyEvaluation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | policy evaluation name | 
**identifier** | **str** | policy evaluation id | 
**description** | **str** | policy evaluation description | [optional] 
**bundles** | [**List[Bundle]**](Bundle.md) |  | [optional] 
**evaluation** | **str** |  | 
**created_at** | **str** | datetime of creation | 
**updated_at** | **str** | datetime of last update | 

## Example

```python
from sysdig_client.models.policy_evaluation import PolicyEvaluation

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyEvaluation from a JSON string
policy_evaluation_instance = PolicyEvaluation.from_json(json)
# print the JSON string representation of the object
print(PolicyEvaluation.to_json())

# convert the object into a dict
policy_evaluation_dict = policy_evaluation_instance.to_dict()
# create an instance of PolicyEvaluation from a dict
policy_evaluation_from_dict = PolicyEvaluation.from_dict(policy_evaluation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


