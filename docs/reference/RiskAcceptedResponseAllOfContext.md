# RiskAcceptedResponseAllOfContext

If entityType is not `vulnerability` or `policyRule`, you should use `Empty Matcher` in the context.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from sysdig_client.models.risk_accepted_response_all_of_context import RiskAcceptedResponseAllOfContext

# TODO update the JSON string below
json = "{}"
# create an instance of RiskAcceptedResponseAllOfContext from a JSON string
risk_accepted_response_all_of_context_instance = RiskAcceptedResponseAllOfContext.from_json(json)
# print the JSON string representation of the object
print(RiskAcceptedResponseAllOfContext.to_json())

# convert the object into a dict
risk_accepted_response_all_of_context_dict = risk_accepted_response_all_of_context_instance.to_dict()
# create an instance of RiskAcceptedResponseAllOfContext from a dict
risk_accepted_response_all_of_context_from_dict = RiskAcceptedResponseAllOfContext.from_dict(risk_accepted_response_all_of_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


