# CreatePolicyRequest

A Policy definition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | human readable policy name | 
**description** | **str** | policy description | [optional] 
**bundles** | [**List[BundleRef]**](BundleRef.md) | bundles defining this policy | 
**stages** | [**List[NewStage]**](NewStage.md) | array of stages for the policy.  An empty array means the policy is applied only when specifically requested by its identifier.  | [optional] 

## Example

```python
from sysdig_client.models.create_policy_request import CreatePolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePolicyRequest from a JSON string
create_policy_request_instance = CreatePolicyRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePolicyRequest.to_json())

# convert the object into a dict
create_policy_request_dict = create_policy_request_instance.to_dict()
# create an instance of CreatePolicyRequest from a dict
create_policy_request_from_dict = CreatePolicyRequest.from_dict(create_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


