# CreateRiskAcceptedRequestAllOfContext

If entityType is not `vulnerability` or `policyRule`, you should use `Empty Matcher` in the context.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from sysdig_client.models.create_risk_accepted_request_all_of_context import CreateRiskAcceptedRequestAllOfContext

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRiskAcceptedRequestAllOfContext from a JSON string
create_risk_accepted_request_all_of_context_instance = CreateRiskAcceptedRequestAllOfContext.from_json(json)
# print the JSON string representation of the object
print(CreateRiskAcceptedRequestAllOfContext.to_json())

# convert the object into a dict
create_risk_accepted_request_all_of_context_dict = create_risk_accepted_request_all_of_context_instance.to_dict()
# create an instance of CreateRiskAcceptedRequestAllOfContext from a dict
create_risk_accepted_request_all_of_context_from_dict = CreateRiskAcceptedRequestAllOfContext.from_dict(create_risk_accepted_request_all_of_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


