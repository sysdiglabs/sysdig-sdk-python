# GetPolicyResponse

A Policy definition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the Policy ID | 
**name** | **str** | human readable policy name | 
**identifier** | **str** | policy identifier generated from the name | 
**description** | **str** | policy description | [optional] 
**bundles** | [**List[BundleRef]**](BundleRef.md) | bundles defining this policy | 
**stages** | [**List[Stage]**](Stage.md) | array of stages for the policy.  An empty array means the policy is applied only when specifically requested by its identifier.  | 

## Example

```python
from sysdig_client.models.get_policy_response import GetPolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPolicyResponse from a JSON string
get_policy_response_instance = GetPolicyResponse.from_json(json)
# print the JSON string representation of the object
print(GetPolicyResponse.to_json())

# convert the object into a dict
get_policy_response_dict = get_policy_response_instance.to_dict()
# create an instance of GetPolicyResponse from a dict
get_policy_response_from_dict = GetPolicyResponse.from_dict(get_policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


